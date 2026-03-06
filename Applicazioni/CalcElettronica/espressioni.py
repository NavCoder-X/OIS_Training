from colorama import Fore, Style, init
from Headers import *
from operatori import *
from utilities import *
import ast
import operator

# Operatori sicuri per valutazione
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def safe_eval(expr_str: str) -> float | None:
    """Valuta in modo sicuro un'espressione matematica usando ast.
    
    Supporta solo operatori matematici di base (+, -, *, /, ^, -unario).
    
    Args:
        expr_str: Stringa dell'espressione da valutare
        
    Returns:
        Risultato numerico, None se errore
        
    Raises:
        ValueError: Se espressione non valida o contiene operazioni non consentite
        
    Example:
        >>> safe_eval("2 + 3 * 4")
        14.0
        >>> safe_eval("1 / 0")  # Ritorna None (divisione per zero)
    """
    try:
        expr_str = expr_str.replace('^', '**')
        node = ast.parse(expr_str, mode='eval')
        
        def evaluate(node):
            if isinstance(node, ast.Expression):
                return evaluate(node.body)
            elif isinstance(node, ast.Constant):
                return float(node.value)
            elif isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)
                if right == 0 and isinstance(node.op, ast.Div):
                    raise ValueError("Divisione per zero")
                return SAFE_OPERATORS[type(node.op)](left, right)
            elif isinstance(node, ast.UnaryOp):
                return SAFE_OPERATORS[type(node.op)](evaluate(node.operand))
            else:
                raise ValueError("Operazione non consentita")
        
        result = evaluate(node)
        return result
        
    except (SyntaxError, ValueError, ZeroDivisionError, KeyError) as e:
        return None

def gestisciOperatoreSpeciale(expr : list[str], variabili : dict) -> list[str] | None:
    """Gestisce operatori speciali per circuiti (P, PC, PT, KRAMER, |).
    
    Operatori speciali:
    - P>v,i: Potenza (V, I)
    - PC>r1,r2,itot: Partitore corrente
    - PT>r1,r2,vin: Partitore tensione
    - KRAMER>a,b,c,d,...: Risolutore 3x3 (12 parametri)
    - R1|R2: Parallelo di resistenze
    
    Args:
        expr: Lista di token dell'espressione
        variabili: Dizionario variabili disponibili
        
    Returns:
        Lista di token modificata, None se errore
    """
    i = 0
    lunghezza = len(expr)
    if lunghezza < 3:
        return None

    while i < lunghezza:
        token = expr[i]
        ris = None

        if token == '>' and i > 0 and expr[i-1] in NOMI_OPERATORI_SPECIALI:
            if i+1 < len(expr):
                valori = tokenizeVirgole(expr[i+1])
                valori = [val for val in valori if val != ","]
                if valori is None:
                    return None
                
                try:
                    if ciSonoVar(valori, variabili):
                        valori = convertiVariabili(valori, variabili)

                    if valori is None:
                        return None

                    match expr[i-1]:
                        case 'P':
                                if len(valori) != 2:
                                    print(Fore.RED + f"Errore: P> richiede 2 parametri (V, I), ricevuti {len(valori)}")
                                    return None
                                V = float(valori[0])
                                I = float(valori[1])
                                ris = potenza(V, I)
                        
                        case 'PC':
                                if len(valori) != 3:
                                    print(Fore.RED + f"Errore: PC> richiede 3 parametri (R1, R2, Itot), ricevuti {len(valori)}")
                                    return None
                                R1 = float(valori[0])
                                R2 = float(valori[1])
                                ITOT = float(valori[2])
                                ris = partitoreCorrente(R1, R2, ITOT)

                        case 'PT':
                                if len(valori) != 3:
                                    print(Fore.RED + f"Errore: PT> richiede 3 parametri (R1, R2, Vin), ricevuti {len(valori)}")
                                    return None
                                R1 = float(valori[0])
                                R2 = float(valori[1])
                                VIN = float(valori[2])
                                ris = partitoreTensione(R1, R2, VIN)

                        case 'KRAMER':
                                if len(valori) != Config.KRAMER_PARAMS:
                                    print(Fore.RED + f"Errore: KRAMER> richiede {Config.KRAMER_PARAMS} parametri (3 eq x 4 coeff), ricevuti {len(valori)}")
                                    return None
                                equazioni = [list(map(float, valori[j:j+4])) for j in range(0, Config.KRAMER_PARAMS, 4)]
                                result = Kramer3x3(equazioni)
                                if result is None:
                                    return None
                                x, y, z = result
                                variabili['x'] = x
                                variabili['y'] = y
                                variabili['z'] = z
                                return None  # Fine elaborazione dopo Kramer
                    
                    if ris is None:
                        return None
                    
                    expr[i] = str(ris)
                    expr.pop(i+1)
                    expr.pop(i-1)
                    lunghezza -= 2
                    i -= 1
                
                except (ValueError, IndexError) as e:
                    print(Fore.RED + f"Errore nel parsing dell'operatore speciale: {str(e)}")
                    return None
            else:
                return None

        elif token == '|' and i > 0 and i+1 < len(expr):
            try:
                if is_number(expr[i-1]) and is_number(expr[i+1]):
                    R1 = float(expr[i-1])
                    R2 = float(expr[i+1])
                    ris = parallelo([R1, R2])
                    
                    if ris is None:
                        return None
                    
                    expr[i] = str(ris)
                    expr.pop(i+1)
                    expr.pop(i-1)
                    lunghezza -= 2
                    i -= 1
                else:
                    return None
            except (ValueError, IndexError):
                return None
        
        i += 1

    return expr
            



