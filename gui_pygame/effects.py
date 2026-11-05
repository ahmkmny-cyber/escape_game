import math
import random
import pygame
from . import config


def make_vignette(w, h, strength=180):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    cx, cy = w // 2, h // 2
    maxd = math.hypot(cx, cy)
    for y in range(0, h, 4):
        for x in range(0, w, 4):
            d = math.hypot(x - cx, y - cy) / maxd
            a = int((d ** 2.2) * strength)
            if a > 0:
                surf.fill((0, 0, 0, min(a, strength)), (x, y, 4, 4))
    return surf


class Dust:
    def __init__(self, n=70, w=1280, h=720):
        self.w = w
        self.h = h
        self.p = [
            {
                "x": random.uniform(0, w),
                "y": random.uniform(0, h),
                "s": random.uniform(1, 3),
                "vx": random.uniform(-8, -2),
                "vy": random.uniform(-6, 6),
                "a": random.randint(12, 45),
            }
            for _ in range(n)
        ]

    def update(self, dt):
        for d in self.p:
            d["x"] += d["vx"] * dt
            d["y"] += d["vy"] * dt
            if d["x"] < 0:
                d["x"] = self.w
                d["y"] = random.uniform(0, self.h)
            if d["y"] < 0:
                d["y"] = self.h
            if d["y"] > self.h:
                d["y"] = 0

    def draw(self, surf):
        for d in self.p:
            c = (160, 160, 170, d["a"])
            dot = pygame.Surface((int(d["s"] * 2), int(d["s"] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(dot, c, (int(d["s"]), int(d["s"])), int(d["s"]))
            surf.blit(dot, (d["x"], d["y"]))


class Hotspot:
    """Rusty Lake style clickable point with Limbo glow."""

    def __init__(self, x, y, radius, label, sub):
        self.x = x
        self.y = y
        self.r = radius
        self.label = label
        self.sub = sub
        self.hover = False
        self.pulse = random.uniform(0, 6)

    def contains(self, pos):
        return math.hypot(pos[0] - self.x, pos[1] - self.y) <= self.r + 14

    def draw(self, surf, font, small, solved, flick, time_s):
        self.pulse += 0.05
        x0 = int(self.x)
        y0 = int(self.y)
        glow_r = int(self.r + 10 + math.sin(self.pulse) * 4 + (6 if self.hover else 0))
        base = (80, 200, 120) if solved else ((120, 220, 235) if self.hover else (200, 70, 70))
        # outer glow (additive-ish: 3 translucent circles)
        for i, alpha in ((3, 30), (2, 45), (1, 60)):
            g = pygame.Surface((glow_r * 2 * i, glow_r * 2 * i), pygame.SRCALPHA)
            pygame.draw.circle(g, (*base, alpha), (glow_r * i, glow_r * i), glow_r)
            surf.blit(g, (x0 - glow_r * i, y0 - glow_r * i), special_flags=pygame.BLEND_ADD)
        # terminal body: dark cabinet + screen
        flicker = 0.85 + 0.15 * flick
        body_c = (int(24 * flicker), int(26 * flicker), int(32 * flicker))
        pygame.draw.rect(surf, body_c, (x0 - 52, y0 - 40, 104, 80), border_radius=8)
        pygame.draw.rect(surf, base, (x0 - 52, y0 - 40, 104, 80), 2, border_radius=8)
        scr_c = (15, 30, 25) if solved else (20, 28, 40)
        pygame.draw.rect(surf, scr_c, (x0 - 42, y0 - 30, 84, 48), border_radius=4)
        # scanlines
        for ly in range(y0 - 30, y0 + 18, 6):
            pygame.draw.line(surf, (0, 0, 0, 90), (x0 - 42, ly), (x0 + 42, ly))
        # LED blink
        led_on = (time_s * 2 + x0) % 2 < 1
        pygame.draw.circle(surf, (255, 60, 60) if led_on else (90, 20, 20), (x0 + 38, y0 - 32), 4)
        mark = "✓" if solved else ("?" if not self.hover else "!")
        img = font.render(mark, True, base)
        surf.blit(img, img.get_rect(center=(x0, y0 - 4)))
        lab = small.render(self.label, True, (220, 220, 220) if self.hover else (150, 150, 150))
        lr = lab.get_rect(center=(x0, y0 + 62))
        bg = pygame.Surface((lr.w + 16, lr.h + 8), pygame.SRCALPHA)
        bg.fill((5, 5, 8, 170))
        surf.blit(bg, (lr.x - 8, lr.y - 4))
        surf.blit(lab, lr)
        if self.hover and not solved:
            tip = small.render(self.sub, True, (230, 190, 90))
            surf.blit(tip, tip.get_rect(center=(x0, y0 - 62)))
