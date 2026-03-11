from colorama import Fore, Style, init
from more_itertools import is_prime,factor
from src.Headers import *
from src.operatori import *
from src.utilities import *
from src.Funcs import *
from math import * 
import ast
import operator
import os

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
    """Gestisce operatori speciali e funzioni.
    Args:
        expr: Lista di token dell'espressione
        variabili: Dizionario variabili disponibili
        
    Returns:
        Lista di token modificata, None se errore
    """
    i = 0
    lunghezza = len(expr)

    while i < lunghezza:
        token = expr[i]
        ris = None

        if token == Config.CustomOperators.FUNZIONE.value and i > 0 and expr[i-1] in NOMI_OPERATORI_SPECIALI or expr[i-1] in FUNZIONI:
            if i+1 < len(expr):
                valori = tokenizeVirgole(expr[i+1])
                if valori is None:
                    return None
                
                # gestione operatori
                try:
                    if ciSonoVar(valori, variabili):
                        valori = convertiVariabili(valori, variabili)

                    if valori is None:
                        return None
                    
                     # gestione funzioni
                    if expr[i-1] in FUNZIONI:
                        logic, vars = FUNZIONI[expr[i-1]].processa(valori)
                        return controlloExpr(logic,vars)

                    match expr[i-1]:
                        case Config.SpecialOperators.POWER.value:
                                if len(valori) != 2:
                                    print(Fore.RED + f"Errore: P> richiede 2 parametri (V, I), ricevuti {len(valori)}")
                                    return None
                                V = float(valori[0])
                                I = float(valori[1])
                                ris = potenza(V, I)
                        
                        case Config.SpecialOperators.CURRENT_DIVIDER.value:
                                if len(valori) != 3:
                                    print(Fore.RED + f"Errore: PC> richiede 3 parametri (R1, R2, Itot), ricevuti {len(valori)}")
                                    return None
                                R1 = float(valori[0])
                                R2 = float(valori[1])
                                ITOT = float(valori[2])
                                ris = partitoreCorrente(R1, R2, ITOT)

                        case Config.SpecialOperators.VOLTAGE_DIVIDER.value:
                                if len(valori) != 3:
                                    print(Fore.RED + f"Errore: PT> richiede 3 parametri (R1, R2, Vin), ricevuti {len(valori)}")
                                    return None
                                R1 = float(valori[0])
                                R2 = float(valori[1])
                                VIN = float(valori[2])
                                ris = partitoreTensione(R1, R2, VIN)

                        case Config.SpecialOperators.PARALLELO.value:
                            if len(valori) < 1:
                                print(Fore.RED + f"Errore: PLL> richiede almeno 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = parallelo(list(map(float, valori)))

                        case Config.SpecialOperators.ABS.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: ABS> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = abs(float(valori[0]))

                        case Config.SpecialOperators.SQRT.value:
                            if len(valori) != 1 and len(valori) != 2:
                                print(Fore.RED + f"Errore: SQRT> richiede 1 o 2 parametri, ricevuti {len(valori)}")
                                return None
                            if len(valori) == 1:
                                ris = sqrt(float(valori[0]))
                            else:
                                ris = customSqrt(float(valori[0]),floor(float(valori[1])))
                        
                        case Config.SpecialOperators.LOG.value:
                            if len(valori) != 1 and len(valori) != 2:
                                print(Fore.RED + f"Errore: LOG> richiede 1 o 2 parametri, ricevuti {len(valori)}")
                                return None
                            if len(valori) == 1:
                                ris = log10(float(valori[0]))
                            else:
                                ris = log(float(valori[0]),floor(float(valori[1])))

                        case Config.SpecialOperators.LOG2.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: LOG2> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = log2(float(valori[0]))

                        case Config.SpecialOperators.SIN.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: SIN> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = sin(float(valori[0]))

                        case Config.SpecialOperators.COS.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: COS> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = cos(float(valori[0]))

                        case Config.SpecialOperators.TAN.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: TAN> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = tan(float(valori[0]))

                        case Config.SpecialOperators.ASIN.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: ASIN> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = asin(float(valori[0]))

                        case Config.SpecialOperators.ACOS.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: ACOS> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = acos(float(valori[0]))

                        case Config.SpecialOperators.ATAN.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: ATAN> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = atan(float(valori[0]))

                        case Config.SpecialOperators.DEG.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: DEG> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = degrees(float(valori[0]))

                        case Config.SpecialOperators.RAD.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: RAD> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = radians(float(valori[0]))

                        case Config.SpecialOperators.GCD.value:
                            if len(valori) != 2:
                                print(Fore.RED + f"Errore: GCD> richiede 2 parametro, ricevuti {len(valori)}")
                                return None
                            ris = gcd(floor(float(valori[0])),floor(float(valori[1])))

                        case Config.SpecialOperators.LCM.value:
                            if len(valori) != 2:
                                print(Fore.RED + f"Errore: LCM> richiede 2 parametro, ricevuti {len(valori)}")
                                return None
                            ris = lcm(floor(float(valori[0])),floor(float(valori[1])))

                        case Config.SpecialOperators.HYPOT.value:
                            if len(valori) != 2:
                                print(Fore.RED + f"Errore: HYPOT> richiede 2 parametro, ricevuti {len(valori)}")
                                return None
                            ris = hypot(float(valori[0]),float(valori[1]))

                        case Config.SpecialOperators.PRIMO.value:
                            if len(valori) != 1:
                                print(Fore.RED + f"Errore: PRIMO> richiede 1 parametro, ricevuti {len(valori)}")
                                return None
                            ris = is_prime(int(float(valori[0])))

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

        elif token == Config.CustomOperators.PARALLELO.value and i > 0 and i+1 < len(expr):
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
        
        elif token == Config.CustomOperators.FATTORIALE.value and i > 0:
            try:
                if is_number(expr[i-1]):
                    n = floor(float(expr[i-1]))
                    if n < 0:
                        print(Fore.RED + "Errore: fattoriale non definito per numeri negativi.")
                        return None
                    ris = factorial(n)
                    
                    if ris is None:
                        return None
                    
                    expr[i] = str(ris)
                    expr.pop(i-1)
                    lunghezza -= 1
                    i -= 1
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
    if isinstance(expr,float):
        return expr
        
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
                stack[-1] = str(ris)  # Sostituisco '(' con il risultato
            else:
                print(Fore.RED + "Errore nella valutazione della sottospressione.")
                return None
        else:
            stack.append(token)

    return ris

def controlloExpr(expr : str, variabili : dict):
    # controllo se espressione in formato giusto
    expr_debug = expr
    # caso in cui sia un define funzione
    if expr.startswith(Config.CustomFuncs.DEF.value):
        expr = expr.split(Config.FUNC_DEVIDER)
        if len(expr) != 4:
            print(Fore.RED + f"Errore hai passato {len(expr)} argomenti alla definizione di una funzione invece di 4.")
            return None
        
        nome = togliSpazi(expr[1])
        if not validaNomeVariabile(nome) and nome not in variabili:
            print(Fore.RED + f"ERRORE: {nome} nome non valido")
            return None
        
        args = []
        parametri = tokenizeVirgole(expr[2])
        for a in parametri:
            a = togliSpazi(a)
            if a in args:
                continue
            if validaNomeVariabile(a) and a != nome:
                args.append(a)
            else:
                print(Fore.RED + f"Errore: {a} non valido come nome parametro funzione")
                return None
        logica = togliSpazi(expr[3])
        f = Function(nome,args,logica)
        FUNZIONI[f.nome] = f 
        return None

    try:
        expr = tokenize(expr)
        expr = formatta(expr)
        validaParentesi(expr)
        
        # ciclo per parsing parentesi se presenti
        expr.insert(0, '(')
        expr.append(')')
        ris = evaluateWithParentheses(expr, variabili)

        if ris is not None:
            variabili[Config.RIS_PRECEDENTE] = ris
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            return ris
        else:
            print(Fore.RED + f"ERRORE in espressione: {expr_debug}")
            print(Fore.RED + "Espressione non valida.")
            input("premi per continuare...")
    
    except InvalidExpressionError as e:
        print(Fore.RED + f"ERRORE in espressione: {expr_debug}")
        print(Fore.RED + f"Errore nell'espressione: {str(e)}")
        input("premi per continuare...")
    except Exception as e:
        print(Fore.RED + f"ERRORE in espressione: {expr_debug}")
        print(Fore.RED + f"Errore inaspettato: {str(e)}")
        input("premi per continuare...")


def processaFile(file : str, variabili : dict):
    if not os.path.isfile(file):
        return None
    
    with open(file,"r") as f:
        testo = f.readlines()
        for riga in testo:
            riga = riga.replace("\n","")
            riga = togliSpazi(riga)
            riga = togliCommenti(riga)
            if riga:
                controlloExpr(riga,variabili)
           

def espressionLoop() -> None:
    variabili = dict()
    # costnati 
    variabili[Config.PI] = pi
    FUNZIONI.clear()

    while True:
        clear()
        espressioniHeader()
        expr = input("espressione: ")
        expr = togliSpazi(expr)
        if not expr:
            continue
        
        elif expr == Config.CustomFuncs.ESCI.value:
            break

        elif expr == Config.CustomFuncs.SHOW.value:
            show(variabili)
            continue
        
        elif expr == Config.CustomFuncs.PWD.value:
            os.system("pwd")
            input()
            continue

        elif expr == Config.CustomFuncs.SALVA.value:
            salvaSessione(variabili)
            input()
            continue

        elif expr == Config.CustomFuncs.LIST.value:
            path = input(Fore.CYAN + "Path sessioni: ")
            path = togliSpazi(path)
            if path:
                listSessioni(path)
            else:
                listSessioni()
            input()
            continue

        elif expr == Config.CustomFuncs.KRAMER.value:
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

        elif expr == Config.CustomFuncs.DEF.value:
            f = newFunction(variabili)
            if f is not None:
                FUNZIONI[f.nome] = f
            input("Premi per continuare...")
            continue

        elif expr == Config.CustomFuncs.SHOW_FUNCTIONS.value:
            showFuncs(FUNZIONI)
            continue

        elif expr == Config.CustomFuncs.PULISCI.value:
            variabili.clear()
            print(Fore.YELLOW + "Variabili cancellate.")
            input()
            continue

        elif expr == Config.CustomFuncs.HELP.value:
            helpLoop()
            continue

        elif expr == Config.CustomFuncs.LEGGI.value:
            file = input(Fore.CYAN + "Path File: ")
            processaFile(file,variabili)
            continue

        elif expr == Config.CustomFuncs.LEN.value:
            stringa = input("Stringa: ")
            ris = len(stringa)
            variabili[Config.RIS_PRECEDENTE] = ris
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            input()
            continue

        elif expr == Config.CustomFuncs.FATTORI.value:
            try:
                n = input("numero: ")
                n = processaEspressione(tokenize(n), variabili)
                n = floor(n)
            except Exception as e:
                print(Fore.RED + f"Numero non inserito: {str(e)}")
                input()
                continue
            ris = list(factor(n))
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            input()
            continue

        elif expr == Config.CustomFuncs.DIVISORI.value:
            try:
                n = input("numero: ")
                n = processaEspressione(tokenize(n), variabili)
                n = floor(n)
            except Exception as e:
                print(Fore.RED + f"Numero non inserito: {str(e)}")
                input()
                continue
            ris = divisori(n)
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            input()
            continue

        elif expr == Config.CustomFuncs.COMBINAZIONI.value:
            try:
                n = input("elementi totali: ")
                n = processaEspressione(tokenize(n), variabili)
                n = floor(n)
                y = input("numero elementi da scegliere: ")
                y = processaEspressione(tokenize(y), variabili)
                y = floor(y)
            except Exception as e:
                print(Fore.RED + f"Numero non inserito: {str(e)}")
                input()
                continue
            ris = nCr(n,y)
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            input()
            continue

        elif expr == Config.CustomFuncs.PERMUTAZIONI.value:
            try:
                n = input("elementi totali: ")
                n = processaEspressione(tokenize(n), variabili)
                n = floor(n)
                y = input("numero elementi da scegliere: ")
                y = processaEspressione(tokenize(y), variabili)
                y = floor(y)
            except Exception as e:
                print(Fore.RED + f"Numero non inserito: {str(e)}")
                input()
                continue
            ris = nPr(n,y)
            print(Fore.GREEN + "Risultato: " + Fore.WHITE + str(ris))
            input()
            continue

        controlloExpr(expr,variabili)

        input()