def processaEspressione(expr : list[str], variabili : dict) -> float | None:
    """Processa un'espressione tokenizzata e ritorna il risultato.
    
    Gestisce:
    - Assegnamenti di variabili (x = 5)
    - Conversione variabili
    - Operatori speciali
    - Valutazione matematica sicura
    
    Args:
        expr: Lista di token
        variabili: Dizionario variabili (modificato in place per assegnamenti)
        
    Returns:
        Valore numerico calcolato, None se errore
        
    Raises:
        InvalidExpressionError: Se sintassi non corretta
    """
    if not expr:
        return None

    # caso in cui c'è assegnamento (x = 5)
    if len(expr) >= 3 and '=' in expr:
        nome_variabile = expr[0]

        if expr[1] != '=':
            print(Fore.RED + "Espressione non valida: formato assegnamento errato.")
            return None
    
        if not validaNomeVariabile(nome_variabile):
            print(Fore.RED + "Nome variabile non valido.")
            return None
        
        valore = processaEspressione(expr[2:], variabili)
        if valore is not None:
            variabili[nome_variabile] = valore
        return valore
    
    # caso in cui ci sono variabili
    if ciSonoVar(expr, variabili):
        try:
            expr = convertiVariabili(expr, variabili)
            if expr is None:
                print(Fore.RED + "Espressione non valida: variabile non definita.")
                return None
            return processaEspressione(expr, variabili)
        except InvalidVariableError as e:
            print(Fore.RED + str(e))
            return None
    
    elif ciSonoOperatoriSpeciali(expr):
        ris = gestisciOperatoreSpeciale(expr, variabili)
        if ris is None:
            return None
        ris = processaEspressione(ris, variabili)
        if ris is None:
            return None
        return ris
        
    # caso in cui è un espressione normale
    else:
        try:
            valore = safe_eval("".join([str(token) for token in expr]))
            if valore is not None and is_number(str(valore)):
                return valore
            else:
                print(Fore.RED + "Espressione non valida: formattazione scorretta o operazione non supportata.")
                return None
        except Exception as e:
            print(Fore.RED + f"Espressione non valida: {str(e)}")
            return None

def show(variabili : dict) -> None:
    if not variabili:
        print(Fore.YELLOW + "Nessuna variabile definita.")
    else:
        print(Fore.CYAN + "\n--- Variabili Definite ---")
        for k, v in variabili.items():
            print(Fore.CYAN + f"{k} = " + Fore.WHITE + f"{v}")
        print()
    input("Premi INVIO per continuare...")


def evaluateWithParentheses(expr : list[str], variabili : dict) -> float | None:
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
            ris = processaEspressione(sub_expr, variabili)
            if ris is not None:
                stack[-1] = ris  # Sostituisco '(' con il risultato
            else:
                print(Fore.RED + "Errore nella valutazione della sottospressione.")
                return None
        else:
            stack.append(token)

    return ris

def espressionLoop() -> None:
    variabili = dict()

    while True:
        clear()
        espressioniHeader()
        expr = input("espressione: ")
        if not expr:
            continue
        
        if expr == "exit":
            break

        if expr == "show":
            show(variabili)
            continue

        if expr == "KRAMER":
            inp = KramerInput(variabili)
            if inp is None:
                print(Fore.RED + "Errore nel parsing di variabili")
                input()
                continue
            ris = Kramer3x3(inp)
            if ris is not None:
                x, y, z = ris
                variabili['x'] = x
                variabili['y'] = y
                variabili['z'] = z
                print(Fore.GREEN + f"Soluzioni salvate: x={x}, y={y}, z={z}")
            continue

        if expr == "clear":
            variabili.clear()
            print(Fore.YELLOW + "Variabili cancellate.")
            input()
            continue

        if expr == "help":
            showHelp()
            continue

        # controllo se espressione in formato giusto
        try:
            expr = togliSpazi(expr)
            expr = tokenize(expr)
            expr = formatta(expr)
            validaParentesi(expr)
            
            # ciclo per parsing parentesi se presenti
            expr.insert(0, '(')
            expr.append(')')
            ris = evaluateWithParentheses(expr, variabili)

            if ris is not None:
                variabili['ris'] = ris
                print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            else:
                print(Fore.RED + "Espressione non valida.")
        
        except InvalidExpressionError as e:
            print(Fore.RED + f"Errore nell'espressione: {str(e)}")
        except Exception as e:
            print(Fore.RED + f"Errore inaspettato: {str(e)}")

        input()



