import pygame
from . import config


class AudioManager:
    """Separate channels: 0=background loop, 1=voiceover once."""

    def __init__(self):
        self.ok = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            self.bg = pygame.mixer.Channel(0)
            self.voice = pygame.mixer.Channel(1)
            self.ok = True
        except Exception as e:
            print(f"[audio] mixer init failed: {e}")

    def _play(self, channel, path, loops=0):
        if not self.ok:
            return
        try:
            if not path.exists():
                print(f"[audio] missing: {path.name}")
                return
            sound = pygame.mixer.Sound(str(path))
            channel.play(sound, loops=loops)
        except Exception as e:
            print(f"[audio] play failed {path.name}: {e}")

    def play_menu(self):
        self._play(self.bg, config.MENU_MUSIC, loops=-1)

    def play_room_bg(self):
        self._play(self.bg, config.ROOM1_BG, loops=-1)

    def play_voiceover(self):
        self._play(self.voice, config.ROOM1_VOICE, loops=0)

    def stop_all(self):
        try:
            pygame.mixer.stop()
        except Exception:
            pass
