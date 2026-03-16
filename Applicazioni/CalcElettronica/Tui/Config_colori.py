from textual.theme import Theme
"""Costanti colori"""

COLORE_NOME_VARIABILE = "bold cyan"
COLORE_SELETTORE = "bold white"
COLORE_FOOTER = "bold white"
DEFAULT_THEME = "monokai"
COLORE_OUTPUT_INFO = "#ffffff"
COLORE_OUTPUT_RESULT = "#ffffff"
COLORE_OUTPUT_ERROR = "#e74c3c"
COLORE_OUTPUT_COMMAND = "#b1aeae"
COLORE_OUTPUT_TABLE = "#8677ea"
COLORE_OUTPUT_TABLE_VALUE = "#ffffff"

# --- Colori sezione Help ---
COLORE_HELP_SEZIONE  = "bold cyan"       # intestazioni sezione (TUTTO MAIUSCOLO:)
COLORE_HELP_VOCE     = "bright_green"    # parte sinistra di righe con ->
COLORE_HELP_TESTO    = "white"           # testo normale
COLORE_HELP_NOTA     = "dim white"       # descrizione a destra di ->

# tema custom
CALC_THEME = Theme(
    name="calc-elettronica",
    primary="#5C1B9DC5",
    secondary="#8677ea",
    background="#242424",
    surface="#DD9AEC",
    panel="#E983BB",
    warning="#f52323",
    error="#e74c3c",
    success="#ffffff",
    accent="#b1aeae",
    dark=True,
)
