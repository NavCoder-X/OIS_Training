from colorama import Fore, Style, init
from src.config import Config
import os

init(autoreset=True)

# sito ASCI art: https://patorjk.com/software/taag/#p=display&f=ANSI+Regular&t=HElp&x=none&v=4&h=4&w=80&we=false

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def titolo() -> None:
    print(
Fore.BLUE + Style.BRIGHT + r"""
 ██████  █████  ██       ██████  ██████  ██       █████  ████████ ██████  ██  ██████ ███████ 
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██   ██ ██ ██      ██      
██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██████  ██ ██      █████   
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██   ██ ██ ██      ██      
 ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██    ██   ██ ██  ██████ ███████ 
                                                                                             
""")
        
def kramerHeader() -> None:
    print(
Fore.MAGENTA + Style.BRIGHT + r"""
                                           
▄▄▄   ▄▄▄                                  
███ ▄███▀                                  
███████   ████▄  ▀▀█▄ ███▄███▄ ▄█▀█▄ ████▄ 
███▀███▄  ██ ▀▀ ▄█▀██ ██ ██ ██ ██▄█▀ ██ ▀▀ 
███  ▀███ ██    ▀█▄██ ██ ██ ██ ▀█▄▄▄ ██    
                                           
""")
    
def espressioniHeader() -> None:
    print(
Fore.YELLOW + Style.BRIGHT + r"""
  _____                             _             _ 
 | ____|___ _ __  _ __ ___  ___ ___(_) ___  _ __ (_)
 |  _| / __| '_ \| '__/ _ \/ __/ __| |/ _ \| '_ \| |
 | |___\__ \ |_) | | |  __/\__ \__ \ | (_) | | | | |
 |_____|___/ .__/|_|  \___||___/___/_|\___/|_| |_|_|
           |_|
""")
    
def menu() -> None:
    titolo()
    print(Fore.GREEN + "1. Espressioni")
    print(Fore.GREEN + "2. Kramer 3x3")
    print(Fore.GREEN + "3. Aiuto")
    print(Fore.GREEN + "4. Esci")

def helpHeader():
    print(
Fore.YELLOW + Style.BRIGHT + r"""
██   ██ ███████ ██      ██████  
██   ██ ██      ██      ██   ██ 
███████ █████   ██      ██████  
██   ██ ██      ██      ██      
██   ██ ███████ ███████ ██      
                                
""")
    
p = Config.SpecialOperators.POWER.value
pt = Config.SpecialOperators.VOLTAGE_DIVIDER.value
pc = Config.SpecialOperators.CURRENT_DIVIDER.value
pll = Config.SpecialOperators.PARALLELO.value
sqrt = Config.SpecialOperators.SQRT.value
abs_op = Config.SpecialOperators.ABS.value
log_op = Config.SpecialOperators.LOG.value
log2 = Config.SpecialOperators.LOG2.value
sin_op = Config.SpecialOperators.SIN.value
cos_op = Config.SpecialOperators.COS.value
tan_op = Config.SpecialOperators.TAN.value
asin = Config.SpecialOperators.ASIN.value
acos = Config.SpecialOperators.ACOS.value
atan = Config.SpecialOperators.ATAN.value
deg = Config.SpecialOperators.DEG.value
rad = Config.SpecialOperators.RAD.value
gcd_op = Config.SpecialOperators.GCD.value
lcm = Config.SpecialOperators.LCM.value
hypot = Config.SpecialOperators.HYPOT.value
primo = Config.SpecialOperators.PRIMO.value

