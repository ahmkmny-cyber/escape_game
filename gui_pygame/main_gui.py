"""Pygame prototype v2: Rusty Lake hotspots + Limbo lighting."""
import math
import random
import sys
import pygame

from . import config
from .audio import AudioManager
from .state import LevelState
from .effects import Dust, Hotspot, make_vignette

STORY_LINES = [
    "In 2023, a programmer named Tarek was working on strange code...",
    "A code that could extract data from places not connected to internet!",
    "Neighbors heard TERRIFYING SCREAMS. Police found Tarek DEAD.",
    "Screen kept printing:  while True:  kill user",
    "You entered the room. Door locked. Lights out.",
    "You have 15 minutes to find the bug. Otherwise SERVER LOCKS FOREVER.",
]

HOTSPOT_DEFS = [
    (250, 360, "MAIN TERMINAL", "inspect code"),
    (1030, 360, "SERVER RACK", "bloody wires"),
    (480, 520, "ABANDONED DESK", "hack desk"),
    (800, 520, "SYSTEM LOGS", "binary lock"),
]


class Button:
    """Horror-skinned button (sliced art, falls back to drawn box)."""

    def __init__(self, rect, text, font, bg=config.PANEL, fg=config.WHITE, icon=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg
        self.icon = icon  # logical icon name from ui_skin.ICON_MAP
        self.hover = False
        self.pressed = False
        self._skin = None
        try:
            from . import ui_skin as _skin
            self._skin = _skin.btn_images()
        except Exception:
            self._skin = None

    def _art(self, w, h, state):
        img = self._skin[state]
        return pygame.transform.smoothscale(img, (w, h))

    def draw(self, surf):
        # drawn horror button (bundle slices had baked-in text, unusable)
        w, h = self.rect.w, self.rect.h
        base_top = (90, 22, 22) if self.pressed else ((140, 30, 30) if self.hover else (58, 16, 16))
        base_bot = (45, 10, 10) if self.pressed else ((80, 16, 16) if self.hover else (30, 8, 8))
        for yy in range(h):
            t = yy / max(1, h - 1)
            c = tuple(int(base_top[i] + (base_bot[i] - base_top[i]) * t) for i in range(3))
            pygame.draw.line(surf, c, (self.rect.x, self.rect.y + yy), (self.rect.x + w - 1, self.rect.y + yy))
        pygame.draw.line(surf, (200, 90, 90), (self.rect.x + 2, self.rect.y + 1), (self.rect.x + w - 3, self.rect.y + 1))
        pygame.draw.rect(surf, (200, 60, 60) if self.hover else (120, 30, 30), self.rect, 2, border_radius=8)
        if self.icon:
            try:
                from . import ui_skin as _skin
                ic = _skin.icon(self.icon, size=26)
                if ic is not None:
                    surf.blit(ic, (self.rect.x + 10, self.rect.centery - 13))
                    img = self.font.render(self.text, True, self.fg)
                    surf.blit(img, (self.rect.x + 44, self.rect.centery - img.get_height() // 2))
                    return
            except Exception:
                pass
        img = self.font.render(self.text, True, self.fg)
        surf.blit(img, img.get_rect(center=self.rect.center))

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            was = self.pressed
            self.pressed = False
            if was and self.rect.collidepoint(event.pos):
                return True
        return False


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
        pygame.display.set_caption("ESCAPE THE NIGHT - Room 01 (Rusty Lake x Limbo)")
        self.clock = pygame.time.Clock()
        self.font_big = config.get_font(54, bold=True, style="title")
        self.font_title = config.get_font(40, bold=True, style="title")
        self.font = config.get_font(28)
        self.font_small = config.get_font(22)
        self.font_code = config.get_font(24)
        self.audio = AudioManager()
        self.scene = "MENU"
        self.level = LevelState()
        self.active_puzzle = None
        self.input_text = ""
        self.msg = ""
        self.msg_color = config.GRAY
        self.story_idx = 0
        self._accum = 0
        self.time_s = 0.0
        self.flick = 1.0
        # presentation animations
        self.menu_t = 0.0
        self.shake = 0.0
        self.flash = 0
        self.flash_color = (255, 60, 60)
        self.story_chars = 0.0
        self.vignette = make_vignette(config.SCREEN_W, config.SCREEN_H)
        self.dust = Dust()
        self.mouse = (config.SCREEN_W // 2, config.SCREEN_H // 2)
        # animated film grain (2 precomputed frames, cheap)
        self._grain = []
        for _ in range(2):
            g = pygame.Surface((config.SCREEN_W // 2, config.SCREEN_H // 2), pygame.SRCALPHA)
            for _ in range(2600):
                x, y = random.randint(0, config.SCREEN_W // 2 - 1), random.randint(0, config.SCREEN_H // 2 - 1)
                v = random.randint(0, 255)
                g.set_at((x, y), (v, v, v, config.GRAIN_ALPHA))
            self._grain.append(pygame.transform.scale(g, (config.SCREEN_W, config.SCREEN_H)))
        self._grain_t = 0.0
        self._grain_i = 0

        cx = config.SCREEN_W // 2
        self.btn_start = Button((cx - 200, 400, 400, 60), "ENTER THE SERVER", self.font)
        self.btn_quit = Button((cx - 200, 475, 400, 60), "QUIT", self.font)
        self.btn_hint = Button((30, 100, 230, 45), "LANTERN HINT (-60s)", self.font_small, icon="hint")
        self.btn_back = Button((140, 618, 220, 45), "BACK TO ROOM", self.font_small, icon="back")
        self.btn_submit = Button((920, 618, 220, 45), "SUBMIT", self.font)
        self.hotspots = [Hotspot(x, y, 46, f"P0{i+1}", sub) for i, (x, y, _, sub) in enumerate(HOTSPOT_DEFS)]
        self.corner = pygame.Rect(590, 600, 100, 60)
        self.room_bg_img = self._load_room_bg(1)
        self.pack_trees = None  # retired: sheets are parts, see atlas.build (menu uses composed strip below)
        self.pack_chars = None
        # walking companion: single character part (not the whole sheet)
        self.walker = self._load_walker() if config.SHOW_WALKER else None
        self.walker_x = 200.0
        self.walker_dir = 1
        self.walker_speed = 90.0
        self.audio.play_menu()

    @staticmethod
    def _load_walker():
        try:
            from . import atlas as _atlas
            spr = _atlas.part("Characters.png", _atlas.WALKER_IDX)
            return pygame.transform.smoothscale(spr, (72, 168))
        except Exception as e:
            print(f"[assets] walker failed: {e}")
            return None

    @staticmethod
    def _load_pack(name, size):
        import os
        p = config.BASE_DIR / "assets" / "pack_greenwoods" / name
        try:
            if os.path.exists(str(p)):
                img = pygame.image.load(str(p)).convert_alpha()
                return pygame.transform.scale(img, size)
        except Exception as e:
            print(f"[assets] pack {name} failed: {e}")
        return None

    @staticmethod
    def _cover(img, tw, th):
        sw, sh = img.get_size()
        scale = max(tw / sw, th / sh)
        img = pygame.transform.scale(img, (int(sw * scale), int(sh * scale)))
        x = (img.get_width() - tw) // 2
        y = (img.get_height() - th) // 2
        return img.subsurface((x, y, tw, th)).copy()

    @staticmethod
    def _load_room_bg(room_number):
        import os
        candidates = [config.ROOM_BG_IMAGES.get(room_number)]
        base = str(candidates[0])
        # try .png then .jpg
        for alt in [base, os.path.splitext(base)[0] + ".jpg"]:
            try:
                if os.path.exists(alt):
                    img = pygame.image.load(alt).convert()
                    # cover-crop to overscan (no distortion) for camera sway
                    return App._cover(img, config.SCREEN_W + 40, config.SCREEN_H + 40)
            except Exception as e:
                print(f"[assets] failed to load {alt}: {e}")
        return None

    def run(self, max_frames=0):
        frames = 0
        while True:
            dt = self.clock.tick(config.FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self.on_event(event)
            self.update(dt)
            self.draw()
            pygame.display.flip()
            frames += 1
            if max_frames and frames >= max_frames:
                return

    # ---------- logic (unchanged rules) ----------
    def update(self, dt):
        self.time_s += dt
        self.menu_t += dt
        if self.shake > 0:
            self.shake = max(0.0, self.shake - dt * 30)
        if self.flash > 0:
            self.flash = max(0, self.flash - int(dt * 400))
        # story typewriter (~45 chars/sec)
        if self.scene == "STORY" and self.story_idx < len(STORY_LINES):
            self.story_chars += dt * 45
        # fluorescent flicker: mostly 1.0 with random dips
        if random.random() < 0.06:
            self.flick = random.uniform(0.55, 0.9)
        else:
            self.flick += (1.0 - self.flick) * min(1.0, dt * 8)
        self.dust.update(dt)
        # walker patrol (ROOM only)
        if self.scene == "ROOM" and getattr(self, "walker", None) is not None:
            self.walker_x += self.walker_dir * self.walker_speed * dt
            if self.walker_x > 1020:
                self.walker_x = 1020
                self.walker_dir = -1
            if self.walker_x < 140:
                self.walker_x = 140
                self.walker_dir = 1
        if self.scene in ("ROOM", "PUZZLE") and not self.level.over and not self.level.won:
            self._accum += dt
            if self._accum >= 1.0:
                self._accum = 0
                self.level.remaining -= 1
                if self.level.remaining <= 0:
                    self.level.remaining = 0
                    self.level.over = True
                    self.msg = "TIME'S UP - SYSTEM LOCKED"
                    self.msg_color = config.LIGHT_RED

    def on_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.mouse = event.pos
            if self.scene == "ROOM":
                for h in self.hotspots:
                    h.hover = h.contains(event.pos)
        if self.scene == "MENU":
            if self.btn_start.handle(event):
                self.scene = "STORY"
                self.story_idx = 0
                self.audio.stop_all()
                self.audio.play_room_bg()
                self.audio.play_voiceover()
            if self.btn_quit.handle(event):
                pygame.quit()
                sys.exit()
        elif self.scene == "STORY":
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.advance_story()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.advance_story()
        elif self.scene == "ROOM":
            if self.btn_hint.handle(event):
                self.use_hint()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, h in enumerate(self.hotspots):
                    if h.contains(event.pos):
                        self.active_puzzle = self.level.puzzles[i]
                        self.input_text = ""
                        self.msg = ""
                        self.scene = "PUZZLE"
                        break
                if self.corner.collidepoint(event.pos):
                    self.msg = "NOTE: 4-bit slots [8-4-2-1]. 3 = 0 0 1 1. Memorize it."
                    self.msg_color = config.YELLOW
        elif self.scene == "PUZZLE":
            if self.btn_back.handle(event):
                self.scene = "ROOM"
                self.msg = ""
            if self.btn_submit.handle(event):
                self.submit_answer()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "ROOM"
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.submit_answer()
                else:
                    ch = event.unicode
                    if ch and len(self.input_text) < 24 and (ch.isalnum() or ch in "_- "):
                        self.input_text += ch

    def advance_story(self):
        # first ENTER completes typewriter line, second advances
        cur = STORY_LINES[self.story_idx] if self.story_idx < len(STORY_LINES) else ""
        if self.story_chars < len(cur):
            self.story_chars = float(len(cur))
            return
        self.story_idx += 1
        self.story_chars = 0.0
        if self.story_idx >= len(STORY_LINES):
            self.scene = "ROOM"

    def submit_answer(self):
        p = self.active_puzzle
        if not p:
            return
        ans = self.input_text.strip()
        ok = (ans == p.answer) if p.id == 1 else (ans.upper() == p.answer.upper())
        if ok:
            p.solved = True
            self.msg = f"PUZZLE {p.id:02d} SOLVED!"
            self.msg_color = config.GREEN
            self.flash = 90
            self.flash_color = (80, 200, 120)
            if self.level.check_win():
                self.msg = "LEVEL 01 CLEARED - BADGE: SILVER"
        else:
            self.level.apply_penalty(config.WRONG_PENALTY)
            self.msg = f"WRONG! -{config.WRONG_PENALTY}s penalty"
            self.msg_color = config.LIGHT_RED
            self.shake = 12.0
            self.flash = 120
            self.flash_color = (255, 60, 60)

    def use_hint(self):
        if self.level.hint_used:
            self.msg = "LANTERN ALREADY USED"
            self.msg_color = config.YELLOW
            return
        unsolved = [p for p in self.level.puzzles if not p.solved]
        if not unsolved:
            return
        p = unsolved[0]
        self.level.hint_used = True
        self.level.apply_penalty(config.HINT_PENALTY)
        self.msg = f"HINT P{p.id}: {p.hint}"
        self.msg_color = config.YELLOW

    # ---------- draw ----------
    def draw(self):
        s = self.screen
        s.fill((5, 5, 8))
        self._grain_t += 1 / max(1, config.FPS)
        if self._grain_t > 0.12:
            self._grain_t = 0.0
            self._grain_i ^= 1
        if self.scene == "MENU":
            self.draw_menu_bg(s)
            self.draw_menu(s)
        elif self.scene == "STORY":
            self.draw_room_bg(s, dim=0.75)
            self.draw_story(s)
        elif self.scene == "ROOM":
            self.draw_room_bg(s, dim=1.0)
            self.draw_hud(s)
            self.draw_hotspots(s)
        elif self.scene == "PUZZLE":
            self.draw_room_bg(s, dim=0.45)
            self.draw_hud(s)
            self.draw_puzzle_modal(s)
        self.dust.draw(s)
        s.blit(self._grain[self._grain_i], (0, 0))
        s.blit(self.vignette, (0, 0))
        if self.flash > 0:
            ov = pygame.Surface((config.SCREEN_W, config.SCREEN_H), pygame.SRCALPHA)
            ov.fill((*self.flash_color, min(self.flash, 110)))
            s.blit(ov, (0, 0))

    def draw_room_bg(self, s, dim=1.0):
        import math as _m
        W, H = config.SCREEN_W, config.SCREEN_H
        f = self.flick * dim
        sway = _m.sin(self.time_s * 0.3) * 10  # slow camera drift for presentation
        bob = _m.cos(self.time_s * 0.23) * 8
        shx = (random.uniform(-1, 1) * self.shake) if self.shake > 0 else 0
        shy = (random.uniform(-1, 1) * self.shake) if self.shake > 0 else 0
        if getattr(self, "room_bg_img", None) is not None:
            # real image + horror grade + flicker on top
            s.blit(self.room_bg_img, (-20 + sway + shx, -20 + bob + shy))
            shade = pygame.Surface((W, H), pygame.SRCALPHA)
            shade.fill((5, 5, 12, int(config.BG_SHADE - 60 * f)))
            s.blit(shade, (0, 0))
            red = pygame.Surface((W, H), pygame.SRCALPHA)
            red.fill((120, 10, 10, config.BG_RED))
            s.blit(red, (0, 0))
            s.blit(self.vignette, (0, 0))
        else:
            # wall gradient
            for y in range(80, H, 8):
                t = (y - 80) / (H - 80)
                c = (int((18 + t * 14) * f), int((20 + t * 12) * f), int((28 + t * 10) * f))
                pygame.draw.rect(s, c, (0, y, W, 8))
            # floor
            pygame.draw.rect(s, (int(12 * f), int(12 * f), int(16 * f)), (0, 560, W, H - 560))
            pygame.draw.line(s, (int(90 * f), int(30 * f), int(30 * f)), (0, 560), (W, 560), 2)
            # server cabinets silhouettes
            for i, x in enumerate([60, 1050, 420, 740]):
                w, h = 170, 220
                y = 340 if i < 2 else 380
                pygame.draw.rect(s, (int(16 * f), int(18 * f), int(24 * f)), (x, y, w, h), border_radius=6)
                pygame.draw.rect(s, (int(70 * f), int(25 * f), int(25 * f)), (x, y, w, h), 2, border_radius=6)
                for k in range(4):
                    ly = y + 30 + k * 45
                    on = (self.time_s * 1.5 + i + k) % 2 < 1
                    pygame.draw.circle(s, (255, 60, 60) if on else (70, 18, 18), (x + w - 22, ly), 4)
                    pygame.draw.rect(s, (int(30 * f), int(34 * f), int(44 * f)), (x + 16, ly - 8, w - 50, 16), border_radius=3)
        # ceiling lamp cone
        cone = pygame.Surface((700, 500), pygame.SRCALPHA)
        pygame.draw.polygon(cone, (190, 170, 130, int(26 * f)), [(270, 0), (430, 0), (620, 500), (80, 500)])
        s.blit(cone, (W // 2 - 350, 80))
        pygame.draw.rect(s, (int(200 * f), int(180 * f), int(140 * f)), (W // 2 - 60, 78, 120, 12), border_radius=4)
        # bloody code on wall
        code = self.font_small.render("while True:  kill user", True, (int(200 * f), int(50 * f), int(50 * f)))
        s.blit(code, code.get_rect(center=(W // 2, 150)))
        # mouse lantern glow (Limbo light around cursor)
        mx, my = self.mouse
        glow = pygame.Surface((360, 360), pygame.SRCALPHA)
        pygame.draw.circle(glow, (150, 140, 110, 28), (180, 180), 170)
        pygame.draw.circle(glow, (150, 140, 110, 40), (180, 180), 110)
        s.blit(glow, (mx - 180, my - 180), special_flags=pygame.BLEND_ADD)

    def _blit_panel(self, s, rect):
        try:
            from . import ui_skin as _skin
            for img, pos in _skin.nine_slice(_skin.panel_big(), rect, margin=14):
                s.blit(img, pos)
            return True
        except Exception:
            pygame.draw.rect(s, (14, 14, 20), rect, border_radius=12)
            return False

    def draw_menu_bg(self, s):
        W, H = config.SCREEN_W, config.SCREEN_H
        for y in range(0, H, 8):
            t = y / H
            c = (int(8 + t * 10), int(6 + t * 6), int(10 + t * 8))
            pygame.draw.rect(s, c, (0, y, W, 8))
        # faint red glow behind title
        glow = pygame.Surface((800, 300), pygame.SRCALPHA)
        pygame.draw.ellipse(glow, (150, 20, 20, 40), (0, 0, 800, 300))
        s.blit(glow, (W // 2 - 400, 60))

    def draw_menu(self, s):
        import math as _m
        # entrance slide + flickering title
        slide = int(max(0, 240 - self.menu_t * 420))
        jx = random.randint(-2, 2) if random.random() < 0.08 else 0
        self._blit_panel(s, (config.SCREEN_W // 2 - 360, 115 + slide, 720, 150))
        t = self.font_big.render("ESCAPE THE NIGHT", True, config.RED)
        s.blit(t, t.get_rect(center=(config.SCREEN_W // 2 + jx, 175 + slide)))
        sub = self.font.render("KILL_USER.PY - Server Room", True, config.GRAY)
        s.blit(sub, sub.get_rect(center=(config.SCREEN_W // 2, 232 + slide)))
        info = self.font_small.render("Click a glowing terminal. Solve 4 puzzles before 15:00.", True, config.GRAY)
        s.blit(info, info.get_rect(center=(config.SCREEN_W // 2, 320)))
        for b in (self.btn_start, self.btn_quit):
            old = b.rect.y
            b.rect.y = old + slide
            b.draw(s)
            b.rect.y = old

    def draw_story(self, s):
        # dialogue box (skinned panel)
        self._blit_panel(s, (50, 95, config.SCREEN_W - 100, 430))
        title = self.font.render("CASE FILE - TAREK (ENTER to continue)", True, config.RED)
        s.blit(title, (80, 115))
        y = 180
        for i in range(min(self.story_idx + 1, len(STORY_LINES))):
            line = STORY_LINES[i]
            if i == self.story_idx:
                line = line[: int(self.story_chars)]  # typewriter
            s.blit(self.font_small.render(line, True, config.WHITE), (80, y))
            y += 45
        nxt = self.font_small.render(f"[{self.story_idx + 1}/{len(STORY_LINES)}] ENTER / CLICK...", True, config.GRAY)
        s.blit(nxt, (80, 610))

    def draw_hud(self, s):
        pygame.draw.rect(s, (12, 12, 16, 220), (0, 0, config.SCREEN_W, 80))
        pygame.draw.line(s, config.RED, (0, 80), (config.SCREEN_W, 80), 2)
        s.blit(self.font.render("ROOM 01 | LEVEL 01", True, config.WHITE), (30, 14))
        tcol = config.LIGHT_RED if self.level.remaining < 120 else config.WHITE
        # urgent blink under 60s
        if self.level.remaining < 60 and int(self.time_s * 2) % 2 == 0:
            tcol = config.RED
        try:
            from . import ui_skin as _skin
            _clk = _skin.icon("clock", size=30)
            if _clk is not None:
                s.blit(_clk, (500, 12))
                s.blit(self.font.render(f"{self.level.time_str}", True, tcol), (538, 14))
            else:
                raise RuntimeError
        except Exception:
            s.blit(self.font.render(f"TIME {self.level.time_str}", True, tcol), (500, 14))
        # draining timer bar (15:00 -> 0)
        frac = max(0.0, self.level.remaining / float(15 * 60))
        pygame.draw.rect(s, (40, 20, 20), (500, 52, 220, 12), border_radius=6)
        bar_c = config.GREEN if frac > 0.5 else (config.YELLOW if frac > 0.2 else config.RED)
        pygame.draw.rect(s, bar_c, (500, 52, int(220 * frac), 12), border_radius=6)
        htxt = "LANTERN: EMPTY" if self.level.hint_used else "LANTERN: READY"
        s.blit(self.font_small.render(htxt, True, config.YELLOW), (920, 22))
        marks = "  ".join("✓" if p.solved else "·" for p in self.level.puzzles)
        s.blit(self.font_small.render(f"[{marks}]", True, config.GRAY), (760, 48))

    def draw_hotspots(self, s):
        import math as _m
        t = self.font.render("The server hums. Something watches. Choose a terminal:", True, config.CYAN)
        s.blit(t, (300, 100))
        for i, h in enumerate(self.hotspots):
            solved = self.level.puzzles[i].solved
            if not hasattr(h, "base_y"):
                h.base_y = h.y
            h.y = h.base_y + _m.sin(self.time_s * 1.6 + i * 1.3) * 4  # bounded float
            h.draw(s, self.font, self.font_small, solved, self.flick, self.time_s)
            names = ["MAIN TERMINAL", "SERVER RACK", "ABANDONED DESK", "SYSTEM LOGS"]
            lab = self.font_small.render(names[i], True, config.GRAY)
            s.blit(lab, lab.get_rect(center=(h.x, h.y + 84)))
        # dark corner clue (Rusty Lake hidden note)
        pygame.draw.rect(s, (20, 20, 26), self.corner, border_radius=6)
        pygame.draw.rect(s, config.YELLOW if self.corner.collidepoint(self.mouse) else config.DARK_GRAY, self.corner, 2, border_radius=6)
        note = self.font_small.render("NOTE ?", True, config.YELLOW)
        s.blit(note, note.get_rect(center=self.corner.center))
        self.btn_hint.draw(s)
        # walking companion (single character part, not whole sheet)
        if getattr(self, "walker", None) is not None:
            import math as _m2
            bob = int(abs(_m2.sin(self.time_s * 6)) * 6)
            spr = self.walker if self.walker_dir > 0 else pygame.transform.flip(self.walker, True, False)
            # shadow
            sh = pygame.Surface((64, 14), pygame.SRCALPHA)
            pygame.draw.ellipse(sh, (0, 0, 0, 120), (0, 0, 64, 14))
            sw = spr.get_width()
            s.blit(sh, (self.walker_x - 32, 668))
            s.blit(spr, (self.walker_x - sw // 2, 500 - bob))
        if self.level.won:
            self._blit_panel(s, (config.SCREEN_W // 2 - 330, 545, 660, 70))
            w = self.font.render("LEVEL 01 CLEARED - BADGE: SILVER", True, config.GREEN)
            s.blit(w, w.get_rect(center=(config.SCREEN_W // 2, 582)))
        if self.level.over:
            self._blit_panel(s, (config.SCREEN_W // 2 - 330, 545, 660, 70))
            w = self.font.render("TIME'S UP - SYSTEM LOCKED", True, config.LIGHT_RED)
            s.blit(w, w.get_rect(center=(config.SCREEN_W // 2, 582)))
        if self.msg:
            m = self.font_small.render(self.msg[:100], True, self.msg_color)
            s.blit(m, (30, 660))

    def draw_puzzle_modal(self, s):
        p = self.active_puzzle
        # skinned frame (nine-slice panel art, fallback to drawn box)
        mw, mh = 1120, 560
        mx, my = (config.SCREEN_W - mw) // 2, 110
        try:
            from . import ui_skin as _skin
            for img, pos in _skin.nine_slice(_skin.panel_big(), (mx, my, mw, mh), margin=14):
                s.blit(img, pos)
        except Exception:
            pygame.draw.rect(s, (14, 14, 20), (mx, my, mw, mh), border_radius=12)
        glow_c = config.GREEN if p and p.solved else config.RED
        pygame.draw.rect(s, glow_c, (mx, my, mw, mh), 2, border_radius=12)
        if not p:
            return
        s.blit(self.font_title.render(p.title, True, config.RED), (mx + 40, my + 20))
        y = my + 65
        for line in p.prompt_lines:
            s.blit(self.font_small.render(line, True, config.WHITE), (mx + 40, y))
            y += 30
        y += 8
        s.blit(self.font_small.render("Code:", True, config.YELLOW), (mx + 40, y))
        y += 30
        for c in p.code_lines:
            s.blit(self.font_code.render("   " + c, True, (170, 170, 180)), (mx + 40, y))
            y += 30
        pygame.draw.rect(s, config.WHITE, (mx + 40, my + mh - 110, 660, 48), 2, border_radius=6)
        txt = self.font.render(self.input_text + ("_" if int(self.time_s * 2) % 2 == 0 else " "), True, config.WHITE)
        s.blit(txt, (mx + 55, my + mh - 102))
        # move buttons into modal coords
        self.btn_submit.rect.topleft = (mx + 730, my + mh - 110)
        self.btn_back.rect.topleft = (mx + 40, my + mh - 48) if False else self.btn_back.rect.topleft
        self.btn_submit.draw(s)
        # back button fixed bottom-left of modal
        back_rect = pygame.Rect(mx + 40, my + mh - 52, 220, 40)
        old = self.btn_back.rect
        self.btn_back.rect = back_rect
        self.btn_back.text = "BACK (ESC)"
        self.btn_back.draw(s)
        self.btn_back.rect = old
        if self.msg:
            m = self.font_small.render(self.msg[:95], True, self.msg_color)
            s.blit(m, (mx + 300, my + mh - 42))


def main():
    App().run()


if __name__ == "__main__":
    main()
