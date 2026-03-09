from src.espressioni import *
from src.utilities import *
from colorama import Fore, Style, init

def newFunction():
    nome = input(Fore.WHITE + "Nome funzione: ")
    if not validaNomeVariabile(nome):
        print(Fore.RED + "Nome non valido. Non può essere un numero, un operatore o una parola riservata.")
        return
    
    args = list(input("argomenti: ").split())
    for arg in args:
        if not validaNomeVariabile(arg):
            print(Fore.RED + f"Nome argomento '{arg}' non valido. Non può essere un numero, un operatore o una parola riservata.")
            return
    
    logic = input("logica (usa argomenti come variabili): ")
    return Function(nome, args, logic)

class Function():
    def __init__(self, nome : str, argomenti : list[str], logic : str):
        self.nome = nome
        self.argomenti = argomenti
        self.logic = logic

    