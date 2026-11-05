"""Clean rebuild: consistent dark-silhouette room backgrounds (no photos).
Usage:  python -m gui_pygame.build_room_bg
Saves room01/02/03 into assets/rooms/.
"""
import os
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
import math
import random
import pygame

from . import config

W, H = 1280, 720

pygame.init()
pygame.display.set_mode((1, 1))
random.seed(7)


def base(top, bottom, floor_y=560, floor_c=(10, 10, 13)):
    s = pygame.Surface((W, H))
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        pygame.draw.line(s, c, (0, y), (W, y))
    pygame.draw.rect(s, floor_c, (0, floor_y, W, H - floor_y))
    return s


def fog(s, bands=((300, 60), (420, 90), (520, 70)), alpha=16):
    for y, h in bands:
        f = pygame.Surface((W, h * 2), pygame.SRCALPHA)
        for i in range(6):
            pygame.draw.ellipse(f, (140, 150, 160, alpha), (80 * i - 40, 0, W - 160 * i + 200, h * 2))
        s.blit(f, (0, y - h // 2))


def finish(s, red_glow=False):
    vg = pygame.Surface((W, H), pygame.SRCALPHA)
    cx, cy = W // 2, H // 2
    maxd = math.hypot(cx, cy)
    for y in range(0, H, 6):
        for x in range(0, W, 6):
            d = math.hypot(x - cx, y - cy) / maxd
            a = int((d ** 2.4) * 175)
            if a:
                vg.fill((0, 0, 0, min(a, 175)), (x, y, 6, 6))
    s.blit(vg, (0, 0))
    if red_glow:
        g = pygame.Surface((W, H), pygame.SRCALPHA)
        pygame.draw.ellipse(g, (150, 15, 15, 30), (W // 2 - 420, 120, 840, 480), 60)
        s.blit(g, (0, 0))
    return s


def leds(s, x, y, n=4):
    for k in range(n):
        on = random.random() < 0.55
        c = (255, 60, 60) if on else (80, 20, 20)
        if k % 3 == 2:
            c = (80, 200, 130) if on else (20, 60, 35)
        pygame.draw.circle(s, c, (x + k * 13, y), 3)


def room_server():
    s = base((8, 10, 18), (20, 16, 22))
    # back rack row (dark)
    for x in (90, 320, 870, 1100):
        pygame.draw.rect(s, (13, 15, 21), (x, 300, 150, 240))
        pygame.draw.rect(s, (60, 22, 22), (x, 300, 150, 240), 2)
        for k in range(5):
            ly = 322 + k * 44
            pygame.draw.rect(s, (22, 26, 34), (x + 12, ly, 126, 26), border_radius=3)
            leds(s, x + 24, ly + 13)
    # cables
    for _ in range(7):
        x0 = random.randint(60, W - 200)
        pygame.draw.arc(s, (8, 8, 10), (x0, 560, 170, 70), 0.3, 2.7, 3)
    # wall code
    font = pygame.font.SysFont("consolas", 30, bold=True)
    txt = font.render("while True:  kill user", True, (170, 45, 45))
    s.blit(txt, txt.get_rect(center=(W // 2, 140)))
    # lamp cone
    cone = pygame.Surface((640, 460), pygame.SRCALPHA)
    pygame.draw.polygon(cone, (190, 170, 130, 22), [(250, 0), (390, 0), (560, 460), (80, 460)])
    s.blit(cone, (W // 2 - 320, 60))
    fog(s)
    return finish(s, red_glow=True)


def room_clinic():
    s = base((9, 16, 17), (18, 26, 25))
    # tile strip
    pygame.draw.rect(s, (18, 28, 28), (0, 290, W, 110))
    for x in range(0, W, 64):
        pygame.draw.line(s, (10, 16, 16), (x, 290), (x, 400), 1)
    pygame.draw.line(s, (10, 16, 16), (0, 345), (W, 345), 1)
    # cross sign
    pygame.draw.rect(s, (110, 22, 22), (W // 2 - 36, 100, 72, 72), border_radius=8)
    pygame.draw.rect(s, (225, 225, 225), (W // 2 - 7, 114, 14, 44))
    pygame.draw.rect(s, (225, 225, 225), (W // 2 - 22, 129, 44, 14))
    # beds + monitors
    for x in (150, 880):
        pygame.draw.rect(s, (14, 22, 22), (x, 430, 250, 24), border_radius=6)
        for lx in (x + 16, x + 222):
            pygame.draw.rect(s, (8, 12, 12), (lx, 454, 12, 110))
        pygame.draw.rect(s, (24, 38, 38), (x + 18, 402, 56, 30), border_radius=6)
        pygame.draw.rect(s, (16, 34, 30), (x + 158, 358, 78, 58), border_radius=4)
        pygame.draw.rect(s, (70, 180, 140), (x + 158, 358, 78, 58), 2, border_radius=4)
        pygame.draw.lines(s, (80, 220, 160), False,
                          [(x + 164, 390), (x + 178, 390), (x + 184, 372), (x + 192, 400), (x + 206, 380), (x + 230, 380)], 2)
    fog(s, alpha=20)
    return finish(s)


def room_orphanage():
    s = base((14, 9, 20), (26, 15, 22))
    # moon window
    pygame.draw.rect(s, (12, 9, 18), (W // 2 - 105, 110, 210, 170), border_radius=8)
    pygame.draw.rect(s, (55, 45, 70), (W // 2 - 105, 110, 210, 170), 3, border_radius=8)
    pygame.draw.circle(s, (205, 195, 175), (W // 2 + 38, 160), 32)
    pygame.draw.circle(s, (12, 9, 18), (W // 2 + 50, 152), 32)
    pygame.draw.line(s, (55, 45, 70), (W // 2, 110), (W // 2, 280), 2)
    pygame.draw.line(s, (55, 45, 70), (W // 2 - 105, 195), (W // 2 + 105, 195), 2)
    # bunk beds
    for x in (110, 890):
        for level in (420, 482):
            pygame.draw.rect(s, (18, 13, 24), (x, level, 280, 16), border_radius=5)
            pygame.draw.rect(s, (80, 55, 90), (x, level, 280, 16), 1, border_radius=5)
        for px in (x + 10, x + 258):
            pygame.draw.rect(s, (11, 8, 15), (px, 380, 12, 190))
        for _ in range(2):  # doll eyes
            ex, ey = x + random.randint(40, 210), random.randint(430, 470)
            pygame.draw.circle(s, (210, 50, 50), (ex, ey), 3)
            pygame.draw.circle(s, (210, 50, 50), (ex + 13, ey), 3)
    font = pygame.font.SysFont("consolas", 22, bold=True)
    s.blit(font.render("NO CHILD EVER LEFT", True, (150, 55, 65)), (W // 2 - 130, 300))
    fog(s, alpha=22)
    return finish(s, red_glow=True)


def main():
    for name, fn in (("room01_server", room_server), ("room02_clinic", room_clinic),
                     ("room03_orphanage", room_orphanage)):
        img = fn()
        dst = config.BASE_DIR / "assets" / "rooms" / f"{name}.png"
        pygame.image.save(img, str(dst))
        print(f"saved -> {dst} ({dst.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
