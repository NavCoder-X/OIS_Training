from src.utilities import validaParentesi, is_number
from colorama import Fore
from src.Headers import bitwiseHeader, clear
from src.espressioni import show

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
        if validaParentesi(expr):
            expr.append(')')
            expr.insert(0,'(')
        else:
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
                
                # Valuto la sottospressione
                ris = self.processa(sub_expr)
                if ris is not None:
                    stack[-1] = str(ris)  # Sostituisco '(' con il risultato
                else:
                    print(Fore.RED + "Errore nella valutazione della sottospressione.")
                    return None
            else:
                stack.append(token)

        return ris
    
    def processa(self, expr : list[str]):
        if '=' in expr and len(expr) >= 3:
            if expr[1] == '=' and self.validaNomeVariabile(expr[0]):
                variabile = expr[0]
                valore_expr = expr[2:]
                valore = self.processa(valore_expr)
                if valore is not None:
                    VARIABILI[variabile] = valore
                    return valore
                else:
                    print(Fore.RED + "Errore nella valutazione dell'espressione di assegnazione.")
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
                    print(Fore.RED + f"ERRORE: {e}")
                    return None
                
            elif token == "~" and i+1 < lunghezza:
                if is_number(expr[i+1]):
                    a = int(expr[i+1])
                else:
                    return None
                
                expr[i] = ~a
                expr.pop(i+1)
                lunghezza -= 1
            
            i+=1
        return expr[0]
    
    def stampaInQuadrato(self, s : list[str], l):
        print(Fore.WHITE + "┌" + "─"*l +"┐" + Fore.CYAN + "┌" + "─"*l +"┐" + Fore.GREEN + "┌" + "─"*l +"┐")
        print(Fore.WHITE + "│" + s[0].center(l) + "│" + Fore.CYAN + "│" + s[1].center(l) + "│" + Fore.GREEN + "│" + s[2].center(l) + "│")
        print(Fore.WHITE + "└" + "─"*l + "┘" + Fore.CYAN + "└" + "─"*l + "┘" + Fore.GREEN + "└" + "─"*l + "┘")

    
    def stampaConfigurazione(self,n : int):
        b = str(bin(n))[2:]
        h = str(hex(n))[2:]
        n = str(n)
        l = max(len(b),len(h),len(n))+10
        self.stampaInQuadrato([n,b,h],l)
        
    def validate(self, expr : list[str]):
        for token in expr:
            if token not in self.operators and not is_number(token) and not self.validaNomeVariabile(token):
                print(Fore.RED + f"Token non valido: '{token}'")
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
    
    
def boolLoop():
    parser = BitwiseParser()
    while True:
        try:
            clear()
            bitwiseHeader()
            expr = input("Espressione: ").strip()
            if not expr:
                continue

            if expr == "show":
                show(VARIABILI)
                input(Fore.YELLOW + "Premi ENTER per continuare...")
                continue

            if expr == "confronta":
                a = input("Valore: ").strip()
                if a in VARIABILI:
                    a = VARIABILI[a]
                if not is_number(a):
                    print(Fore.RED + f"Valore non valido: '{a}'")
                    input(Fore.YELLOW + "Premi ENTER per continuare...")
                    continue
                
                while a != 'break':
                    parser.stampaConfigurazione(int(a))
                    a = input("Valore: ").strip()
                    if a in VARIABILI:
                        a = VARIABILI[a]
                    if not is_number(a):
                        print(Fore.RED + f"Valore non valido: '{a}'")
                        input(Fore.YELLOW + "Premi ENTER per continuare...")
                        continue

                input(Fore.YELLOW + "Premi ENTER per continuare...")
                continue

            tokens = parser.tokenize(expr)
            if not parser.validate(tokens):
                print(Fore.RED + "Espressione non valida. Assicurati di usare solo numeri e operatori bitwise (&, |, ^, ~, <, >).")
                input()
                continue

            result = parser.evalWithParentesis(tokens)
            if result is not None:
                result = int(result)
                VARIABILI['ris'] = str(result)
                print(Fore.GREEN + f"Risultato: {result}")
                parser.stampaConfigurazione(result)
            else:
                print(Fore.RED + "Errore nella valutazione dell'espressione.")
            
        except Exception as e:
            print(Fore.RED + f"Errore: {e}")

        input(Fore.YELLOW + "Premi ENTER per continuare...")