exit_cmd = Config.CustomFuncs.ESCI.value
show_cmd = Config.CustomFuncs.SHOW.value
clear_cmd = Config.CustomFuncs.PULISCI.value
read_cmd = Config.CustomFuncs.LEGGI.value
kramer_cmd = Config.CustomFuncs.KRAMER.value
factors_cmd = Config.CustomFuncs.FATTORI.value
divisori_cmd = Config.CustomFuncs.DIVISORI.value
help_cmd = Config.CustomFuncs.HELP.value
combinazioni_cmd = Config.CustomFuncs.COMBINAZIONI.value
permutazioni_cmd = Config.CustomFuncs.PERMUTAZIONI.value
pwd_cmd = Config.CustomFuncs.PWD.value
save_cmd = Config.CustomFuncs.SALVA.value
list_cmd = Config.CustomFuncs.LIST.value

par_op = Config.CustomOperators.PARALLELO.value
fun_op = Config.CustomOperators.FUNZIONE.value
fat_op = Config.CustomOperators.FATTORIALE.value
commento_op = Config.CustomOperators.COMMENTO.value

ris_precedente = Config.RIS_PRECEDENTE
    
def helpEspressioni():
    print(Fore.CYAN + "\n=== GUIDA ESPRESSIONI ===")
    print(Fore.WHITE + f"""
OPERAZIONI BASE:
  • + addizione
  • - sottrazione
  • * moltiplicazione
  • / divisione
  • ^ potenza (es: 2^3 = 8)
  • ( ) parentesi

FUNZIONI SPECIALI (sintassi: NOME{fun_op}parametri):
  • {p}{fun_op}(V,I)              → Potenza (V*I)
  • {pt}{fun_op}(R1,R2,Vin)       → Partitore tensione su R1
  • {pc}{fun_op}(R1,R2,Itot)      → Partitore corrente, corrente in R2
  • {pll}{fun_op}(R1,R2,...)      → Resistenze parallelo
  • {sqrt}{fun_op}(x) o {sqrt}{fun_op}(x,n)→ Radice (n-esima)
  • {abs_op}{fun_op}(x)              → Valore assoluto
  • {log_op}{fun_op}(x) o {log_op}{fun_op}(x,b)  → Logaritmo (base b)
  • {log2}{fun_op}(x)             → Logaritmo base 2
  • {sin_op}{fun_op}(x), {cos_op}{fun_op}(x), {tan_op}{fun_op}(x) → Trigonometria
  • {asin}{fun_op}(x), {acos}{fun_op}(x), {atan}{fun_op}(x) → Inversi
  • {deg}{fun_op}(x)              → Radianti → Gradi
  • {rad}{fun_op}(x)              → Gradi → Radianti
  • {gcd_op}{fun_op}(a,b)            → Massimo comun divisore
  • {lcm}{fun_op}(a,b)            → Minimo comune multiplo
  • {hypot}{fun_op}(a,b)          → Ipotenusa
  • {primo}{fun_op}(x)            → Verifica se primo (1=sì, 0=no)
  • x{fat_op}                   → Fattoriale
  • x{par_op}y                   → Parallelo (per resistenze)


COMANDI:
  • {exit_cmd}          → Torna al menu
  • {show_cmd}          → Mostra variabili definite
  • {clear_cmd}         → Cancella variabili
  • {read_cmd}          → Leggi da file
  • {kramer_cmd}        → Risolvi sistema 3x3
  • {factors_cmd} x     → Fattori primi di x (int)
  • {divisori_cmd} x    → Divisori di x (int)
  • {combinazioni_cmd} n,k → Combinazioni C(n,k)
  • {permutazioni_cmd} n,k → Permutazioni P(n,k)

VARIABILI:
  • Puoi definire variabili: (x = 5)-(y = 10)
  • Poi usarle: x + y
  • il risulatato precedente si trova sempre nella variabile {ris_precedente}
  • {ris_precedente} non viene sovrascritto dai Comandi
  • viene risolto prima tutto cio che ce a destra del uaguale mntre per le espressioni viene valutato tutto da sinistra verso destra

""")
    print(Fore.YELLOW + "Premi ENTER per continuare...")
    input()

