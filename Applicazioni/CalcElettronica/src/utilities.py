from colorama import Fore, Style, init
from src.config import *
from enum import Enum
import ast
import os

# ===== CUSTOM EXCEPTIONS =====
class InvalidExpressionError(Exception):
    """Eccezione per espressione non valida."""
    pass

class InvalidVariableError(Exception):
    """Eccezione per variabile non valida."""
    pass

class MatrixDimensionError(Exception):
    """Eccezione per dimensioni matrice non corrette."""
    pass


def togliSpazi(s : str) -> str:
    return s.replace(" ","")

def is_number(x) -> bool:
    try:
        float(x)
        return True
    except (ValueError, TypeError):
        return False

def validaParentesi(espressione : list[str]) -> bool:
    stack = []
    for pice in espressione:
        if pice == "(":
            stack.append(pice)
        elif pice == ")":
            if not stack or stack[-1] != "(":
                raise InvalidExpressionError("Parentesi non bilanciate: ')' senza '('")
            stack.pop()
    
    if stack:
        raise InvalidExpressionError("Parentesi non bilanciate: '(' senza ')'")
    
    return True

def tokenize(espressione : str) -> list[str]:
    """Trasforma una stringa in lista di token (numeri, variabili, operatori)
        
    Example:
        >>> tokenize("1+2*3")
        ['1', '+', '2', '*', '3']
        >>> tokenize("(a+b)")
        ['(', 'a', '+', 'b', ')']
    """
    tokens = []
    current_token = ""
    for char in espressione:
        if char in OPERATORI:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
        current_token = ""

    return tokens

def tokenizeVirgole(espressione : str) -> list[str]:
    """
    Example:
        >>> tokenizeVirgole("1,2,3")
        ['1', ',', '2', ',', '3']
    """
    tokens = []
    current_token = ""
    for char in espressione:
        if char in ",":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
        current_token = ""

    return tokens

def validaNomeVariabile(variabile : str) -> bool:
    if not variabile:
        return False
    
    if variabile in NOMI_NON_VALIDI:
        return False
    
    if variabile[0].isdigit():
        return False
    
    for char in variabile:
        if not (char.isalnum() or char == "_"):
            return False
    
    return True

def convertiVariabili(tokens : list[str], variabili : dict) -> list[str] | None:
    """Sostituisce i nomi delle variabili con i loro valori.
    
    Args:
        tokens: Lista di token da convertire
        variabili: Dizionario delle variabili disponibili
        
    Returns:
        Lista di token con variabili sostituite, None se errore
        
    Raises:
        InvalidVariableError: Se una variabile non è definita
    """
    new_tokens = []
    lunghezza = len(tokens)
    for i in range(lunghezza):
        token = tokens[i]
        if token in variabili:
            new_tokens.append(str(variabili[token]))
        elif token in OPERATORI or is_number(token) or ',' in token or token in NOMI_OPERATORI_SPECIALI:
            new_tokens.append(token)
        else:
            raise InvalidVariableError(f"Variabile non definita: '{token}'")
    
    return new_tokens

def formatta(tokens : list[str]) -> list[str]:
    """
    Example:
        >>> formatta(["-", "5", "+", "3"])
        ['(', '0', '-', '5', ')', '+', '3']
    """
    new_tokens = []
    lunghezza = len(tokens)
    i = 0
    while i < lunghezza:
        token = tokens[i]
        if token == '-' and (i == 0 or tokens[i-1] in OPERATORI or token == ','):
            new_tokens.append('(')
            new_tokens.append('0')
            new_tokens.append('-')
            new_tokens.append(tokens[i+1])
            new_tokens.append(')')
            i+=1
        else:
            new_tokens.append(token)
        i+=1
    
    return new_tokens


def ciSonoVar(expr : list[str], variabili : dict) -> bool:
    for token in expr:
        if token not in OPERATORI and not is_number(token) and token not in NOMI_OPERATORI_SPECIALI and ',' not in token:
            return True
    return False

def ciSonoOperatoriSpeciali(expr : list[str]) -> bool:
    return any(token in OPERATORI_SPECIALI for token in expr)

def KramerInput(variabili : dict) -> list[list[float]] | None:
    equazioni = [[0,0,0,0] for _ in range(3)]
    
    for i in range(3):
        try:
            riga = input(Fore.LIGHTBLUE_EX + f"equazione {i+1} (formato: x y z d): ").split()
            
            if len(riga) != 4:
                print(Fore.RED + f"Errore: inserire esattamente 4 valori (hai inserito {len(riga)})")
                return None
            
            # Parser personalizzato per variabili
            for j, addendo in enumerate(riga):
                if is_number(addendo):
                    equazioni[i][j] = float(addendo)
                elif (addendo[0] in ['-', '+']) and addendo[1:] in variabili:
                    valore = variabili[addendo[1:]]
                    equazioni[i][j] = -valore if addendo[0] == '-' else valore
                elif addendo in variabili:
                    equazioni[i][j] = variabili[addendo]
                else:
                    raise InvalidVariableError(f"Variabile non definita: '{addendo}'")
        
        except InvalidVariableError as e:
            print(Fore.RED + f"Errore nel parsing di variabili: {str(e)}")
            return None
        except (ValueError, IndexError) as e:
            print(Fore.RED + "Errore nel parsing dei coefficienti")
            return None
    
    return equazioni

def togliCommenti(s : str):
    return s.split(Config.CustomOperators.COMMENTO.value)[0].strip()

def salvaSessione(variabili : dict):
    nomeSessione = input(Fore.CYAN + "nome Sessione: ")
    if nomeSessione and validaNomeVariabile(nomeSessione):
        with open(f"{nomeSessione}.{Config.ESTENSIONE_SESSIONE}", "w") as f:
            for var, val in variabili.items():
                if val > 999999999999 or val < -999999999999:
                    print(Fore.YELLOW + f"Attenzione: la variabile '{var}' ha un valore troppo grande per essere salvato correttamente.")
                f.write(f"{var}={val}\n")
        print(Fore.GREEN + f"Sessione '{nomeSessione}' salvata con successo.")
    else:
        print(Fore.RED + "Nome sessione non valido")

def listSessioni(path = None):
    if path is None:
        path = os.getcwd()
    if os.path.exists(path):
        for file in os.listdir(path):
            if file.endswith(f".{Config.ESTENSIONE_SESSIONE}"):
                print(Fore.GREEN + file)

    else:
        print(Fore.RED + "Path non valido")
