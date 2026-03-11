from colorama import Fore, Style, init
from src.Headers import *
from src.operatori import *
from src.espressioni import espressionLoop
from src.boleanParser import *

init(autoreset=True)
 
def main():
    while True:
        clear()
        menu()
        scelta = input(Fore.WHITE + "Opzione: ")
        if(scelta.isdigit()):
            scelta = int(scelta)
        else:
            continue

        match scelta:
            case 1:
                espressionLoop()
                
            case 2:
                Kramer3x3(None)

            case 3:
                boolLoop()

            case 4:
                helpLoop()

            case 5:
                break


if __name__ == "__main__":
    main()  