def helpKramer3x3():
    print(Fore.CYAN + "\n=== GUIDA KRAMER 3x3 ===")
    print(Fore.WHITE + """
Risolve sistemi lineari 3x3 usando il metodo di Cramer.

FORMATO:
  a₁x + b₁y + c₁z = d₁
  a₂x + b₂y + c₂z = d₂
  a₃x + b₃y + c₃z = d₃

ESEMPIO:
  2x + y - z = 8
  -3x - y + 2z = -11
  -2x + y + 2z = -3

ALL'INSERIMENTO:
  Digita 4 numeri separati da spazio per ogni equazione:
  equazione 1: 2 1 -1 8
  equazione 2: -3 -1 2 -11
  equazione 3: -2 1 2 -3

  Risposta: x = 2.0, y = 3.0, z = -1.0

NOTE:
  • Sovrascrive le variabili x, y, z coi risultati
  • Se il determinante = 0, il sistema ha infinite soluzioni
  • Se det=0 e i determinanti speciali ≠ 0, nessuna soluzione
""")
    print(Fore.YELLOW + "Premi ENTER per continuare...")
    input()

def helpComandi():
    print(Fore.CYAN + "\n=== COMANDI SPECIALI ===")
    print(Fore.WHITE + f"""
COMANDI DURANTE L'INSERIMENTO:
  • {exit_cmd}           → Ritorna al menu precedente
  • {help_cmd}           → Mostra questo aiuto
  • {show_cmd}           → Mostra variabili definite
  • {clear_cmd}          → Cancella tutte le variabili salvate
  • {kramer_cmd}         → Risolvi un sistema 3x3

COMANDI DI SESSIONE:
  • {pwd_cmd}            → Mostra directory corrente
  • {save_cmd}           → Salva la sessione su file
  • {list_cmd}           → Elenca tutte le sessioni salvate
  
SUGGERIMENTI:
  • Puoi definire variabili in qualsiasi momento
  • Le variabili rimangono salvate fino a {clear_cmd}
  • Usa parentesi per chiarire l'ordine delle operazioni
  • I parametri delle funzioni sono separati da virgola
""")
    print(Fore.YELLOW + "Premi ENTER per continuare...")
    input()

def helpFileLettura():
    print(Fore.CYAN + "\n=== LETTURA FILE (input.txt) ===")
    print(Fore.WHITE + f"""
Il programma legge espressioni da input.txt e carica i dati

FORMATO SUPPORTATO:
  • Una espressione per riga
  • Linee vuote vengono ignorate
  • Linee che iniziano con {commento_op} sono commenti

ESEMPIO DI input.txt:
  {commento_op} Calcoli di prova
  2 + 3 * 4
  (10 + 5) / 3
  {p}{fun_op}(12,2)
  
  {sqrt}{fun_op}(16)
  x = 5
  x * 2

NOTE:
  • Le variabili definite in un'espressione persistono alle seguenti
  • Non puoi usare Comandi speciali (es: {help_cmd}, {show_cmd}) all'interno di input.txt
""")
    print(Fore.YELLOW + "Premi ENTER per continuare...")
    input()

def helpLoop():
    while True:
        clear()
        helpHeader()
        print(Fore.CYAN + "Sezioni disponibili:")
        print(Fore.GREEN + "1. Espressioni")
        print(Fore.GREEN + "2. Kramer 3x3")
        print(Fore.GREEN + "3. Comandi speciali")
        print(Fore.GREEN + "4. Lettura file")
        print(Fore.GREEN + "5. Torna al menu principale")
        scelta = input(Fore.WHITE + "Quale sezione vuoi vedere: ")
        
        if scelta.isdigit():
            scelta = int(scelta)
        else:
            continue
        
        match scelta:
            case 1:
                clear()
                helpEspressioni()
            case 2:
                clear()
                helpKramer3x3()
            case 3:
                clear()
                helpComandi()
            case 4:
                clear()
                helpFileLettura()
            case 5:
                break
            case _:
                print(Fore.RED + "Opzione non valida!")
                input(Fore.YELLOW + "Premi ENTER per continuare...")
        
    