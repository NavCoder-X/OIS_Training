from colorama import Fore, Style, init

init(autoreset=True)

def clear() -> None:
    print("\033[H\033[J", end="")

def titolo() -> None:
    print(
Fore.BLUE + Style.BRIGHT + r"""
  ______     ___       __        ______     _______  __       _______ .___________.___________..______        ______   .__   __.  __    ______     ___      
 /      |   /   \     |  |      /      |   |   ____||  |     |   ____||           |           ||   _  \      /  __  \  |  \ |  | |  |  /      |   /   \     
|  ,----'  /  ^  \    |  |     |  ,----'   |  |__   |  |     |  |__   `---|  |----`---|  |----`|  |_)  |    |  |  |  | |   \|  | |  | |  ,----'  /  ^  \    
|  |      /  /_\  \   |  |     |  |        |   __|  |  |     |   __|      |  |        |  |     |      /     |  |  |  | |  . `  | |  | |  |      /  /_\  \   
|  `----./  _____  \  |  `----.|  `----.   |  |____ |  `----.|  |____     |  |        |  |     |  |\  \----.|  `--'  | |  |\   | |  | |  `----./  _____  \  
 \______/__/     \__\ |_______| \______|   |_______||_______||_______|    |__|        |__|     | _| `._____| \______/  |__| \__| |__|  \______/__/     \__\ 
                                                                                                                                                              
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
    print(Fore.GREEN + "3. Esci")


def showHelp() -> None:
    clear()
    espressioniHeader()
    print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════╗
║         GUIDA CALCOLATRICE ELETTRONICA AVANZATA            ║
╚════════════════════════════════════════════════════════════╝

📝 COMANDI SPECIALI:
  • show              - Mostra tutte le variabili definite
  • clear             - Cancella tutte le variabili
  • exit              - Esce dalla calcolatrice
  • help              - Mostra questa guida
  • KRAMER            - Risolvi sistema 3x3 lineare
  • ris               - Accedi al risultato precedente

🔢 OPERAZIONI MATEMATICHE:
  • +  Addizione
  • -  Sottrazione (unario e binario)
  • *  Moltiplicazione
  • /  Divisione
  • ^  Elevamento a potenza

⚡ OPERATORI SPECIALI PER CIRCUITI:
  
  1. POTENZA: P>V,I
     Calcola P = V × I
     Esempio: P>10,2
     Risultato: 20.0 Watt
  
  2. PARALLELO: R1|R2
     Calcola resistenza equivalente in parallelo
     Esempio: 10|20
     Risultato: 6.67 Ohm
  
  3. PARTITORE TENSIONE: PT>R1,R2,Vin
     V_out = Vin × R1 / (R1 + R2)
     Esempio: PT>100,100,10
     Risultato: 5.0 Volt
  
  4. PARTITORE CORRENTE: PC>R1,R2,Iin
     I_out = Iin × R1 / (R1 + R2)
     Esempio: PC>100,100,10
     Risultato: 5.0 Ampere

  5. METODO DI KRAMER: KRAMER>a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3
     Risolve: a1×x + b1×y + c1×z = d1
              a2×x + b2×y + c2×z = d2
              a3×x + b3×y + c3×z = d3
     Esempio: KRAMER>1,0,0,5,0,1,0,10,0,0,1,15
     Risultato: x=5, y=10, z=15

💾 VARIABILI:
  • Assegna: x = 5
  • Riusa:   2 * x + 3
  • Supporta: +/- prima della variabile (es: -x)

📌 ESEMPI DI USO:
  
  Espressione semplice:
    > 2 + 3 * 4
    Risultato: 14.0
  
  Con variabili:
    > r1 = 100
    > r2 = 50
    > r1 | r2
    Risultato: 33.33 Ohm
  
  Operatore speciale:
    > v = 12
    > i = 2
    > P>v,i
    Risultato: 24.0 Watt
  
  Parentesi:
    > (2 + 3) * (10 - 6)
    Risultato: 20.0

⚠️  NOTE IMPORTANTI:
  • I nomi variabili devono iniziare con lettera o underscore
  • Solo nomi validi: P, PC, PT, KRAMER, ris sono riservati
  • Gli spazi vengono ignorati
  • Le parentesi devono essere bilanciate
  • Il risultato precedente è sempre accessibile come 'ris'
""")
    input("Premi INVIO per tornare al menu...")