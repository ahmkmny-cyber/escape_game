# file music_of_game.py
import pygame
import threading
import time

# تأكيد تهيئة الصوت
if not pygame.mixer.get_init():
    pygame.mixer.init()

# حط مسار ملف الصوت الخاص بموسيقى القائمة الخلفية هنا
MENU_MUSIC_PATH = r"C:\Users\Compu City\Downloads\Game_Background_no_whistle.mp3"

music_thread = None
is_playing = False

def _play_loop():
    global is_playing
    try:
        pygame.mixer.music.load(MENU_MUSIC_PATH)
        # التشغيل في حلقة لا نهائية (-1)
        pygame.mixer.music.play(-1)
        is_playing = True
    except Exception as e:
        print(f"Error loading menu music: {e}")

def start_menu_music():
    """تشغيل موسيقى الخلفية للقائمة الرئيسية إذا لم تكن شغالة"""
    global music_thread, is_playing
    if not is_playing or not pygame.mixer.music.get_busy():
        music_thread = threading.Thread(target=_play_loop, daemon=True)
        music_thread.start()

def stop_menu_music():
    """إيقاف موسيقى القائمة الرئيسية عند بدء أي ليفل"""
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False