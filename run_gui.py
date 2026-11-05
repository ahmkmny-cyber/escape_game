"""Direct launcher: run with  python run_gui.py  from any folder."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from gui_pygame.main_gui import main

if __name__ == "__main__":
    main()
