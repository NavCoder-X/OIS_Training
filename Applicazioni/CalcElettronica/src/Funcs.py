from src.utilities import *
from src.config import *
from colorama import Fore, Style, init

def newFunction(variabili : dict):
    nome = input(Fore.WHITE + "Nome funzione: ")
    nome = togliSpazi(nome)
    if not validaNomeVariabile(nome) and nome not in variabili:
        print(Fore.RED + "Nome non valido. Non può essere un numero, un operatore o una parola riservata.")
        return
    
    args = list(input("argomenti: ").split())
    new_args = []
    for arg in args:
        arg = togliSpazi(arg)
        if arg in new_args:
            continue
        if not validaNomeVariabile(arg) and arg != nome:
            print(Fore.RED + f"Nome argomento '{arg}' non valido. Non può essere un numero, un operatore o una parola riservata.")
            return
        new_args.append(arg)
    
    logic = input("logica (usa argomenti come variabili): ")
    logic = togliSpazi(logic)
    return Function(nome, new_args, logic)

class Function():
    def __init__(self, nome : str, argomenti : list[str], logic : str):
        self.nome = nome
        self.argomenti = argomenti # nomi
        self.nArgs = len(argomenti)
        self.Args = {f : None for f in argomenti}
        self.logic = logic

    def processa(self, vars : list[str]):
        if self.nArgs != len(vars):
            print(Fore.RED + f"Erorre numero di argomenti previsti {self.nArgs}, numero di argomenti ricevuti {len(vars)}")
            return None

        try:
            i = 0
            for par in self.argomenti:
                self.Args[par] = vars[i]
                i+=1
            return self.logic,self.Args
        except Exception as e:
            print(Fore.RED + f"Errore: {e}")
            return None
        
    def __str__(self):
        definitore = Config.CustomFuncs.DEF.value
        separatore = Config.FUNC_DEVIDER

        s = f"{definitore} {separatore} "
        s += self.nome
        s += separatore + " "

        for par in self.argomenti:
            s += par + ","
        
        s += f" {separatore} {self.logic}"
        return s

def showFuncs(funzioni : dict):
    for f in funzioni.values():
        print(Fore.CYAN + f"{f.nome} : " + Fore.WHITE + f"{f.argomenti} | {f.logic}")
    input()
        



        
