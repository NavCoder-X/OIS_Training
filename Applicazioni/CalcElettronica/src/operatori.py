from math import factorial

from colorama import Fore, Style, init
from src.Headers import *
from src.utilities import *

def Kramer3x3(equazioni = None):
    # input in formato matrice 3x3
    if equazioni is None:
        clear()
        kramerHeader()
        equazioni = [[0,0,0,0] for _ in range(3)]
        for i in range(3):
            riga = input(Fore.LIGHTBLUE_EX + f"equazione {i+1} (formato: x y z d): ")
            equazioni[i] = list(map(float, riga.split()))

    if(any(len(riga) != 4 for riga in equazioni)):
        print(Fore.RED + "inserire 4 valori ciascuna equazione.")
        input()
        return
    
    # calcolo del determinante
    D = (equazioni[0][0] * (equazioni[1][1] * equazioni[2][2] - equazioni[1][2] * equazioni[2][1]) -
            equazioni[0][1] * (equazioni[1][0] * equazioni[2][2] - equazioni[1][2] * equazioni[2][0]) +
            equazioni[0][2] * (equazioni[1][0] * equazioni[2][1] - equazioni[1][1] * equazioni[2][0]))
    
    # calcolo dei determinanti per x, y, z
    Dx = (equazioni[0][3] * (equazioni[1][1] * equazioni[2][2] - equazioni[1][2] * equazioni[2][1]) -
            equazioni[0][1] * (equazioni[1][3] * equazioni[2][2] - equazioni[1][2] * equazioni[2][3]) +
            equazioni[0][2] * (equazioni[1][3] * equazioni[2][1] - equazioni[1][1] * equazioni[2][3]))
    
    Dy = (equazioni[0][0] * (equazioni[1][3] * equazioni[2][2] - equazioni[1][2] * equazioni[2][3]) -
            equazioni[0][3] * (equazioni[1][0] * equazioni[2][2] - equazioni[1][2] * equazioni[2][0]) +
            equazioni[0][2] * (equazioni[1][0] * equazioni[2][3] - equazioni[1][3] * equazioni[2][0]))
    
    Dz = (equazioni[0][0] * (equazioni[1][1] * equazioni[2][3] - equazioni[1][3] * equazioni[2][1]) -
            equazioni[0][1] * (equazioni[1][0] * equazioni[2][3] - equazioni[1][3] * equazioni[2][0]) +
            equazioni[0][3] * (equazioni[1][0] * equazioni[2][1] - equazioni[1][1] * equazioni[2][0]))
        
    if D == 0:
        if(Dx == 0 and Dy == 0 and Dz == 0):
            print(Fore.YELLOW + "Il sistema ha infinite soluzioni.")
        else:
            print(Fore.RED + "Il sistema non ha soluzioni.")
        input()
        return
    
    # calcolo delle soluzioni
    x = Dx / D
    y = Dy / D
    z = Dz / D
    print(Fore.GREEN + f"Soluzione: x = {x}, y = {y}, z = {z}") 
    input()
    return (x,y,z)

def __parallelo(a : float, b : float):
    if(a == 0 and b == 0):
        print(Fore.RED + "Errore: Divisione per zero.")
        return
    
    return a*b / (a+b)

def parallelo(resistenze : list[float]):
    if(len(resistenze) <= 1):
        print(Fore.RED + "Errore servono almeno 2 resistenze.")
        return
    
    ris = __parallelo(resistenze[0],resistenze[1])
    for i in range(1,len(resistenze)-1):
        ris = __parallelo(ris, resistenze[i])
    
    return ris

def partitoreTensione(R1 : float, R2 : float, Vin : float):
    if(R1 + R2 == 0):
        print(Fore.RED + "Errore: Divisione per zero.")
        return
    
    return Vin * R1 / (R2 + R1)

def partitoreCorrente(R1 : float, R2 : float, Iin : float):
    if(R1 + R2 == 0):
        print(Fore.RED + "Errore: Divisione per zero.")
        return
    
    return Iin * R1 / (R1 + R2)

def potenza(V : float, I : float):
    return V * I

def customSqrt(x : float, n : int):
    if x < 0:
        print(Fore.RED + "Errore: Impossibile calcolare la radice di un numero negativo.")
        return None
    if n <= 0:
        print(Fore.RED + "Errore: L'indice della radice deve essere un intero positivo.")
        return None
    l = 0
    r = x
    esp = 10**(-11)
    while r-l > esp:
        mid = (l+r)/2
        mifìd_pow = mid**n
        if mifìd_pow < x:
            l = mid
        else:
            r = mid

    return l

def divisori(n : int):
    n = abs(n)
    if n == 1:
        return [1]
    
    deviders = []
    for i in range(1,n//2 + 1):
        if n % i == 0:
            deviders.append(i)
    if n != 1 and n != 0:
        deviders.append(n)
    return deviders

def nCr(n : int, r : int):
    if n < 0 or r < 0 or r > n:
        print(Fore.RED + "Errore: n e r devono essere non negativi e r deve essere minore o uguale a n.")
        return None
    return factorial(n) // (factorial(r) * factorial(n-r))

def nPr(n : int, r : int):
    if n < 0 or r < 0 or r > n:
        print(Fore.RED + "Errore: n e r devono essere non negativi e r deve essere minore o uguale a n.")
        return None
    return factorial(n) // factorial(n-r)
