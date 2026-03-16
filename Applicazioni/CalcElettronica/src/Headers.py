from src.config import Config
import os

# sito ASCI art: https://patorjk.com/software/taag/#p=display&f=ANSI+Regular&t=HElp&x=none&v=4&h=4&w=80&we=false

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def titolo() -> None:
    return """
 ██████  █████  ██       ██████  ██████  ██       █████  ████████ ██████  ██  ██████ ███████ 
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██   ██ ██ ██      ██      
██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██████  ██ ██      █████   
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██   ██ ██ ██      ██      
 ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██    ██   ██ ██  ██████ ███████ 
                                                                                             
"""
    
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
def_cmd = Config.CustomFuncs.DEF.value
showf_cmd = Config.CustomFuncs.SHOW_FUNCTIONS.value

par_op = Config.CustomOperators.PARALLELO.value
fun_op = Config.CustomOperators.FUNZIONE.value
fat_op = Config.CustomOperators.FATTORIALE.value
commento_op = Config.CustomOperators.COMMENTO.value

ris_precedente = Config.RIS_PRECEDENTE
        
# ===== STRING GETTERS PER TUI =====

def get_help_espressioni() -> str:
    return f"""OPERAZIONI BASE:
  +  addizione
  -  sottrazione
  *  moltiplicazione
  /  divisione
  ^  potenza  (es: 2^3 = 8)
  ( ) parentesi

FUNZIONI SPECIALI  (sintassi: NOME{fun_op}parametri):
  {p}{fun_op}(V,I)                -> Potenza (V*I)
  {pt}{fun_op}(R1,R2,Vin)         -> Partitore tensione su R1
  {pc}{fun_op}(R1,R2,Itot)        -> Partitore corrente in R2
  {pll}{fun_op}(R1,R2,...)        -> Resistenze in parallelo
  {sqrt}{fun_op}(x) o {sqrt}{fun_op}(x,n)   -> Radice n-esima
  {abs_op}{fun_op}(x)                -> Valore assoluto
  {log_op}{fun_op}(x) o {log_op}{fun_op}(x,b)    -> Logaritmo (base b)
  {log2}{fun_op}(x)               -> Logaritmo base 2
  {sin_op}{fun_op}(x), {cos_op}{fun_op}(x), {tan_op}{fun_op}(x)   -> Trigonometria
  {asin}{fun_op}(x), {acos}{fun_op}(x), {atan}{fun_op}(x)   -> Inversi trig.
  {deg}{fun_op}(x)                -> Radianti -> Gradi
  {rad}{fun_op}(x)                -> Gradi -> Radianti
  {gcd_op}{fun_op}(a,b)              -> Massimo comun divisore
  {lcm}{fun_op}(a,b)              -> Minimo comune multiplo
  {hypot}{fun_op}(a,b)            -> Ipotenusa
  {primo}{fun_op}(x)              -> Verifica se primo (1=si, 0=no)
  x{fat_op}                     -> Fattoriale
  x{par_op}y                     -> Parallelo resistenze

COMANDI:
  {exit_cmd}            -> Torna al menu
  {show_cmd}            -> Mostra variabili
  {showf_cmd}           -> Mostra funzioni utente
  {clear_cmd}           -> Cancella variabili
  {read_cmd}            -> Leggi da file
  {kramer_cmd}          -> Risolvi sistema 3x3
  {def_cmd}             -> Crea funzione utente guidata
  {factors_cmd} x       -> Fattori primi di x
  {divisori_cmd} x      -> Divisori di x
  {combinazioni_cmd} n,k   -> Combinazioni C(n,k)
  {permutazioni_cmd} n,k   -> Permutazioni P(n,k)

FUNZIONI UTENTE:
  Definizione guidata:  {def_cmd}
  Definizione inline:   {def_cmd} | nome | arg1,arg2,... | espressione
  Chiamata:             nome{fun_op}arg1,arg2,...
  Esempio:
      {def_cmd} | somma2 | x,y | x+y
      somma2{fun_op}3,4

VARIABILI:
  Definisci:   x = 5
  Usa:         x + y
  Risultato precedente disponibile in: {ris_precedente}
  {ris_precedente} non viene sovrascritto dai Comandi
  Prima dell'= viene valutata tutta l'espressione a destra
"""

def get_help_kramer() -> str:
    return """GUIDA KRAMER 3x3:

Risolve sistemi lineari 3x3 con il metodo di Cramer.

FORMATO:
  a1*x + b1*y + c1*z = d1
  a2*x + b2*y + c2*z = d2
  a3*x + b3*y + c3*z = d3

ESEMPIO:
  2x + y - z = 8
  -3x - y + 2z = -11
  -2x + y + 2z = -3

ALL'INSERIMENTO:
  Digita 4 numeri separati da spazio per ogni equazione:
  equazione 1:  2 1 -1 8
  equazione 2:  -3 -1 2 -11
  equazione 3:  -2 1 2 -3

  Risposta: x = 2.0, y = 3.0, z = -1.0

NOTE:
  Sovrascrive le variabili x, y, z con i risultati
  det = 0  ->  infinite soluzioni
  det = 0 e det_speciali != 0  ->  nessuna soluzione
"""

