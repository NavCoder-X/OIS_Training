from colorama import Fore, Style, init
from Headers import *
from operatori import *
from espressioni import *

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
                break


if __name__ == "__main__":
    main()  