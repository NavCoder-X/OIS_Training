import os
import sys

# Fix per Textual + PyInstaller --onefile su Windows:
# gli handle stdin/stdout vengono sostituiti con oggetti senza fileno(),
# causando un crash al primo keypress nel Windows console driver.
if getattr(sys, 'frozen', False) and sys.platform == 'win32':
    try:
        sys.stdin  = open('CONIN$',  'r', encoding='utf-8', errors='replace')
        sys.stdout = open('CONOUT$', 'w', encoding='utf-8', errors='replace')
        sys.stderr = open('CONOUT$', 'w', encoding='utf-8', errors='replace')
    except Exception:
        pass

# In frozen --onefile, __file__ punta alla cartella temp di estrazione (sys._MEIPASS).
# I file dati (variabili.txt, error.txt, output.txt) vanno scritti accanto all'exe.
if getattr(sys, 'frozen', False):
    PROJECT_ROOT = os.path.dirname(sys.executable)
else:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Tui.Tui import SelectingApp


def main() -> None:
    SelectingApp().run()


if __name__ == "__main__":
    main()