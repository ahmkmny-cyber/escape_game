from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SCREEN_W = 1280
SCREEN_H = 720
FPS = 60

# Colors (same horror palette as terminal version)
BG = (10, 10, 14)
PANEL = (22, 22, 28)
RED = (178, 34, 34)
LIGHT_RED = (255, 90, 90)
DARK_RED = (120, 20, 20)
WHITE = (235, 235, 235)
GRAY = (150, 150, 150)
DARK_GRAY = (90, 90, 90)
GREEN = (80, 200, 120)
YELLOW = (230, 190, 90)
CYAN = (90, 200, 220)
PURPLE = (180, 120, 220)

# Audio (relative paths - fixes old absolute C:\... paths)
MENU_MUSIC = BASE_DIR / "Game_Background.mp3"
ROOM1_BG = BASE_DIR / "Kill_User_Background.mp3"
ROOM1_VOICE = BASE_DIR / "Kill_User_voiceover.mp3"

# Room background images (PNG/JPG in assets/rooms/, else procedural fallback)
ROOM_BG_IMAGES = {
    1: BASE_DIR / "assets" / "rooms" / "room01_server.png",
    2: BASE_DIR / "assets" / "rooms" / "room02_clinic.png",
    3: BASE_DIR / "assets" / "rooms" / "room03_orphanage.png",
}
# also accept .jpg variant
ROOM_BG_FALLBACK_EXT = ".jpg"

# Walking companion on/off (cartoon art clashes with horror rooms)
SHOW_WALKER = False

# Horror grade applied over room backgrounds (tune these, no re-import needed)
BG_SHADE = 150   # 0-255 dark overlay (higher = darker)
BG_RED = 26      # red tint at edges
GRAIN_ALPHA = 26 # animated film grain strength

# Horror title font switch: HelpMe (ransom-note) / Nosifer (dripping) /
# Eater (melting) / Butcherman (torn) / Creepster (jagged).
# Body/Arabic always Cairo.
TITLE_FONT_FILE = "HelpMe.ttf"

# Game rules (match Kill_User_py.py)
LEVEL_TIME = 15 * 60
WRONG_PENALTY = 30
HINT_PENALTY = 60

def get_font(size=28, bold=False, style="body"):
    """Cairo for body/Arabic, Nosifer (horror) for titles. Fallback to system."""
    import pygame
    if style == "title":
        horror = BASE_DIR / "assets" / "fonts" / TITLE_FONT_FILE
        if horror.exists():
            try:
                return pygame.font.Font(str(horror), size)
            except Exception:
                pass
    cairo = BASE_DIR / "assets" / "fonts" / "Cairo.ttf"
    if cairo.exists():
        try:
            return pygame.font.Font(str(cairo), size)
        except Exception:
            pass
    return pygame.font.SysFont("consolas", size, bold=bold)
