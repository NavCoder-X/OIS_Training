from copy import deepcopy
from time import sleep

# scacchiera 
EMPTY = 0
REGINA = 1
N = 15
scacchiera = []
for i in range(N):
    scacchiera.append([0]*N)

def printScacchiera(scacchiera):
    n = len(scacchiera)
    
    # Stampa bordo superiore
    print("┌" + "────┬" * (n - 1) + "────┐")
    
    for i in range(n):
        # Stampa riga con le regine
        for j in range(n):
            if scacchiera[i][j] == REGINA:
                print(f"│ ♛  ", end="")
            else:
                print(f"│    ", end="")
        print("│")
        
        # Stampa separatore tra righe
        if i < n - 1:
            print("├" + "────┼" * (n - 1) + "────┤")
        else:
            print("└" + "────┴" * (n - 1) + "────┘")
    print()

# verifica che una regina non sia ataccata
def isSottoAtacco(scacchiera, i, j):
    # non controllo la riga , sono sicuro che non ci sia nessuna regina la
    # controllo la colonna
    for k in range(len(scacchiera)):
        if scacchiera[k][j] == REGINA and i != k:
            return True
        

    da_controllare = (
        list(zip(range(i + 1, len(scacchiera)), range(j + 1, len(scacchiera)))) + # sotto la principale
        list(zip(range(i - 1, -1, -1), range(j - 1, -1, -1))) + # sopra la principale
        list(zip(range(i + 1, len(scacchiera)), range(j - 1, -1, -1))) + # sotto la secondaria
        list(zip(range(i - 1, -1, -1), range(j + 1, len(scacchiera))))) # sopra la secondaria
    
    # print(da_controllare)
        
    for k, l in da_controllare:
        if scacchiera[k][l] == REGINA:
            return True


    return False

soluzioni = []
def poszioneRegina(scacchiera, n, punto_massimo = len(scacchiera)):
    print("\033[H\033[J", end="")
    printScacchiera(scacchiera)
    input()
    # sleep(0.1)
    
    if n == punto_massimo:
        soluzioni.append(deepcopy(scacchiera))
        return
    
    for j in range(len(scacchiera)):
        if not isSottoAtacco(scacchiera,n,j):
            scacchiera[n][j] = REGINA
            poszioneRegina(scacchiera,n+1,punto_massimo)
            scacchiera[n][j] = EMPTY

    return

def posizioneRegineN(scacchiera, n):
    # funzione per posizionare meno di len(scacchiera regine)
    if n == 0:
        soluzioni.append(deepcopy(scacchiera))
        return
    
    if n > len(scacchiera) :
        print("Errore: n deve essere minore o uguale alla dimensione della scacchiera.")
        return
    
    for i in range(len(scacchiera)-n+1):
        poszioneRegina(scacchiera,i,i+n)


posizioneRegineN(scacchiera, N)
for soluzione in soluzioni:
    printScacchiera(soluzione)
print(f"Soluzioni trovate: {len(soluzioni)}")
