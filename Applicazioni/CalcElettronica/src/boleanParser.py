from src.utilities import validaParentesi, is_number, write_error, write_output, wait_user_input

VARIABILI = dict()

class BitwiseParser:
    def __init__(self):
        self.operators = {
            '&': 'AND',
            '|': 'OR',
            '^': 'XOR',
            '~': 'NOT',
            '<': 'LSHIFT',
            '>': 'RSHIFT',
            '(': 'LPAREN',
            ')': 'RPAREN',
            '=': 'ASSIGN',
        }

    def tokenize(self, expression):
        tokens = []
        current_token = ''
        for char in expression:
            if char.isspace():
                continue
            if char in self.operators:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            else:
                current_token += char
        if current_token:
            tokens.append(current_token)
        return tokens
    
    def evalWithParentesis(self, expr : list[str]):
        try:
            if validaParentesi(expr):
                expr.append(')')
                expr.insert(0,'(')
            else:
                return None
        except Exception as e:
            write_error(f"Espressione non valida: {e}")
            return None

        ris = None
        stack = []
        for i in range(len(expr)):
            token = expr[i]
            if token == ')':
                # Estraggo la sottospressione
                sub_expr = []
                while stack and stack[-1] != '(':
                    sub_expr.insert(0, stack[-1])
                    stack.pop()

                if not stack:
                    write_error("Espressione non valida: parentesi non bilanciate.")
                    return None

                if not sub_expr:
                    write_error("Espressione non valida: parentesi vuote.")
                    return None
                
                # Valuto la sottospressione
                ris = self.processa(sub_expr)
                if ris is not None:
                    stack[-1] = str(ris)  # Sostituisco '(' con il risultato
                else:
                    write_error("Errore nella valutazione della sottospressione.")
                    return None
            else:
                stack.append(token)

        return ris
    
    def processa(self, expr : list[str]):
        if not expr:
            write_error("Espressione non valida: nessun contenuto da valutare.")
            return None

        if '=' in expr and len(expr) >= 3:
            if expr[1] == '=' and self.validaNomeVariabile(expr[0]):
                variabile = expr[0]
                valore_expr = expr[2:]
                valore = self.processa(valore_expr)
                if valore is not None:
                    VARIABILI[variabile] = valore
                    return valore
                else:
                    write_error("Errore nella valutazione dell'espressione di assegnazione.")
                    return None
                
        i = 0
        lunghezza = len(expr)
        while i < lunghezza:
            token = expr[i]
                
            if self.ciSonoVar(expr):
                expr = self.convretVars(expr, VARIABILI)
                lunghezza = len(expr)
                i = 0
                continue

            if token in "&|^<>" and i+1 < lunghezza and i != 0:
                try:
                    if is_number(expr[i-1]) and is_number(expr[i+1]):
                        a , b = int(expr[i-1]), int(expr[i+1])
                    else:
                        return None
                    
                    match token:
                        case '&':
                            ris = a & b

                        case '|':
                            ris = a | b

                        case '^':
                            ris = a ^ b

                        case '>':
                            ris = a >> b

                        case '<':
                            ris = a << b
                    
                    expr[i] = str(ris)
                    expr.pop(i+1)
                    expr.pop(i-1)
                    lunghezza-=2
                    i-=1
                    
                except Exception as e:
                    write_error(f"ERRORE: {e}")
                    return None
                
            elif token == "~" and i+1 < lunghezza:
                if is_number(expr[i+1]):
                    a = int(expr[i+1])
                else:
                    write_error("Espressione non valida: NOT richiede un numero dopo '~'.")
                    return None
                
                expr[i] = ~a
                expr.pop(i+1)
                lunghezza -= 1
            
            i+=1

        if len(expr) != 1:
            write_error("Espressione non valida: operatori o operandi mancanti.")
            return None

        return expr[0]
    
    def _to_base_without_prefix(self, value: int, base: int) -> str:
        if base not in (2, 16):
            raise ValueError("Base non supportata")

        sign = "-" if value < 0 else ""
        raw = format(abs(value), "b" if base == 2 else "x")
        return f"{sign}{raw}"

    def _render_clean_table(self, headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> list[str]:
        widths = [len(header) for header in headers]
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(cell))

        header_line = " | ".join(header.ljust(widths[i]) for i, header in enumerate(headers))
        separator = "-+-".join("-" * width for width in widths)
        body = [" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)) for row in rows]
        return [header_line, separator, *body]

    
    def stampaConfigurazione(self,n : int):
        rows = [(
            str(n),
            self._to_base_without_prefix(n, 2),
            self._to_base_without_prefix(n, 16),
        )]
        for line in self._render_clean_table(("DEC", "BIN", "HEX"), rows):
            write_output(line)
        
    def validate(self, expr : list[str]):
        assignment_index = expr.index('=') if '=' in expr else -1

        for i, token in enumerate(expr):
            if token in self.operators or is_number(token):
                continue

            if not self.validaNomeVariabile(token):
                write_error(f"Token non valido: '{token}'")
                return False

            # LHS di assegnamento: permetti variabile nuova, es: x = 5
            if assignment_index == 1 and i == 0:
                continue

            if token not in VARIABILI:
                write_error(f"Variabile non definita: '{token}'")
                return False

        return True
    
    def validaNomeVariabile(self, nome : str):
        if nome in self.operators:
            return False
        if is_number(nome):
            return False
        return True

    def convretVars(self, tokens : list[str], variabili : dict):
        new_tokens = []
        for token in tokens:
            if token in variabili:
                new_tokens.append(variabili[token])
            elif token in self.operators or is_number(token):
                new_tokens.append(token)
        
        return new_tokens
    
    def ciSonoVar(self, expr : list[str]) -> bool:
        return any(token in VARIABILI for token in expr)
    
    
