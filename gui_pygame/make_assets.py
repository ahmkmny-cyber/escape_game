"""Generate original CC0 placeholder backgrounds (1280x720) for the 3 rooms."""
import os
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
import random
import math
import pygame

W, H = 1280, 720
OUT = {
    "room01_server": "assets/rooms/room01_server.png",
    "room02_clinic": "assets/rooms/room02_clinic.png",
    "room03_orphanage": "assets/rooms/room03_orphanage.png",
}

pygame.init()
pygame.display.set_mode((1, 1))


def grain(surf, n=5200, alpha=22):
    for _ in range(n):
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        v = random.randint(0, 255)
        surf.set_at((x, y), (v, v, v, alpha))


def vignette(surf, strength=170):
    v = pygame.Surface((W, H), pygame.SRCALPHA)
    cx, cy = W // 2, H // 2
    maxd = math.hypot(cx, cy)
    for y in range(0, H, 6):
        for x in range(0, W, 6):
            d = math.hypot(x - cx, y - cy) / maxd
            a = int((d ** 2.4) * strength)
            if a:
                v.fill((0, 0, 0, min(a, strength)), (x, y, 6, 6))
    surf.blit(v, (0, 0))


def base_gradient(top, bottom, floor_y=560, floor_c=(12, 12, 16)):
    s = pygame.Surface((W, H))
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        pygame.draw.line(s, c, (0, y), (W, y))
    pygame.draw.rect(s, floor_c, (0, floor_y, W, H - floor_y))
    pygame.draw.line(s, (90, 30, 30), (0, floor_y), (W, floor_y), 2)
    return s


