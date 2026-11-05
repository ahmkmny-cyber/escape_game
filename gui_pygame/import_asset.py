"""Import any downloaded background into assets/rooms/ (auto resize to 1280x720).
Usage:
  python -m gui_pygame.import_asset "C:/Downloads/horror_lab.jpg" --room 1
  python -m gui_pygame.import_asset "C:/Downloads/ward.png" --room 2
Rooms: 1=server, 2=clinic, 3=orphanage
"""
import argparse
import os
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
from pathlib import Path
import pygame

pygame.init()
pygame.display.set_mode((1, 1))

NAMES = {1: "room01_server.png", 2: "room02_clinic.png", 3: "room03_orphanage.png"}
BASE = Path(__file__).resolve().parent.parent / "assets" / "rooms"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="downloaded image path")
    ap.add_argument("--room", type=int, choices=[1, 2, 3], required=True)
    ap.add_argument("--fit", action="store_true",
                    help="fit whole image (blur-fill bars) instead of cover-crop; best for square packs")
    args = ap.parse_args()
    src = Path(args.src)
    if not src.exists():
        print(f"NOT FOUND: {src}")
        return
    try:
        img = pygame.image.load(str(src)).convert()
    except Exception as e:
        print(f"LOAD FAILED: {e}")
        return
    # cover-crop to 1280x720 (no distortion for any aspect)
    sw, sh = img.get_size()
    if args.fit:
        # fit whole image + dark blurred fill (keeps every detail of square packs)
        scale = min(1280 / sw, 720 / sh)
        nw, nh = int(sw * scale), int(sh * scale)
        small = pygame.transform.smoothscale(img, (nw, nh))
        bg = pygame.transform.smoothscale(img, (1280, 720))
        dark = pygame.Surface((1280, 720), pygame.SRCALPHA)
        dark.fill((5, 5, 12, 170))
        bg.blit(dark, (0, 0))
        bg.blit(small, ((1280 - nw) // 2, (720 - nh) // 2))
        img = bg
    else:
        scale = max(1280 / sw, 720 / sh)
        img = pygame.transform.scale(img, (int(sw * scale), int(sh * scale)))
        x = (img.get_width() - 1280) // 2
        y = (img.get_height() - 720) // 2
        img = img.subsurface((x, y, 1280, 720)).copy()
    # slight dark horror grade so text/hotspots stay readable
    shade = pygame.Surface((1280, 720), pygame.SRCALPHA)
    shade.fill((5, 5, 12, 45))
    img.blit(shade, (0, 0))
    dst = BASE / NAMES[args.room]
    BASE.mkdir(parents=True, exist_ok=True)
    pygame.image.save(img, str(dst))
    print(f"saved -> {dst} ({dst.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
