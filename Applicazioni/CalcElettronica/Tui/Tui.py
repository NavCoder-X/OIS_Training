import sys
import os
# Aggiunge la cartella CalcElettronica al path per poter importare src.*
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widgets import Footer, Static, Label, Input, Button
from textual import events
from textual.binding import Binding
from textual.message import Message
from textual.containers import VerticalScroll, HorizontalGroup, Vertical
from textual import on
from rich.markup import escape as _rich_escape
from math import floor, pi
from more_itertools import factor

from Tui.Config_colori import *
from src.Headers import HELP_TOPICS, titolo
from src.config import Config, ERROR_FILE, OUTPUT_FILE
from src.utilities import FUNZIONI, clear_io_files, salvaSessioneConNome, listSessioni
from src.espressioni import controlloExpr, variabili as EXPR_VARIABILI, processaEspressione, processaFile
from src.utilities import tokenize
from src.operatori import Kramer3x3, divisori, nCr, nPr
from src.boleanParser import BitwiseParser, VARIABILI as BOOL_VARIABILI


# In frozen --onefile la cartella di __file__ è sys._MEIPASS (temporanea).
# I file dati vanno scritti accanto all'exe, non nella cartella di estrazione.
if getattr(sys, 'frozen', False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
else:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _insert_text_in_input(widget: Input, text: str) -> None:
    pos = widget.cursor_position
    value = widget.value
    widget.value = value[:pos] + text + value[pos:]
    widget.cursor_position = pos + len(text)


def _keypad_key_to_char(key: str) -> str | None:
    key = (key or "").lower()
    mapping = {
        "kp_0": "0",
        "kp_1": "1",
        "kp_2": "2",
        "kp_3": "3",
        "kp_4": "4",
        "kp_5": "5",
        "kp_6": "6",
        "kp_7": "7",
        "kp_8": "8",
        "kp_9": "9",
        "keypad_0": "0",
        "keypad_1": "1",
        "keypad_2": "2",
        "keypad_3": "3",
        "keypad_4": "4",
        "keypad_5": "5",
        "keypad_6": "6",
        "keypad_7": "7",
        "keypad_8": "8",
        "keypad_9": "9",
        "numpad0": "0",
        "numpad1": "1",
        "numpad2": "2",
        "numpad3": "3",
        "numpad4": "4",
        "numpad5": "5",
        "numpad6": "6",
        "numpad7": "7",
        "numpad8": "8",
        "numpad9": "9",
        "kp_decimal": ".",
        "kp_period": ".",
        "keypad_decimal": ".",
        "kp_add": "+",
        "kp_subtract": "-",
        "kp_multiply": "*",
        "kp_divide": "/",
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/",
        "decimal": ".",
        "equal": "=",
        "separator": ",",
        "keypad_add": "+",
        "keypad_subtract": "-",
        "keypad_multiply": "*",
        "keypad_divide": "/",
        "plus": "+",
        "plus_sign": "+",
        "minus": "-",
        "minus_sign": "-",
        "asterisk": "*",
        "star": "*",
        "slash": "/",
        "forward_slash": "/",
    }
    if key in mapping:
        return mapping[key]

    # Fallback per naming differenti tra terminali (es. keypad-1, numpad_7, kp9)
    compact = key.replace("-", "_")
    if any(prefix in compact for prefix in ("kp", "keypad", "numpad")):
        for digit in "0123456789":
            if compact.endswith(f"_{digit}") or compact.endswith(digit):
                return digit
        if "decimal" in compact or "period" in compact or "dot" in compact:
            return "."
        if "add" in compact or "plus" in compact:
            return "+"
        if "subtract" in compact or "minus" in compact:
            return "-"
        if "multiply" in compact or "asterisk" in compact:
            return "*"
        if "divide" in compact or "slash" in compact:
            return "/"

    return None


def _handle_manual_input_key(event: events.Key, widget: Input) -> bool:
    if event.character == " " or event.key in ("space", "spacebar"):
        _insert_text_in_input(widget, " ")
        event.stop()
        event.prevent_default()
        return True

    mapped = _keypad_key_to_char(event.key)
    if mapped is not None:
        _insert_text_in_input(widget, mapped)
        event.stop()
        event.prevent_default()
        return True

    return False


def _render_variables_table(variables: dict) -> str:
    if not variables:
        return "Nessuna variabile"

    rows = [(str(key), str(variables[key])) for key in sorted(variables.keys())]
    return _render_clean_table(("NOME", "VALORE"), rows)


def _to_base_without_prefix(value: int, base: int) -> str:
    if base not in (2, 16):
        raise ValueError("Base non supportata")

    sign = "-" if value < 0 else ""
    raw = format(abs(value), "b" if base == 2 else "x")
    return f"{sign}{raw}"


def _render_clean_table(headers: tuple[str, ...], rows: list[tuple[str, ...]]) -> str:
    if not rows:
        return ""

    widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    header_line = " | ".join(header.ljust(widths[i]) for i, header in enumerate(headers))
    separator = "-+-".join("-" * width for width in widths)
    body = [" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)) for row in rows]

    return "\n".join([header_line, separator, *body])


def _render_number_formats_table(values: list[int]) -> str:
    if not values:
        return "Nessun valore"

    rows = [
        (str(v), _to_base_without_prefix(v, 2), _to_base_without_prefix(v, 16))
        for v in values
    ]
    return _render_clean_table(("DEC", "BIN", "HEX"), rows)


def _read_and_clear_file(file_name: str) -> list[str]:
    path = os.path.join(PROJECT_ROOT, file_name)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines() if line.rstrip("\n")]
    with open(path, "w", encoding="utf-8") as f:
        f.write("")
    return lines


def _collect_backend_messages() -> list[str]:
    errors = _read_and_clear_file(ERROR_FILE)
    outputs = _read_and_clear_file(OUTPUT_FILE)
    messages = []
    for line in outputs:
        messages.append(f"OUT: {line}")
    for line in errors:
        messages.append(f"ERR: {line}")
    return messages


def _format_table_line(line: str) -> str:
    stripped = line.strip()
    if set(stripped) <= set("-+") and stripped:
        return f"[{COLORE_OUTPUT_TABLE}]{_rich_escape(line)}[/{COLORE_OUTPUT_TABLE}]"

    if " | " in line:
        return f"[{COLORE_OUTPUT_TABLE_VALUE}]{_rich_escape(line)}[/{COLORE_OUTPUT_TABLE_VALUE}]"

    return f"[{COLORE_OUTPUT_TABLE_VALUE}]{_rich_escape(line)}[/{COLORE_OUTPUT_TABLE_VALUE}]"


def _format_console_line(line: str) -> str:
    if not line:
        return ""

    stripped = line.strip()
    if " | " in line or (stripped and set(stripped) <= set("-+")):
        return _format_table_line(line)

    if line.startswith("ERR: "):
        payload = _rich_escape(line[5:])
        return f"[bold {COLORE_OUTPUT_ERROR}]ERR:[/bold {COLORE_OUTPUT_ERROR}] [{COLORE_OUTPUT_ERROR}]{payload}[/{COLORE_OUTPUT_ERROR}]"

    if line.startswith("> "):
        return f"[{COLORE_OUTPUT_COMMAND}]>{_rich_escape(line[1:])}[/{COLORE_OUTPUT_COMMAND}]"

    if line.startswith("OUT: "):
        payload = line[5:]
        if payload.startswith("Risultato:"):
            return f"[bold {COLORE_OUTPUT_RESULT}]{_rich_escape(payload)}[/bold {COLORE_OUTPUT_RESULT}]"
        return f"[{COLORE_OUTPUT_INFO}]{_rich_escape(payload)}[/{COLORE_OUTPUT_INFO}]"

    if stripped.startswith(("Risultato:", "Soluzioni:")):
        return f"[bold {COLORE_OUTPUT_RESULT}]{_rich_escape(line)}[/bold {COLORE_OUTPUT_RESULT}]"

    if "errore" in stripped.lower() or "non valida" in stripped.lower():
        return f"[{COLORE_OUTPUT_ERROR}]{_rich_escape(line)}[/{COLORE_OUTPUT_ERROR}]"

    if stripped.startswith(("Comandi utili:", "Operatori:")):
        return f"[{COLORE_OUTPUT_TABLE}]{_rich_escape(line)}[/{COLORE_OUTPUT_TABLE}]"

    return f"[{COLORE_OUTPUT_INFO}]{_rich_escape(line)}[/{COLORE_OUTPUT_INFO}]"


def _render_console_blocks(lines: list[str]) -> str:
    formatted: list[str] = []
    for block in lines:
        for line in block.splitlines() or [""]:
            formatted.append(_format_console_line(line))
    return "\n".join(formatted)


class PromptModal(ModalScreen[dict | None]):
    BINDINGS = [
        Binding("escape", "cancel", "Annulla", show=False),
    ]

    def __init__(self, title: str, fields: list[tuple[str, str, str]]) -> None:
        super().__init__()
        self.title_text = title
        self.fields = fields

    def compose(self) -> ComposeResult:
        with Vertical(classes="prompt-modal"):
            yield Static(self.title_text, classes="prompt-title")
            yield Static("Compila i campi e premi INVIO per confermare", classes="prompt-subtitle")
            for key, label, placeholder in self.fields:
                yield Label(label, classes="prompt-label")
                yield Input(placeholder=placeholder, id=f"prompt_{key}", classes="prompt-input")
            with HorizontalGroup(classes="prompt-actions"):
                yield Button("Annulla", id="cancel")
                yield Button("Conferma", id="confirm", variant="primary")

    def on_mount(self) -> None:
        self.border_title = "Prompt"
        if self.fields:
            first = self.query_one(f"#prompt_{self.fields[0][0]}", Input)
            self.call_after_refresh(first.focus)

    def on_key(self, event: events.Key) -> None:
        focused = self.focused
        if not isinstance(focused, Input):
            return
        _handle_manual_input_key(event, focused)

    def action_cancel(self) -> None:
        self.dismiss(None)

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancel":
            self.dismiss(None)
            return
        if event.button.id == "confirm":
            data = {}
            for key, _, _ in self.fields:
                inp = self.query_one(f"#prompt_{key}", Input)
                data[key] = inp.value
            self.dismiss(data)

    @on(Input.Submitted)
    def on_input_submitted(self, event: Input.Submitted) -> None:
        inputs = [self.query_one(f"#prompt_{key}", Input) for key, _, _ in self.fields]
        try:
            idx = inputs.index(event.input)
        except ValueError:
            return

        if idx < len(inputs) - 1:
            inputs[idx + 1].focus()
        else:
            data = {}
            for key, _, _ in self.fields:
                inp = self.query_one(f"#prompt_{key}", Input)
                data[key] = inp.value
            self.dismiss(data)

def _format_help_text(text: str) -> str:
    """Aggiunge markup Rich al testo dell'help colorando sezioni, comandi e note."""
    result = []
    for line in text.split('\n'):
        sleft = line.lstrip()
        if not sleft:
            result.append('')
            continue
        safe = _rich_escape(line)
        # Titolo sezione: prima parola tutta maiuscola (>2 lettere), riga finisce con ':'
        first_word = sleft.rstrip(':').split()[0] if sleft.rstrip(':').split() else ''
        if sleft.endswith(':') and first_word.isupper() and len(first_word) > 2:
            result.append(f"[{COLORE_HELP_SEZIONE}]{safe}[/{COLORE_HELP_SEZIONE}]")
        elif '->' in line:
            idx = line.index('->')
            left  = _rich_escape(line[:idx])
            right = _rich_escape(line[idx + 2:])
            result.append(
                f"[{COLORE_HELP_VOCE}]{left}[/{COLORE_HELP_VOCE}]"
                f"[{COLORE_HELP_TESTO}]->[/{COLORE_HELP_TESTO}]"
                f"[{COLORE_HELP_NOTA}]{right}[/{COLORE_HELP_NOTA}]"
            )
        else:
            result.append(f"[{COLORE_HELP_TESTO}]{safe}[/{COLORE_HELP_TESTO}]")
    return '\n'.join(result)

class VariabiliScreen(VerticalScroll):
    def compose(self) -> ComposeResult:
        self.text = "Nessuna variabile"
        yield Label(self.text)

    def on_mount(self):
        self.add_class("Variabili")
        self.border_title = "Variabili"

    def on_focus(self):
        self.add_class("focus")
    def on_blur(self):
        self.remove_class("focus")

    def update_text(self, variables: dict):
        self.text = _render_variables_table(variables)
        self.query_one(Label).update(self.text)

class FunzioniScreen(VerticalScroll):
    def compose(self) -> ComposeResult:
        self.text = "Nessuna funzione"
        yield Label(self.text)

    def on_mount(self):
        self.add_class("Funzioni")
        self.border_title = "Funzioni"

    def on_focus(self):
        self.add_class("focus")
    def on_blur(self):
        self.remove_class("focus")

    def update_text(self, functions: dict):
        if not functions:
            self.text = "Nessuna funzione"
        else:
            lines = []
            for name, f in functions.items():
                lines.append(f"[{COLORE_NOME_VARIABILE}]{name}[/{COLORE_NOME_VARIABILE}]({', '.join(f.argomenti)}) = {f.logic}")
            self.text = "\n".join(lines)
        self.query_one(Label).update(self.text)
       
class EspressioniScreen(Vertical):
    def compose(self) -> ComposeResult:
        self.result_area = Static("", classes="result-area")
        self.input_area = Input(placeholder="Espressione o comando...")
        yield self.result_area
        yield self.input_area

    def on_mount(self):
        self.lines: list[str] = []
        self.history: list[str] = []
        self.history_index: int | None = None
        self.add_class("Espressioni")
        self.border_title = "Espressioni"
        self.input_area.add_class("input")
        self._append_line("Calcolatrice espressioni pronta")
        self._append_line("Comandi utili: show, showf, clear, DIVISORI, FACTORS, NCR, NPR, LEN, KRAMER")
        self._sync_side_panels()
        self.call_after_refresh(self.input_area.focus)

    def on_focus(self):
        self.add_class("focus")
        self.input_area.focus()

    def on_blur(self):
        self.remove_class("focus")

    @on(Input.Submitted)
    def submit_espressione(self, event: Input.Submitted):
        if event.input is not self.input_area:
            return

        expr = event.value.strip()
        self.input_area.value = ""
        if not expr:
            return

        self._push_history(expr)

        self._reset_output(expr)
        self._dispatch(expr)
        self._sync_side_panels()

    def on_key(self, event: events.Key):
        if not self.input_area.has_focus:
            return

        if event.key == "up":
            self._history_up()
            event.stop()
            event.prevent_default()
            return

        if event.key == "down":
            self._history_down()
            event.stop()
            event.prevent_default()
            return

        _handle_manual_input_key(event, self.input_area)

    def _push_history(self, expr: str) -> None:
        if not self.history or self.history[-1] != expr:
            self.history.append(expr)
        self.history = self.history[-100:]
        self.history_index = None

    def _set_input_value(self, value: str) -> None:
        self.input_area.value = value
        self.input_area.cursor_position = len(value)

    def _history_up(self) -> None:
        if not self.history:
            return
        if self.history_index is None:
            self.history_index = len(self.history) - 1
        elif self.history_index > 0:
            self.history_index -= 1
        self._set_input_value(self.history[self.history_index])

    def _history_down(self) -> None:
        if self.history_index is None:
            return
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self._set_input_value(self.history[self.history_index])
            return
        self.history_index = None
        self._set_input_value("")

    def _append_line(self, line: str) -> None:
        self.lines.append(line)
        self.lines = self.lines[-16:]
        self.result_area.update(_render_console_blocks(self.lines))

    def _reset_output(self, expr: str | None = None) -> None:
        self.lines = []
        if expr is not None:
            self.lines.append(f"> {expr}")
        self.result_area.update(_render_console_blocks(self.lines))

    def _sync_side_panels(self) -> None:
        parent = self.parent
        if isinstance(parent, LayoutScreen_Espressioni):
            parent.variabili.update_text(EXPR_VARIABILI)
            parent.funzioni.update_text(FUNZIONI)

    def _eval_number(self, expr: str) -> float | None:
        expr = expr.strip().replace(" ", "")
        if not expr:
            return None
        clear_io_files()
        value = processaEspressione(tokenize(expr), EXPR_VARIABILI)
        for msg in _collect_backend_messages():
            self._append_line(msg)
        return value

    def _dispatch(self, expr: str) -> None:
        cmd = expr

        if cmd == Config.CustomFuncs.SHOW.value:
            self._sync_side_panels()
            self._append_line("Variabili aggiornate nel pannello a sinistra")
            return

        if cmd == Config.CustomFuncs.SHOW_FUNCTIONS.value:
            self._sync_side_panels()
            self._append_line("Funzioni aggiornate nel pannello a destra")
            return

        if cmd == Config.CustomFuncs.PULISCI.value:
            EXPR_VARIABILI.clear()
            EXPR_VARIABILI[Config.PI] = pi
            self._append_line("Variabili cancellate")
            return

        if cmd == Config.CustomFuncs.DIVISORI.value:
            modal = PromptModal("DIVISORI", [("n", "Numero", "es: 120 o x+3")])
            self.app.push_screen(modal, self._handle_divisori)
            return

        if cmd == Config.CustomFuncs.FATTORI.value:
            modal = PromptModal("FACTORS", [("n", "Numero", "es: 84")])
            self.app.push_screen(modal, self._handle_factors)
            return

        if cmd == Config.CustomFuncs.COMBINAZIONI.value:
            modal = PromptModal(
                "NCR",
                [
                    ("n", "Elementi totali (n)", "es: 10"),
                    ("r", "Elementi scelti (r)", "es: 3"),
                ],
            )
            self.app.push_screen(modal, self._handle_ncr)
            return

        if cmd == Config.CustomFuncs.PERMUTAZIONI.value:
            modal = PromptModal(
                "NPR",
                [
                    ("n", "Elementi totali (n)", "es: 10"),
                    ("r", "Elementi scelti (r)", "es: 3"),
                ],
            )
            self.app.push_screen(modal, self._handle_npr)
            return

        if cmd == Config.CustomFuncs.LEN.value:
            modal = PromptModal("LEN", [("s", "Stringa", "testo da misurare")])
            self.app.push_screen(modal, self._handle_len)
            return

        if cmd == Config.CustomFuncs.KRAMER.value:
            modal = PromptModal(
                "KRAMER 3x3",
                [
                    ("eq1", "Equazione 1 (x y z d)", "es: 2 1 -1 8"),
                    ("eq2", "Equazione 2 (x y z d)", "es: -3 -1 2 -11"),
                    ("eq3", "Equazione 3 (x y z d)", "es: -2 1 2 -3"),
                ],
            )
            self.app.push_screen(modal, self._handle_kramer)
            return

        if cmd == Config.CustomFuncs.ESCI.value:
            self._append_line("Comando exit disabilitato in TUI. Usa Ctrl+W per tornare al menu")
            return

        if cmd == Config.CustomFuncs.SALVA.value:
            modal = PromptModal("Salva Sessione", [("name", "Nome sessione", "es: mia_sessione")])
            self.app.push_screen(modal, self._handle_save)
            return

        if cmd == Config.CustomFuncs.LEGGI.value:
            modal = PromptModal("Leggi Sessione", [("path", "Path file", "es: mia_sessione.session")])
            self.app.push_screen(modal, self._handle_read)
            return

        if cmd == Config.CustomFuncs.LIST.value:
            clear_io_files()
            listSessioni(PROJECT_ROOT)
            for msg in _collect_backend_messages():
                self._append_line(msg)
            return

        if cmd == Config.CustomFuncs.PWD.value:
            self._append_line(f"Path: {PROJECT_ROOT}")
            return

        clear_io_files()
        controlloExpr(expr, EXPR_VARIABILI)
        messages = _collect_backend_messages()
        for msg in messages:
            self._append_line(msg)

    def _resolve_session_file(self, raw_path: str) -> str:
        candidate = raw_path.strip()
        if not candidate:
            return ""
        if not os.path.isabs(candidate):
            candidate = os.path.join(PROJECT_ROOT, candidate)
        return os.path.normpath(candidate)

    def _handle_save(self, data: dict | None) -> None:
        if not data:
            self._append_line("Salvataggio annullato")
            return
        name = data.get("name", "").strip()
        if not name:
            self._append_line("Nome sessione mancante")
            return

        clear_io_files()
        salvaSessioneConNome(EXPR_VARIABILI, name)
        for msg in _collect_backend_messages():
            self._append_line(msg)
        self._sync_side_panels()

    def _handle_read(self, data: dict | None) -> None:
        if not data:
            self._append_line("Lettura annullata")
            return

        raw_path = data.get("path", "").strip()
        if not raw_path:
            self._append_line("Path file mancante")
            return

        session_path = self._resolve_session_file(raw_path)
        if not session_path:
            self._append_line("Path file non valido")
            return

        if not os.path.isfile(session_path):
            self._append_line("File sessione non trovato")
            return

        clear_io_files()
        processaFile(session_path, EXPR_VARIABILI)
        for msg in _collect_backend_messages():
            self._append_line(msg)
        self._append_line("Sessione caricata")
        self._sync_side_panels()

    def _handle_divisori(self, data: dict | None) -> None:
        if not data:
            self._append_line("DIVISORI annullato")
            return
        value = self._eval_number(data.get("n", ""))
        if value is None:
            self._append_line("Numero non valido")
            return
        n = floor(value)
        self._append_line(f"Risultato: {divisori(n)}")

    def _handle_factors(self, data: dict | None) -> None:
        if not data:
            self._append_line("FACTORS annullato")
            return
        value = self._eval_number(data.get("n", ""))
        if value is None:
            self._append_line("Numero non valido")
            return
        n = floor(value)
        self._append_line(f"Risultato: {list(factor(n))}")

    def _handle_ncr(self, data: dict | None) -> None:
        if not data:
            self._append_line("NCR annullato")
            return
        n_val = self._eval_number(data.get("n", ""))
        r_val = self._eval_number(data.get("r", ""))
        if n_val is None or r_val is None:
            self._append_line("Valori non validi")
            return
        n = floor(n_val)
        r = floor(r_val)
        result = nCr(n, r)
        if result is not None:
            EXPR_VARIABILI[Config.RIS_PRECEDENTE] = result
            self._append_line(f"Risultato: {result}")

    def _handle_npr(self, data: dict | None) -> None:
        if not data:
            self._append_line("NPR annullato")
            return
        n_val = self._eval_number(data.get("n", ""))
        r_val = self._eval_number(data.get("r", ""))
        if n_val is None or r_val is None:
            self._append_line("Valori non validi")
            return
        n = floor(n_val)
        r = floor(r_val)
        result = nPr(n, r)
        if result is not None:
            EXPR_VARIABILI[Config.RIS_PRECEDENTE] = result
            self._append_line(f"Risultato: {result}")

    def _handle_len(self, data: dict | None) -> None:
        if not data:
            self._append_line("LEN annullato")
            return
        text = data.get("s", "")
        result = len(text)
        EXPR_VARIABILI[Config.RIS_PRECEDENTE] = result
        self._append_line(f"Risultato: {result}")

    def _parse_kramer_row(self, row: str) -> list[float] | None:
        parts = row.strip().split()
        if len(parts) != 4:
            return None
        result = []
        for token in parts:
            if token in EXPR_VARIABILI:
                result.append(float(EXPR_VARIABILI[token]))
                continue
            value = self._eval_number(token)
            if value is None:
                return None
            result.append(float(value))
        return result

    def _handle_kramer(self, data: dict | None) -> None:
        if not data:
            self._append_line("KRAMER annullato")
            return

        row1 = self._parse_kramer_row(data.get("eq1", ""))
        row2 = self._parse_kramer_row(data.get("eq2", ""))
        row3 = self._parse_kramer_row(data.get("eq3", ""))
        if row1 is None or row2 is None or row3 is None:
            self._append_line("Formato equazioni non valido. Usa: x y z d")
            return

        clear_io_files()
        result = Kramer3x3([row1, row2, row3])
        messages = _collect_backend_messages()
        if result is not None:
            x, y, z = result
            EXPR_VARIABILI["x"] = x
            EXPR_VARIABILI["y"] = y
            EXPR_VARIABILI["z"] = z
            EXPR_VARIABILI[Config.RIS_PRECEDENTE] = z
            self._append_line(f"Soluzioni: x={x}, y={y}, z={z}")
        for msg in messages:
            self._append_line(msg)

        self._sync_side_panels()

class BoleanParserScreen(Vertical):
    def compose(self) -> ComposeResult:
        self.result_area = Static("", classes="result-area")
        self.input_area = Input(placeholder="Espressione bitwise...")
        yield self.result_area
        yield self.input_area
    
    def on_mount(self):
        self.parser = BitwiseParser()
        self.lines: list[str] = []
        self.history: list[str] = []
        self.history_index: int | None = None
        self.add_class("BoleanParser")
        self.border_title = "BoleanParser"
        self._append_line("Parser bitwise pronto")
        self._append_line("Operatori: &, |, ^, ~, <, >, parentesi, assegnamento")
        self.call_after_refresh(self.input_area.focus)
        self._sync_variabili()
    
    def on_focus(self):
        self.add_class("focus")
        self.input_area.focus()

    def on_blur(self):
        self.remove_class("focus")

    @on(Input.Submitted)
    def submit_bolean(self, event: Input.Submitted):
        if event.input is not self.input_area:
            return

        expr = event.value.strip()
        self.input_area.value = ""
        if not expr:
            return

        self._push_history(expr)

        self._reset_output(expr)
        self._dispatch(expr)
        self._sync_variabili()

    def on_key(self, event: events.Key):
        if not self.input_area.has_focus:
            return

        if event.key == "up":
            self._history_up()
            event.stop()
            event.prevent_default()
            return

        if event.key == "down":
            self._history_down()
            event.stop()
            event.prevent_default()
            return

        _handle_manual_input_key(event, self.input_area)

    def _push_history(self, expr: str) -> None:
        if not self.history or self.history[-1] != expr:
            self.history.append(expr)
        self.history = self.history[-100:] # salviamo solo 100 espressioni in cronologia
        self.history_index = None

    def _set_input_value(self, value: str) -> None:
        self.input_area.value = value
        self.input_area.cursor_position = len(value)

    def _history_up(self) -> None:
        if not self.history:
            return
        if self.history_index is None:
            self.history_index = len(self.history) - 1
        elif self.history_index > 0:
            self.history_index -= 1
        self._set_input_value(self.history[self.history_index])

    def _history_down(self) -> None:
        if self.history_index is None:
            return
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self._set_input_value(self.history[self.history_index])
            return
        self.history_index = None
        self._set_input_value("")

    def _append_line(self, line: str) -> None:
        self.lines.append(line)
        self.lines = self.lines[-16:]
        self.result_area.update(_render_console_blocks(self.lines))

    def _reset_output(self, expr: str | None = None) -> None:
        self.lines = []
        if expr is not None:
            self.lines.append(f"> {expr}")
        self.result_area.update(_render_console_blocks(self.lines))

    def _sync_variabili(self) -> None:
        parent = self.parent
        if isinstance(parent, LayoutScreen_Bolean):
            parent.variabili.update_text(BOOL_VARIABILI)

    def _dispatch(self, expr: str) -> None:
        cmd = expr.lower()
        if cmd == "show":
            self._sync_variabili()
            self._append_line("Variabili aggiornate nel pannello a sinistra")
            return

        if cmd == "clear":
            BOOL_VARIABILI.clear()
            self._append_line("Variabili bitwise cancellate")
            return

        if cmd == "confronta":
            modal = PromptModal("Confronta DEC/BIN/HEX", [("value", "Valori", "es: 10 15 ris x")])
            self.app.push_screen(modal, self._handle_confronta)
            return

        clear_io_files()
        tokens = self.parser.tokenize(expr)
        if not self.parser.validate(tokens):
            self._append_line("Espressione non valida")
            for msg in _collect_backend_messages():
                self._append_line(msg)
            return

        result = self.parser.evalWithParentesis(tokens)
        if result is None:
            self._append_line("Espressione non valida")
            for msg in _collect_backend_messages():
                self._append_line(msg)
            return

        try:
            value = int(result)
        except Exception:
            self._append_line("Risultato non convertibile a intero")
            for msg in _collect_backend_messages():
                self._append_line(msg)
            return

        BOOL_VARIABILI["ris"] = str(value)
        self._append_line(_render_number_formats_table([value]))
        for msg in _collect_backend_messages():
            self._append_line(msg)

    def _parse_confronta_values(self, raw: str) -> list[int] | None:
        tokens = raw.replace(",", " ").split()
        if not tokens:
            return None

        values: list[int] = []
        for token in tokens:
            token_value = str(BOOL_VARIABILI[token]) if token in BOOL_VARIABILI else token
            try:
                values.append(int(float(token_value)))
            except Exception:
                return None
        return values

    def _handle_confronta(self, data: dict | None) -> None:
        if not data:
            self._append_line("Confronta annullato")
            return
        raw = data.get("value", "").strip()
        if not raw:
            self._append_line("Valore mancante")
            return

        values = self._parse_confronta_values(raw)
        if values is None:
            self._append_line("Valore non valido")
            return

        self._append_line(_render_number_formats_table(values))

class HelpMenu(VerticalScroll):
    #serve a postare un mesaggio che viene intercettato da HelpScreen per aggiornare il contenuto mostrato
    class TopicSelected(Message):
        def __init__(self, topic: str) -> None:
            self.topic = topic
            super().__init__()

    BINDINGS = [
        Binding("down", "move_down", "Giù",  show=True, priority=True),
        Binding("up",   "move_up",   "Su",   show=True, priority=True),
        Binding("enter","select",    "Apri", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        self.selected_index = 0
        for topic in HELP_TOPICS.keys():
            yield Static(topic, classes="help-topic")

    def on_mount(self):
        self.add_class("HelpMenu")
        self.border_title = "Argomenti"
        self.query(".help-topic")[0].add_class("selected")

    def on_focus(self):
        self.add_class("focus")

    def on_blur(self):
        self.remove_class("focus")

    def action_move_down(self):
        items = self.query(".help-topic")
        items[self.selected_index].remove_class("selected")
        self.selected_index = (self.selected_index + 1) % len(items)
        items[self.selected_index].add_class("selected")

    def action_move_up(self):
        items = self.query(".help-topic")
        items[self.selected_index].remove_class("selected")
        self.selected_index = (self.selected_index - 1) % len(items)
        items[self.selected_index].add_class("selected")

    def action_select(self):
        topic = list(HELP_TOPICS.keys())[self.selected_index]
        self.post_message(self.TopicSelected(topic))

class HelpScreen(VerticalScroll):
    def compose(self) -> ComposeResult:
        self._label = Label("")
        yield self._label

    def on_mount(self):
        self.add_class("Help")
        self.border_title = "Guida"
        # mostra il primo argomento di default
        first = list(HELP_TOPICS.keys())[0]
        self.show_topic(first)

    def on_focus(self):
        self.add_class("focus")

    def on_blur(self):
        self.remove_class("focus")

    def show_topic(self, topic: str):
        if topic in HELP_TOPICS:
            content = HELP_TOPICS[topic]()          # chiama la funzione getter
            self._label.update(_format_help_text(content))  # markup colorato
            self.border_title = topic
            self.scroll_home(animate=False)


class LayoutScreen_Espressioni(HorizontalGroup):
    def compose(self) -> ComposeResult:
        self.variabili = VariabiliScreen()
        self.espressioni = EspressioniScreen()
        self.funzioni = FunzioniScreen()
        yield self.variabili
        yield self.espressioni
        yield self.funzioni
    
    def on_mount(self):
        self.add_class("LayoutScreen")

class LayoutScreen_Bolean(HorizontalGroup):
    def compose(self) -> ComposeResult:
        self.variabili = VariabiliScreen()
        self.bolean = BoleanParserScreen()
        yield self.variabili
        yield self.bolean
    
    def on_mount(self):
        self.add_class("LayoutScreen")

class LayoutScreen_Help(HorizontalGroup):
    def compose(self) -> ComposeResult:
        self.helpMenu = HelpMenu()
        self.helpArea = HelpScreen()
        yield self.helpMenu
        yield self.helpArea

    def on_mount(self):
        self.add_class("LayoutScreen")

    # se selezionato automaticamente richiama show_topic
    def on_help_menu_topic_selected(self, event: HelpMenu.TopicSelected):
        self.helpArea.show_topic(event.topic)

class EspressioniPage(Screen):
    BINDINGS = [
        Binding("ctrl+w", "back", "Menu", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        self.layout_windows = LayoutScreen_Espressioni()
        yield self.layout_windows
        yield Footer()

    def action_back(self):
        self.app.pop_screen()

    def on_mount(self):
        self.call_after_refresh(self.layout_windows.espressioni.input_area.focus)

class BoleanPage(Screen):
    BINDINGS = [
        Binding("ctrl+w", "back", "Menu", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        self.layout_windows = LayoutScreen_Bolean()
        yield self.layout_windows
        yield Footer()

    def action_back(self):
        self.app.pop_screen()

    def on_mount(self):
        # mette in coda un aziona da fare (foucs)
        self.call_after_refresh(self.layout_windows.bolean.input_area.focus)

class HelpPage(Screen):
    BINDINGS = [
        Binding("ctrl+w", "back", "Menu", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        self.layout_windows = LayoutScreen_Help()
        yield self.layout_windows
        yield Footer()

    def action_back(self):
        self.app.pop_screen()

    def on_mount(self):
        pass

        
class SelectingScreen(Screen):
    BINDINGS = [
        Binding("down", "move_down", "Giù", show=True, priority=True),
        Binding("up", "move_up", "Su", show=True, priority=True),
        Binding("enter", "select_option", "Seleziona", show=True, priority=True),
    ]

    def compose(self) -> ComposeResult:
        with Vertical(classes="selector-body"):
            self.START = Label(titolo())
            yield self.START
            self.selected_index = -1
            self.options = [
                Static(f"[{COLORE_SELETTORE}]Espressioni[/{COLORE_SELETTORE}]"),
                Static(f"[{COLORE_SELETTORE}]Bolean Parser[/{COLORE_SELETTORE}]"),
                Static(f"[{COLORE_SELETTORE}]Help[/{COLORE_SELETTORE}]")
            ]
            for op in self.options:
                yield op
        yield Footer()

    def on_mount(self):
        self.START.add_class("start")
        for op in self.options:
            op.add_class("selector")

    def action_move_down(self):
        if self.selected_index >= 0:
            self.options[self.selected_index].remove_class("focus")
        self.selected_index = (self.selected_index + 1) % len(self.options)
        self.options[self.selected_index].add_class("focus")

    def action_move_up(self):
        if self.selected_index >= 0:
            self.options[self.selected_index].remove_class("focus")
        self.selected_index = (self.selected_index - 1) % len(self.options)
        self.options[self.selected_index].add_class("focus")

    def action_select_option(self):
        if self.selected_index < 0:
            return
        match self.selected_index:
            case 0:
                self.app.push_screen(EspressioniPage())
            case 1:
                self.app.push_screen(BoleanPage())
            case 2:
                self.app.push_screen(HelpPage())


class SelectingApp(App):
    CSS_PATH = "Style.tcss"
    BINDINGS = [
        Binding("ctrl+c", "quit", "Esci", show=True),
    ]

    def on_mount(self):
        self.register_theme(CALC_THEME)
        self.theme = DEFAULT_THEME
        self.push_screen(SelectingScreen())


if __name__ == "__main__":
    SelectingApp().run()