def lamp_cone(surf, color=(190, 170, 130), alpha=26):
    cone = pygame.Surface((700, 500), pygame.SRCALPHA)
    pygame.draw.polygon(cone, (*color, alpha), [(270, 0), (430, 0), (620, 500), (80, 500)])
    surf.blit(cone, (W // 2 - 350, 60))
    pygame.draw.rect(surf, (200, 180, 140), (W // 2 - 60, 58, 120, 12), border_radius=4)


def make_server():
    s = base_gradient((16, 18, 26), (34, 26, 30))
    # server cabinets
    for i, x in enumerate([60, 280, 830, 1050]):
        w, h, y = 170, 230, 330
        pygame.draw.rect(s, (16, 18, 24), (x, y, w, h), border_radius=6)
        pygame.draw.rect(s, (110, 30, 30), (x, y, w, h), 2, border_radius=6)
        for k in range(5):
            ly = y + 26 + k * 40
            pygame.draw.rect(s, (28, 32, 42), (x + 14, ly, w - 48, 22), border_radius=3)
            for led in range(3):
                on = random.random() < 0.6
                c = (255, 60, 60) if on else (70, 18, 18)
                if led == 1:
                    c = (80, 200, 120) if on else (20, 60, 30)
                pygame.draw.circle(s, c, (x + 24 + led * 14, ly + 11), 3)
    # cables on floor
    for _ in range(8):
        x0 = random.randint(0, W)
        pygame.draw.arc(s, (10, 10, 12), (x0, 590, 180, 60), 0.2, 2.8, 3)
    # bloody wall code
    font = pygame.font.SysFont("consolas", 34, bold=True)
    txt = font.render("while True:  kill user", True, (200, 50, 50))
    s.blit(txt, txt.get_rect(center=(W // 2, 150)))
    font2 = pygame.font.SysFont("consolas", 22)
    s.blit(font2.render("01001000 01000101 01001100 01000000", True, (90, 90, 90)), (W // 2 - 200, 190))
    lamp_cone(s)
    grain(s)
    vignette(s)
    return s


def make_clinic():
    s = base_gradient((14, 22, 22), (30, 36, 34), floor_c=(16, 20, 20))
    # tile wall strip
    pygame.draw.rect(s, (24, 34, 34), (0, 300, W, 120))
    for x in range(0, W, 64):
        pygame.draw.line(s, (14, 20, 20), (x, 300), (x, 420), 1)
    pygame.draw.line(s, (14, 20, 20), (0, 360), (W, 360), 1)
    # red cross sign
    pygame.draw.rect(s, (120, 25, 25), (W // 2 - 40, 110, 80, 80), border_radius=8)
    pygame.draw.rect(s, (230, 230, 230), (W // 2 - 8, 125, 16, 50))
    pygame.draw.rect(s, (230, 230, 230), (W // 2 - 25, 142, 50, 16))
    # beds silhouettes
    for x in [140, 880]:
        pygame.draw.rect(s, (18, 26, 26), (x, 430, 260, 26), border_radius=6)
        for lx in (x + 20, x + 220):
            pygame.draw.rect(s, (10, 14, 14), (lx, 456, 12, 110))
        pygame.draw.rect(s, (30, 44, 44), (x + 20, 400, 60, 34), border_radius=6)  # pillow
        # monitor glow
        pygame.draw.rect(s, (20, 40, 36), (x + 160, 360, 80, 60), border_radius=4)
        pygame.draw.rect(s, (80, 200, 150), (x + 160, 360, 80, 60), 2, border_radius=4)
        font = pygame.font.SysFont("consolas", 20, bold=True)
        s.blit(font.render("___--___", True, (80, 220, 160)), (x + 168, 380))
    lamp_cone(s, color=(150, 220, 190), alpha=22)
    grain(s)
    vignette(s)
    return s


def make_orphanage():
    s = base_gradient((20, 14, 28), (36, 22, 30), floor_c=(14, 10, 16))
    # moon window
    pygame.draw.rect(s, (16, 12, 24), (W // 2 - 110, 120, 220, 180), border_radius=8)
    pygame.draw.rect(s, (60, 50, 80), (W // 2 - 110, 120, 220, 180), 3, border_radius=8)
    pygame.draw.circle(s, (210, 200, 180), (W // 2 + 40, 170), 34)
    pygame.draw.circle(s, (16, 12, 24), (W // 2 + 52, 162), 34)  # crescent
    pygame.draw.line(s, (60, 50, 80), (W // 2, 120), (W // 2, 300), 2)
    pygame.draw.line(s, (60, 50, 80), (W // 2 - 110, 210), (W // 2 + 110, 210), 2)
    # bunk beds
    for x in [100, 900]:
        for level in (420, 480):
            pygame.draw.rect(s, (22, 16, 28), (x, level, 280, 18), border_radius=5)
            pygame.draw.rect(s, (90, 60, 100), (x, level, 280, 18), 1, border_radius=5)
        for px in (x + 10, x + 258):
            pygame.draw.rect(s, (14, 10, 18), (px, 380, 12, 190))
        # doll eyes glowing
        for _ in range(3):
            ex = x + random.randint(30, 230)
            ey = random.randint(430, 470)
            pygame.draw.circle(s, (220, 60, 60), (ex, ey), 3)
            pygame.draw.circle(s, (220, 60, 60), (ex + 14, ey), 3)
    # scattered toys
    for _ in range(6):
        x, y = random.randint(300, 950), random.randint(590, 660)
        pygame.draw.circle(s, (40, 28, 48), (x, y), random.randint(8, 16))
    lamp_cone(s, color=(170, 140, 200), alpha=20)
    font = pygame.font.SysFont("consolas", 24, bold=True)
    s.blit(font.render("NO CHILD EVER LEFT", True, (170, 60, 70)), (W // 2 - 140, 320))
    grain(s)
    vignette(s)
    return s


makers = {"room01_server": make_server, "room02_clinic": make_clinic, "room03_orphanage": make_orphanage}

for name, fn in makers.items():
    img = fn()
    path = OUT[name]
    pygame.image.save(img, path)
    print(f"saved {path}")
