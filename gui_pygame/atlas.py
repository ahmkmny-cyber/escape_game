"""Sprite atlas: slice Green Woods sheets into individual parts and compose scenes.

Sheet layouts were detected by alpha analysis (see contact sheets in temp).
Parts are (x0, y0, x1, y1) boxes with padding; compose_* builds real
1280x720 scenes from parts instead of stretching whole sheets.
"""
import pygame
from . import config

PACK = config.BASE_DIR / "assets" / "pack_greenwoods"

TREES = [
    (1248, 60, 1336, 380),   # 0 tall pine
    (892, 100, 1080, 244),   # 1 wide canopy
    (1104, 68, 1192, 368),   # 2 tall pine
    (688, 92, 848, 252),     # 3 round canopy
    (280, 76, 416, 252),     # 4 round canopy
    (476, 208, 636, 340),    # 5 big bush
    (472, 68, 624, 192),     # 6 canopy
    (128, 96, 236, 228),     # 7 canopy
    (912, 472, 992, 572),    # 8 bush
    (160, 460, 216, 572),    # 9 bush
    (336, 452, 388, 572),    # 10 bush
    (712, 440, 744, 572),    # 11 trunk
    (1092, 500, 1128, 572),  # 12 small bush
    (528, 452, 548, 568),    # 13 sapling
]

CHARACTERS = [
    (292, 216, 316, 272),  # 0 walker candidate A
    (408, 216, 432, 264),  # 1 walker candidate B
    (296, 132, 316, 188),  # 2
    (356, 136, 384, 176),  # 3
    (408, 132, 432, 176),  # 4
    (364, 220, 384, 272),  # 5
    (132, 136, 148, 188),  # 6
    (308, 56, 324, 104),   # 7
    (360, 56, 376, 104),   # 8
]

WALKER_IDX = 0  # change if another character looks better (see contact sheet)

_cache = {}


def _sheet(name):
    if name not in _cache:
        _cache[name] = pygame.image.load(str(PACK / name)).convert_alpha()
    return _cache[name]


def part(name, idx, pad=4):
    boxes = TREES if name == "Trees.png" else CHARACTERS
    x0, y0, x1, y1 = boxes[idx]
    x0 = max(0, x0 - pad)
    y0 = max(0, y0 - pad)
    sheet = _sheet(name)
    x1 = min(sheet.get_width(), x1 + pad)
    y1 = min(sheet.get_height(), y1 + pad)
    return sheet.subsurface((x0, y0, x1 - x0, y1 - y0)).copy()


def scaled(sprite, scale, darken=1.0):
    w, h = sprite.get_size()
    s = pygame.transform.smoothscale(sprite, (max(1, int(w * scale)), max(1, int(h * scale))))
    if darken < 1.0:
        m = pygame.Surface(s.get_size(), pygame.SRCALPHA)
        m.fill((0, 0, 0, int(255 * (1.0 - darken))))
        s = s.copy()
        s.blit(m, (0, 0))
    return s
