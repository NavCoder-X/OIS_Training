from enum import Enum

# ===== CONFIG CLASS =====
class Config:
    """Classe centrale per configurazione costanti del programma."""
    class CustomOperators(Enum):
        PARALLELO = "|"                  # Operatore parallelo per resistenze
        FUNZIONE = ">"                   # Operatore per funzioni speciali
        FATTORIALE = "!"                 # Operatore fattoriale
        COMMENTO = "#"                   # Simbolo per commenti
    
    # Operatori supportati
    OPERATORI_SPECIALI = {op.value for op in CustomOperators}
    OPERATORI = set("+-*/^()=%") | OPERATORI_SPECIALI
    
    # Nomi operatori speciali
    class SpecialOperators(Enum):
        POWER = "P"                    # Potenza
        CURRENT_DIVIDER = "PC"         # Partitore di corrente
        VOLTAGE_DIVIDER = "PT"         # Partitore di tensione
        KRAMER = "KRAMER"              # Risolutore sistemi 3x3
        PARALLELO = "PLL"              # Operatore parallelo
        SQRT = "SQRT"                  # Radice quadrata
        ABS = "ABS"                    # Valore assoluto
        LOG = "LOG"                    # Logaritmo base 10
        LOG2 = "LOG2"                  # Logaritmo base 2
        LEN = "LEN"                    # Lunghezza stringa
        SIN = "SIN"                    # Seno
        COS = "COS"                    # Coseno
        TAN = "TAN"                    # Tangente
        ASIN = "ASIN"                  # Arcoseno
        ACOS = "ACOS"                  # Arcocoseno
        ATAN = "ATAN"                  # Arcotangente
        DEG = "DEG"                    # Conversione a gradi
        RAD = "RAD"                    # Conversione a radianti
        GCD = "GCD"                    # Massimo comun divisore
        LCM = "LCM"                    # Minimo comune multiplo
        HYPOT = "HYPOT"                # Ipotenusa
        PRIMO = "PRIMO"                # Verifica se è un numero primo
        
    class CustomFuncs(Enum):
        ESCI = "exit"                  # Comando per uscire
        SHOW = "show"                  # Comando per mostrare variabili
        HELP = "help"                  # Comando per mostrare aiuto
        LEGGI = "read"                 # Comando per leggere file
        PULISCI = "clear"              # Comando per pulire variabili
        KRAMER = "KRAMER"              # Comando per risolvere sistemi 3x3
        LEN = "LEN"                    # Comando per lunghezza stringa
        FATTORI = "FACTORS"            # Comando per fattori primi
        PRIMO = "PRIMO"                # Comando per verificare se è un numero primo
        DIVISORI = "DIVISORI"          # Comandi per vedere i divisori di un numero
        COMBINAZIONI = "NCR"           # Calcola numeri combinazioni (ordine non conta)
        PERMUTAZIONI = "NPR"           # Calcola numero di permutazioni (ordine conta)
        PWD = "pwd"                    # Pint working directory
        SALVA = "save"                 # Comando per salvare variabili su file
        LIST = "list"                  # Fa vedere tutte le sessioni nella path disgnata


    NOMI_OPERATORI_SPECIALI = set([m.value for m in SpecialOperators])
    NOMI_NON_VALIDI = {m.value for m in CustomFuncs} | NOMI_OPERATORI_SPECIALI
    
    # Costanti di sistema
    KRAMER_PARAMS = 12                 # Numero parametri per Kramer (3 eq x 4 valori)
    KRAMER_EQUATIONS = 3               # Numero equazioni Kramer
    KRAMER_COEFFICIENTS = 4            # Coefficienti per equazione (x, y, z, d)
    MIN_RESISTANCES = 2                # Numero minimo resistenze necessario
    PI = "pi"                          # Pigreco
    RIS_PRECEDENTE = "ris"             # var dove salva risultato calcolato
    ESTENSIONE_SESSIONE = "session"   # estensione file per salvataggio sessione

# Alias 
OPERATORI = Config.OPERATORI
OPERATORI_SPECIALI = Config.OPERATORI_SPECIALI
NOMI_OPERATORI_SPECIALI = Config.NOMI_OPERATORI_SPECIALI
NOMI_NON_VALIDI = Config.NOMI_NON_VALIDI