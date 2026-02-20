from copy import deepcopy
from time import sleep

# scacchiera 
empty = 0
regina = 1
N = 5
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
            if scacchiera[i][j] == regina:
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
    k = 0
    for k in range(len(scacchiera)):
        if(scacchiera[k][j] == regina and i != k):
            return True
        
    # controllo sotto la diagonale principale
    k,l = i,j
    while(l >= 0 and k < len(scacchiera)):
        if(scacchiera[k][l] == regina and (k != i or l != j)):
            return True
        k+=1
        l-=1
        
    # controllo sopra la diagonale principale
    k,l = i,j
    while(k >= 0 and l < len(scacchiera)):
        if(scacchiera[k][l] == regina and (k != i or l != j)):
            return True
        k-=1
        l+=1
        
    # controllo sopra la diagonale secondaria
    k,l = i,j
    while(k >= 0 and l >= 0):
        if(scacchiera[k][l] == regina and (k != i or l != j)):
            return True
        k-=1
        l-=1
    
    # controllo sotto la diagonale secondaria
    k,l = i,j
    while(k < len(scacchiera) and l < len(scacchiera)):
        if(scacchiera[k][l] == regina and (k != i or l != j)):
            return True
        l+=1
        k+=1


    return False

soluzioni = []
def poszioneRegina(scacchiera, n, punto_massimo = len(scacchiera)):
    printScacchiera(scacchiera)
    input()
    # sleep(0.1)
    print("\033[H\033[J", end="")
    
    if(n == punto_massimo):
        soluzioni.append(deepcopy(scacchiera))
        return
    
    for j in range(len(scacchiera)):
        if(not isSottoAtacco(scacchiera,n,j)):
            scacchiera[n][j] = regina
            poszioneRegina(scacchiera,n+1,punto_massimo)
            scacchiera[n][j] = empty

    return

def posizioneRegineN(scacchiera, n):
    # funzione per posizionare meno di len(scacchiera regine)
    if(n == 0):
        soluzioni.append(deepcopy(scacchiera))
        return
    
    if(n > len(scacchiera)):
        print("Errore: n deve essere minore o uguale alla dimensione della scacchiera.")
        return
    
    for i in range(len(scacchiera)-n+1):
        poszioneRegina(scacchiera,i,i+n)

posizioneRegineN(scacchiera, 4)
print(f"Soluzioni trovate: {len(soluzioni)}")
for soluzione in soluzioni:
    printScacchiera(soluzione)