def get_help_comandi() -> str:
    return f"""COMANDI DISPONIBILI:

DURANTE L'INSERIMENTO:
  {exit_cmd}       -> Ritorna al menu precedente
  {help_cmd}       -> Mostra questo aiuto
  {show_cmd}       -> Mostra variabili definite
  {showf_cmd}      -> Mostra funzioni utente
  {def_cmd}        -> Crea funzione utente guidata
  {clear_cmd}      -> Cancella tutte le variabili
  {kramer_cmd}     -> Risolvi un sistema 3x3

COMANDI DI SESSIONE:
  {pwd_cmd}        -> Mostra directory corrente
  {save_cmd}       -> Salva sessione su file (variabili + funzioni)
  {list_cmd}       -> Elenca tutte le sessioni salvate
  {read_cmd}       -> Carica una sessione da file

SINTASSI RAPIDA FUNZIONI:
  Inline:   {def_cmd} | nome | arg1,arg2,... | espressione
  Chiamata: nome{fun_op}arg1,arg2,...

SUGGERIMENTI:
  Le variabili rimangono salvate fino a {clear_cmd}
  Usa parentesi per chiarire l'ordine delle operazioni
  I parametri delle funzioni sono separati da virgola
"""

def get_help_file_lettura() -> str:
    return f"""LETTURA FILE (input.txt):

Il programma legge espressioni da input.txt e carica i dati.

FORMATO SUPPORTATO:
  Una espressione per riga
  Linee vuote vengono ignorate
  Linee che iniziano con {commento_op} sono commenti

ESEMPIO DI input.txt:
  {commento_op} Calcoli di prova
  2 + 3 * 4
  (10 + 5) / 3
  {p}{fun_op}(12,2)
  {def_cmd} | func | x | x*(x+1)/2
  y = func{fun_op}10
  {sqrt}{fun_op}16
  x = 5
  x * 2

NOTE:
  Le variabili definite persistono alle righe successive
  Puoi definire funzioni inline con {def_cmd}
  Comandi interattivi ({help_cmd}, {show_cmd}, {showf_cmd}) non usabili in file
"""

def get_help_precedenze() -> str:
    return f"""PRECEDENZE OPERATORI:

Ordine di valutazione (dal PRIMO all'ULTIMO):

  1.  ( )                     -> Parentesi
  2.  NOME{fun_op}(args)      -> Funzioni speciali e utente
  3.  x{fat_op}               -> Fattoriale
  4.  x{par_op}y              -> Parallelo resistenze
  5.  ^                       -> Potenza
  6.  * /                     -> Molt. e div. (sx -> dx)
  7.  + -                     -> Add. e sott. (sx -> dx)

REGOLE:
  Le parentesi hanno sempre la precedenza massima
  Le funzioni speciali precedono le operazioni aritmetiche
  Il fattoriale si applica solo al numero immediatamente prima
  Il parallelo ha precedenza su *, / e +, -
  A parita' di precedenza si valuta da sinistra a destra

ASSEGNAMENTO:
  x = 2 + 3 * 4   ->  x = 14
  (l'espressione a destra viene valutata per intero, poi assegnata)

ESEMPI:
  2 + 3 * 4          =  14
  (2 + 3) * 4        =  20
  2 ^ 3 * 4          =  32   (^ prima di *)
  5{fat_op} + 1      =  121
  4{par_op}4 * 2     =  4    (| prima di *)
  {sqrt}{fun_op}(9) + 1   =  4
"""

def get_help_bitwise() -> str:
    return """CALCOLATORE BITWISE:

Lavora su interi con operatori bit a bit.

OPERATORI:
  &    -> AND bit a bit
  |    -> OR bit a bit
  ^    -> XOR bit a bit
  ~x   -> NOT bit a bit (complemento)
  <    -> Shift sinistra  (es: 5 < 1 = 10)
  >    -> Shift destra    (es: 8 > 1 = 4)
  ( )  -> Parentesi

VARIABILI:
  a = 5
  b = a < 2
  ris  ->  contiene sempre l'ultimo risultato

COMANDI NELLA SESSIONE BITWISE:
  show       -> Mostra variabili salvate
  confronta  -> Mostra DEC/BIN/HEX di un valore

ESEMPI:
  5 & 3
  (8 > 1) | 1
  mask = 15
  ~mask

NOTE:
  Usa solo numeri interi
  Gli shift usano i simboli singoli: < e >
"""

HELP_TOPICS: dict[str, object] = {
    "Espressioni":          get_help_espressioni,
    "Kramer 3x3":           get_help_kramer,
    "Comandi speciali":     get_help_comandi,
    "Lettura file":         get_help_file_lettura,
    "Precedenze operatori": get_help_precedenze,
    "Calcolatore bitwise":  get_help_bitwise,
}