# file dar_al_noor.py
import os
import time
import threading
import sys
from player_data import update_room_badge, get_player_data
import pygame
import random
#1014
# COLORS
LIGHT_RED = "\033[91m"
RED = "\033[31m"
DARK_RED = "\033[2;31m"
WHITE = "\033[97m"
GRAY = "\033[90m"
import os
import time
import threading
import sys
from player_data import update_room_badge, get_player_data
from music_of_game import stop_menu_music

import pygame

pygame.mixer.init()

sound1 = r"C:\Users\Compu City\Downloads\Dar El-Noor Voiceover no wistle.mp3"
sound2 = r"C:\Users\Compu City\Downloads\Dar_ELnoor_Background_no_whistle.mp3"
# COLORS
LIGHT_RED = "\033[91m"
RED = "\033[31m"
DARK_RED = "\033[2;31m"
WHITE = "\033[97m"
GRAY = "\033[90m"
PURPLE = "\033[95m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BLINK = "\033[5m"
BOLD = "\033[1m"

# الألوان الخاصة بدار النور الملعونة
R = "\033[91m"  # أحمر ساطع (دموي)
B = "\033[31m"  # أحمر مظلم
P = "\033[95m"  # بنفسجي الأرواح والدمى
Y = "\033[93m"  # أصفر تحذيري
CYAN = "\033[96m"  # سيان خافت
D = "\033[90m"  # رمادي مظلم
GREEN = "\033[92m"  # أخضر الشفرات solved
RESET = "\033[0m"
# GAME VARIABLES
remaining_seconds = 15 * 60
hint_used = False
puzzles_solved = [False, False, False,False]
timer_running = False

# CLEAR SCREEN
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# TYPE TEXT EFFECT
def type_text(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# INTRO SCREEN
def intro_screen():
    clear_screen()
    for i in range(6):
        clear_screen()
        if i % 2 == 0:
            print(f"""{RED}{BOLD}
             ██████╗  █████╗ ██████╗     █████╗ ██╗     ███╗   ██╗ ██████╗  ██████╗ ██╗██xFF╗
             ██╔══██╗██╔══██╗██╔══██╗   ██╔══██╗██║     ████╗  ██║██╔═══██╗██╔═══██╗██║██╔╝
             ██║  ██║███████║██████╔╝   ███████║██║     ██╔██╗ ██║██║   ██║██║   ██║█████╗  
             ██║  ██║██╔══██║██╔══██╗   ██╔══██║██║     ██║╚██╗██║██║   ██║██║   ██║██╔══╝  
             ██████╔╝██║  ██║██║  ██║   ██║  ██║███████╗██║ ╚████║╚██████╔╝╚██████╔╝███████╗
             ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝
            \n                 DAR_AL_NOOR.PY - THE FORGOTTEN ORPHANAGE\n{RESET}""")
        else:
            print(f"""{DARK_RED}{BOLD}\n
            
                        [ ORPHANAGE RECORD EXPIRED ]
                        [ DOLLS EYES OPENED ]
                        [ NO CHILD EVER LEFT ] 
                        \n{RESET}""")
        time.sleep(0.5)
    clear_screen()

def play_sound2_only():
    try:
        # استبدلي 'sound2.mp3' باسم الملف أو الكود اللي بيشغل ساوند 2 عندك بالظبط
        pygame.mixer.music.load(sound2)  
        pygame.mixer.music.play(-1) # -1 عشان يفضل يعيد الباك جراوند
    except Exception as e:
        print(f"Error playing background sound: {e}")

def play_background_music():
    pygame.mixer.music.load(sound1)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.load(sound2)
    pygame.mixer.music.play(-1)

# رفع الدالة لتصبح Global ليتمكن menu.py من استيرادها
def stop_background_music():
    pygame.mixer.music.stop()    

# STORY
def play_story():
    stop_menu_music()

    # ================= SOUND =================
    music_thread = threading.Thread(
        target=play_background_music,
        daemon=True)
    music_thread.start()

    # ================= STORY =================
    print(f"""{RED}{BOLD}

    ╔══════════════════════════════════════════════════╗
    ║                  DAR AL NOOR                     ║
    ╚══════════════════════════════════════════════════╝

    {RESET}""")
    time.sleep(0.1)
    type_text(
        f"\n{GRAY}Dar Al Noor used to take in children who had no one to care for"
        f"them.{RESET}\n",0.045,)
    time.sleep(0.2)
    type_text(f"{GRAY}In 1975, the director, {RED}{BOLD}Mr. Saleh{RESET}{GRAY}, started"
        f"telling people that\nthe children were being adopted by families in"
        f"faraway countries.{RESET}\n",0.045,)
    time.sleep(0.45)
    type_text(f"{YELLOW}But the truth was much darker...{RESET}\n", 0.045)
    time.sleep(0.35)
    type_text(f"{RED}{BOLD}NO CHILD EVER LEFT THE ORPHANAGE.{RESET}\n", 0.038)
    time.sleep(0.35)
    type_text(
        f"{WHITE}The beds were found perfectly made. Under each pillow was a small"
        f"doll\nwith a child's name on it.{RESET}\n",0.055,)
    time.sleep(0.3)
    type_text(
        f"{GRAY}And every night, the children still sing the lullaby Mr. Saleh used"
        f"to sing to them...\n{RED}But now, they sing it slowly... and in a"
        f"frightening way.{RESET}\n",0.025,)
    time.sleep(0.35)
    type_text(
        f"{GRAY}You enter the orphanage dormitory. The door suddenly locks behind"
        f"you.\nThen, all the dolls slowly open their eyes.{RESET}\n",
        0.055,)
    time.sleep(0.45)
    type_text(
        f"{PURPLE}A little child whispers: 'We need families... Which one of you will"
        f"stay with us?'{RESET}\n",
        0.045,)
    time.sleep(0.4)
    type_text(
        f"{RED}{BOLD}You have 15 minutes to discover the truth about what happened to"
        f"the children\nand call each child by their real name.{RESET}\n",
        0.055,)
    time.sleep(0.6)
    type_text(
        f"{RED}If you fail... The orphanage will take what it is missing from"
        f"you.{RESET}\n",
        0.052,)
    time.sleep(0.6)
    input(f"\n{YELLOW}Press ENTER to face the dormitory...{RESET}")

# LEVEL START
def level_start(username):
    global timer_running
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  LEVEL 01                        ║
    ║               THE DORMITORY                      ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}The eerie lullaby echoes through the cold room...{RESET}", 0.03)
    type_text(f"{RED}You have 15 minutes before you become part of the orphanage forever.{RESET}\n", 0.03)
    input(f"{WHITE}Press ENTER to continue...{RESET}")
    start_timer()
    return game_loop(username)

# TIMER
def timer_thread():
    global remaining_seconds
    global timer_running
    while timer_running and remaining_seconds > 0:
        time.sleep(1)
        if timer_running:
            remaining_seconds -= 1

def start_timer():
    global timer_running
    timer_running = True
    thread = threading.Thread(target=timer_thread, daemon=True)
    thread.start()

def get_time():
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# HEADER
def show_header():
    hint_status = "🔒" if hint_used else "🔓"
    puzzle_status = ["✓" if solved else "✗" for solved in puzzles_solved]

    print(f"""{RED}{BOLD}
    ╔════════════════════════════════════════════════════════════
    ║ ROOM 03 | LEVEL 01 | TIME: {get_time()} | HINT: {hint_status}               ║
    ║ PUZZLES: {puzzle_status[0]}  {puzzle_status[1]}  {puzzle_status[2]}   {puzzle_status[3]}                                        ║
    ╚════════════════════════════════════════════════════════════
    {RESET}""")

# TIME PENALTY
def time_penalty(seconds, reason):
    global remaining_seconds
    remaining_seconds -= seconds
    if remaining_seconds < 0:
        remaining_seconds = 0
    clear_screen()
  
    print(f"""\n{RED}{BOLD}{BLINK}
                    ⚠  THE DOLLS ARE WATCHING YOU  ⚠{RESET}\n""")
    
    type_text(f"{RED}{reason}{RESET}", 0.04)
    type_text(f"\n{YELLOW}TIME LOST: {seconds} SECONDS{RESET}", 0.04)
    type_text(f"{GRAY}\nThe haunting lullaby grows louder...{RESET}", 0.04)
    time.sleep(2)

# HINT
def available_hints(puzzles):
    for number, solved in enumerate(puzzles, start=1):
        if not solved:
            yield number
def use_hint():
    global hint_used
    if hint_used:
        print(f"\n{RED}{BOLD}⚠ MR. SALEH'S RECORD LOGS HAVE ALREADY GIVEN YOU ONE HINT.{RESET}")
        print(f"{GRAY}You cannot ask for another hint in this level.{RESET}")
        time.sleep(2)
        return
    
    print(f"""{YELLOW}{BOLD}\n
        ╔════════════════════════════════════════════╗
        ║              CHOOSE YOUR HINT              ║
        ╚════════════════════════════════════════════╝{RESET}""")
    for number in available_hints(puzzles_solved):
        print(f"{number} - [Puzzle {number:02d}]")    
    h = input(f"{YELLOW}Which question would you like help with? >>> {RESET}")
    if h == "1":
        hint_used = True
        time_penalty(60, "You searched the director's ledger...")
        print(f"""{YELLOW}{BOLD}\n💡 HINT:
        "Do not trust your words; trust your eyes."{RESET}""")
        print(f"""{GRAY}Note down the order of colors as they flash on the screen before the terminal darkens.{RESET}""")

    elif h == "2":
        hint_used = True
        time_penalty(60, "You searched the director's ledger...")
        print(f"""{YELLOW}{BOLD}\n💡 HINT: 
        "The exit is double-locked by space and iron.\nSecrets lie in the upper corridors before the lower descent."{RESET}""")
      
        
    elif h == "3":
        hint_used = True
        time_penalty(60, "You searched the director's ledger...")
        print(f"""\n{YELLOW}{BOLD}💡 HINT:
        "The key to these numbers isn't in your head—it's written somewhere in this room.{RESET}{GRAY}\nSearch your surroundings for a hidden note before attempting the terminal."{RESET}""")

    elif h == "4":
        hint_used = True
        time_penalty(60, "You searched the director's ledger...")
        print(f"""{YELLOW}{BOLD}\n💡 HINT: 1975 is the reason of where you are now !{RESET}""")    
    else:
        print(f"\n{RED}❌ Please choose 1, 2, or 3.{RESET}")
        time.sleep(2)
        return
    
    print(f"""\n{RED}{BOLD}⚠ YOUR ONE HINT HAS BEEN USED.{RESET}""")
    input(f"\n{GRAY}Press ENTER to continue...{RESET}")

# PUZZLE 1
def puzzle_1():
    import random
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 01                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE CHROMATIC MEMORY SYSTEM{RESET}")
    print(f"\n{WHITE}Memorize the visual color sequence to bypass the lock:{RESET}\n")

    input(f"{YELLOW}Press ENTER when you are ready to observe the sequence...{RESET}")

    colors_data = {
        "a": ("RED", "\033[91m"),
        "b": ("GREEN", "\033[92m"),
        "c": ("BLUE", "\033[94m"),
        "d": ("YELLOW", "\033[93m"),
        "e": ("PURPLE", "\033[95m"),
        "f": ("CYAN", "\033[96m")
    }
    keys_list = list(colors_data.keys())

    sequence = [random.choice(keys_list) for _ in range(5)]

    clear_screen()
    print(f"{YELLOW}Focus! The sequence is flashing...{RESET}\n")
    time.sleep(1.5)

    for key in sequence:
        clear_screen()
        c_name, c_code = colors_data[key]
        print("\n\n")
        print(f"        {c_code}████ {c_name} ████{RESET}")
        time.sleep(0.7)
        clear_screen()
        time.sleep(0.2)

    clear_screen()
    print(f"{CYAN}Available Colors & Keys:{RESET}\n")
    for key, (c_name, c_code) in colors_data.items():
        print(f"  {c_code}■ {c_name}{RESET} [{key.upper()}]")

    print(f"\n{WHITE}Enter the 5 keys (A, B, C, D, E, F) one by one in exact sequence.{RESET}")
    print(f"{GRAY}[Type 'Q' anytime to quit attempt]{RESET}\n")

    user_sequence = []
    aborted = False

    for i in range(5):
        while True:
            key_input = input(f"{RED}☠ Color {i + 1}/5: {RESET}").strip().lower()

            if key_input == "q":
                aborted = True
                break

            if key_input in keys_list:
                user_sequence.append(key_input)
                break

            print(f"{RED}Please enter A, B, C, D, E or F.{RESET}")

        if aborted:
            break

    if not aborted and user_sequence == sequence:
        puzzles_solved[0] = True
        print(f"\n{GREEN}✓ PUZZLE 01 SOLVED. Memory pattern matched!{RESET}")
        time.sleep(1.5)
    else:
        print(f"\n{RED}✗ WRONG SEQUENCE OR ABORTED.{RESET}")
        correct_str = " -> ".join([colors_data[k][0] for k in sequence])
        print(f"{YELLOW}Correct Sequence was: {correct_str}{RESET}")
        time_penalty(30, "Memory pattern corrupted! System locks down...")
        time.sleep(1.5)

# PUZZLE 2
import os
import select
import sys
import time

if os.name == "nt":
    import msvcrt

    os.system("")

    def get_key():
        k = msvcrt.getch()
        if k in (b"\x00", b"\xe0"):
            k = msvcrt.getch()
            return {"H": "w", "P": "s", "K": "a", "M": "d"}.get(
                k.decode("latin1", errors="ignore"), ""
            )
        return k.decode("utf-8", errors="ignore").lower()
else:
    import termios
    import tty

    def get_key():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == "\x1b":
                select.select([sys.stdin], [], [], 0.1)
                ch = sys.stdin.read(2)[-1]
                return {"A": "w", "B": "s", "D": "a", "C": "d"}.get(ch, "")
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
def puzzle_2():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 01                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{WHITE}Escape the Mind Maze to bypass the security system!{RESET}")
    print("Find the Key 🔑, unlock the Door 🚪, and reach the Goal ⭐.\n")
    input("Press Enter to start the maze...")

    # خريطة المتاهة
    MAZE = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, "K", 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, "X", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, "X", 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, "D", 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    START_POS = [1, 1]
    GOAL_POS = [11, 15]
    player_pos = list(START_POS)
    has_key = False

    CELLS = {
        1: "██ ",
        0: " . ",
        "K": "🔑 ",
        "D": "🚪 ",
        "X": "💥 ",
        "P": "🟡 ",
        "G": "⭐ ",
    }

    def draw_board(msg=""):
        print("\033[H", end="")
        out = [
            "=" * 51,
            "              PUZZLE 01: MIND MAZE               ",
            "=" * 51 + "\n",
        ]

        for r in range(len(MAZE)):
            row = " "
            for c in range(len(MAZE[0])):
                pos = [r, c]
                if pos == player_pos:
                    row += CELLS["P"]
                elif pos == GOAL_POS:
                    row += CELLS["G"]
                elif MAZE[r][c] == "K" and has_key:
                    row += CELLS[0]
                elif MAZE[r][c] == "D" and has_key:
                    row += CELLS[0]
                else:
                    row += CELLS[MAZE[r][c]]
            out.append(row)

        out.append("\n" + "-" * 51)
        out.append(f"Key Status: {'COLLECTED ✅' if has_key else 'MISSING ❌'}")
        out.append("Controls: ARROWS / WASD | Q: Quit Puzzle")
        out.append(f"Status: {msg:<40}")
        out.append("-" * 51)
        print("\n".join(out))
    def move(cmd):
        nonlocal player_pos, has_key
        dirs = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        if cmd not in dirs:
            return ""
        dr, dc = dirs[cmd]
        nr, nc = player_pos[0] + dr, player_pos[1] + dc
        target = MAZE[nr][nc]
        if target == 1:
            return "Hit a Wall!"
        if target == "D" and not has_key:
            return "Door is locked! Find the Key 🔑 first."
        if target == "X":
            player_pos = list(START_POS)
            # خصم وقت عند الاصطدام بالشوك
            time_penalty(10, "Stepped on spikes! Extra penalty applied.")
            return "Hit a Spike 💥! Resetting to start."
        player_pos = [nr, nc]
        if target == "K" and not has_key:
            has_key = True
            return "Key collected 🔑!"
        return "Moved!"
    clear_screen()
    print("\033[?25l", end="")  # إخفاء المؤشر
    msg = "Welcome! Find the Key to unlock the Door."
    try:
        while True:
            draw_board(msg)
            # حالة الفوز
            if player_pos == GOAL_POS:
                print("\033[?25h", end="")  # إرجاع المؤشر
                puzzles_solved[1] = True
                print(f"\n{GREEN}✓ PUZZLE 01 SOLVED! MAZE CLEARED.{RESET}")
                time.sleep(1.5)
                break
            key = get_key()
            # الاستسلام / الانسحاب
            if key == "q":
                print("\033[?25h", end="")
                print(f"\n{RED}✗ PUZZLE ABANDONED.{RESET}")
                time_penalty(30, "You abandoned the maze system!")
                time.sleep(1)
                break
            msg = move(key)
    finally:
        print("\033[?25h", end="")
# PUZZLE 3
def puzzle_3():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 03                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE NUMBER CODE SYSTEM{RESET}")
    print(f"\n{WHITE}Decode the numerical sequence to unlock the terminal:{RESET}\n")
    print(f"\n{GRAY}👁 [ The terminal seems to rely on a rule hidden around you... ]{RESET}\n")
    print(f"{YELLOW}    2 - 1 - 2 - 25{RESET}\n")
    print("-" * 50)
    try:
        answer = input(f"{RED}☠ ENTER THE SECRET WORD: {RESET}").strip().upper()

        if answer == "BABY":
            puzzles_solved[2] = True
            print(f"\n{GREEN}✓ PUZZLE 03 SOLVED. Word accepted!{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ WRONG WORD.{RESET}")
            time_penalty(30, "Wrong sequence translation! System rejected key...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! Time is running out...")
        time.sleep(1)

def puzzle_4():
    clear_screen()
    
    # الكود المستنتج من القصة (سنة بداية الأحداث 1975)
    target_code = [1, 9, 7, 5]
    
    # توليد رمز عشوائي للبداية
    current_code = [random.randint(0, 9) for _ in range(4)]
    while current_code == target_code:
        current_code = [random.randint(0, 9) for _ in range(4)]

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 04                       ║
    ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{CYAN}THE ORPHANAGE ARCHIVE LOCK{RESET}")
        print(f"\n{WHITE}Enter the 4-digit year when the dark truth began at Dar Al Noor:{RESET}\n")

        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")

        print(f"{GRAY}👁  [ Search the orphanage story entry... In what year did Mr. Saleh start his lie? ]{RESET}\n")
        print("-" * 50)
        print(f"{WHITE}Controls:{RESET}")
        print(f"  {CYAN}[1, 2, 3, 4]{RESET} Rotate dial 1, 2, 3, or 4")
        print(f"  {GREEN}[S]{RESET} Submit Combination")
        print(f"  {RED}[Q]{RESET} Quit Attempt\n")

        choice = input(f"{RED}☠ Choose action: {RESET}").strip().lower()

        if choice == '1':
            current_code[0] = (current_code[0] + 1) % 10
        elif choice == '2':
            current_code[1] = (current_code[1] + 1) % 10
        elif choice == '3':
            current_code[2] = (current_code[2] + 1) % 10
        elif choice == '4':
            current_code[3] = (current_code[3] + 1) % 10

        elif choice == 's':
            if current_code == target_code:
                puzzles_solved[3] = True
                print(f"\n{GREEN}✓ PUZZLE 04 SOLVED. The archive lock clicks open!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ INCORRECT COMBINATION.{RESET}")
                time_penalty(30, "The lock alarm screeched! The dolls' laughter grows louder...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted archive lock interaction.{RESET}")
            time.sleep(1)
            break
# SEARCH THE ROOM
import sys
import time

def slow_print(text, delay=0.04):
    """دالة لطباعة النص حرفاً بحرف لإعطاء تأثير التشويق والرعب"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def empty_corner():
    clear_screen()
    
    # سرد قصصي مرعب لدار الأيتام
    slow_print(f"{DARK_RED}{BOLD}You wander into the pitch-black operating corner of the orphanage...{RESET}\n", 0.05)
    time.sleep(0.4)
    slow_print(f"{GRAY}Cold, rusted surgical tools litter the wooden floorboards.{RESET}", 0.04)
    slow_print(f"{GRAY}Your flashbeam lands on the doctor's table, covered in dark stains.{RESET}", 0.04)
    slow_print(f"{GRAY}Among faded crayon drawings of headless children, a handwritten rule is glued...{RESET}\n", 0.04)
    time.sleep(0.8)

    # الملاحظة بتصميم مرعب ومناسب للقصة
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║               ORPHANAGE LOG - NOTE 03                ║
    ╠══════════════════════════════════════════════════════╣{RESET}""")

    slow_print(f"{YELLOW}       'The children were given numbers instead of names...{RESET}", 0.05)
    slow_print(f"{YELLOW}        Every number represents a child's letter by its{RESET}", 0.05)
    slow_print(f"{YELLOW}        exact position in the alphabet.'{RESET}", 0.05)

    print(f"""{RED}{BOLD}    ║                                                      ║
    ║   [ Example:  A = 1  │  B = 2  │  C = 3 ... ]        ║
    ╚══════════════════════════════════════════════════════╝
    {RESET}""")

    time.sleep(0.5)
    slow_print(f"{DARK_RED}A faint child's laughter echoes behind the cabinet...{RESET}", 0.05)
    
    input(f"\n{WHITE}☠ Press ENTER to step back into the dark...{RESET}")


# GAME LOOP
def game_loop(username):
    while True:
        if remaining_seconds <= 0:
            game_over()
            return "ROOM1"
        clear_screen()
        show_header()
        # واجهة دار النور الملعونة (Dar Al Noor Orphanage Dormitory)
        print(f"{B}        🧸   [ DAR AL NOOR ORPHANAGE :: DORMITORY 1975 ]   🧸{RESET}")
        print(f"{D}  -- THE CHILDREN ARE SLOWLY SINGING MR. SALEH'S LULLABY... --{RESET}\n")
        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(f"  {R}▲ [LEFT CORNER]{RESET}                                             {R}[RIGHT CORNER] ▲{RESET}")
        print(f"  {Y}[1]{RESET} {CYAN}🛏️  Inspect Perfectly Made Beds{RESET}           {Y}[2]{RESET} {CYAN}🧸 Examine Dolls With Named Pillows{RESET}\n")

        print(f"                            {B}☠️  [SIDE CORNER]  ☠️{RESET}")
        print(f"                {Y}[3]{RESET} {P} 🛏️One of the children's beds{RESET}\n")
        # المركز (مكتب أستاذ صالح وحقيقته)
        print(f"                            {B}☠️  MR. SALEH'S DESK  ☠️{RESET}")
        print(f"                {Y}[4]{RESET} {P}📜 Search Forgotten Adoption Records{RESET}\n")

        # القاعدة (خيارات التفاعل والهروب)
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"  {Y}[5]{RESET} {P}🔍 Search Dark Room Corners{RESET} │  {Y}[6]{RESET} {P}💡 Listen to Whispered Lullaby{RESET} │  {Y}[7]{RESET} {B}🚪 Force Locked Dormitory Door{RESET}")
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"{B}  🩸  "+ "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2+ " ALL DOLLS HAVE OPENED THEIR EYES... THEY ARE WATCHING YOU "+ "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2+ f"  🩸{RESET}")

        try:
            choice = int(input(f"\n{B}🩸 [15-MIN TIMEOUT] Name the children before they keep you forever [1-7]: {RESET}"))
            if choice == 1:
                if puzzles_solved[0]:
                    print(f"\n{GREEN}🛏️ The children's beds are empty. True names revealed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_1()

            elif choice == 2:
                if puzzles_solved[1]:
                    print(f"\n{GREEN}🧸 The dolls under the pillows have closed their eyes. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_2()

            elif choice == 3:
                if puzzles_solved[2]:
                    print(f"\n{GREEN}📜 Mr. Saleh's dark adoption lies are exposed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_3()

            elif choice == 4:
                if puzzles_solved[3]:
                    print(f"\n{GREEN}🛏️ The children's beds are empty. True names revealed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_4()
                     

            elif choice == 5:
                empty_corner()

            elif choice == 6:
                use_hint()

            elif choice == 7:
                print(
                    f"\n{Y}⚠️ THE DORMITORY DOOR SNAPPED LOCKED BEHIND YOU!\nTHE ORPHANAGE WILL NOT LET YOU LEAVE WITHOUT A CHILD.{RESET}"
                )
                time.sleep(2.5)
                continue

            else:
                print(
                    f"\n{R}❌ INVALID CHOICE. A child's distorted lullaby gets closer...{RESET}"
                )
                time.sleep(1)
                clear_screen()

        except ValueError:
            print(
                f"\n{R}❌ NUMBERS ONLY! The whisperer asks: 'Which one of you will stay with us?'{RESET}"
            )
            time.sleep(1)
            clear_screen()

        if all(puzzles_solved):
            return level_complete(username)

# LEVEL COMPLETE
def level_complete(username):
    global timer_running
    timer_running = False
    # تحديث شارة الغرفة الثالثة (room3_badge)
    update_room_badge(username, 3, "SILVER")
    clear_screen()
    print(f"""{GREEN}{BOLD}

    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║              LEVEL 01 CLEARED                    ║
    ║                                                  ║
    ║                 BADGE: SILVER                    ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}\n""")

    type_text(f"{WHITE}The dormitory door unlocked...{RESET}", 0.04)
    type_text(f"{GRAY}But Mr. Saleh's private basement lies ahead.{RESET}", 0.04)

    input(f"\n{WHITE}Press ENTER to continue...{RESET}")
    time.sleep(1)

    from menu import after_level1_room3
    return after_level1_room3(username)

# GAME OVER
def game_over():
    global timer_running
    timer_running = False
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║               THE LULLABY ENDS                   ║
    ║                                                  ║
    ║           YOU ARE NOW ONE OF THEM                ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{DARK_RED}The orphanage took what it was missing... from you.{RESET}", 0.04)
    input(f"\n{WHITE}Press ENTER to return...{RESET}")

# ROOM 3 LEVEL 1
def room3_level1(username):
    global remaining_seconds
    global hint_used
    global puzzles_solved
    global timer_running

    remaining_seconds = 15 * 60
    hint_used = False
    puzzles_solved = [False, False, False,False]
    timer_running = False
    intro_screen()
    play_story()
    return level_start(username)

# =========================================================
# LEVEL 2 PUZZLES (MR. SALEH'S BASEMENT)
# =========================================================

level2_puzzles_solved = [False, False, False,False]
level2_hint_used = False

def level2_puzzle_1():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 01                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE BROKEN MESSAGE SYSTEM{RESET}")
    print(f"\n{WHITE}Decode the encrypted word using the reference pattern[3 steps]:{RESET}\n")

    print(f"{GRAY}    ┌──────────────────────────────────────────────┐{RESET}")
    print(f"{GRAY}    │ Example Reference:                           │{RESET}")
    print(f"{GRAY}    │ KHOOR  ───>  HELLO                           │{RESET}")
    print(f"{GRAY}    └──────────────────────────────────────────────┘{RESET}\n")

    print(f"{YELLOW}    Encrypted Word: RUSKDQ{RESET}\n")
    print("-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER DECRYPTED WORD: {RESET}").strip().upper()

        if answer == "ORPHAN":
            level2_puzzles_solved[0] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED. Decoded to ORPHAN!{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ WRONG DECRYPTION.{RESET}")
            time_penalty(30, "Wrong decryption! The shift pattern was mismatched...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! Time is running out...")
        time.sleep(1)


def level2_puzzle_2():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 02                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE DIGITAL LOOP SEQUENCE{RESET}")
    print(f"\n{WHITE}Analyze the pattern to discover the hidden value of the final code:{RESET}\n")

    print(f"{GRAY}    ┌──────────────────────────────────────────────┐{RESET}")
    print(f"{GRAY}    │  1234  ───>  0                               │{RESET}")
    print(f"{GRAY}    │  6081  ───>  4                               │{RESET}")
    print(f"{GRAY}    │  9306  ───>  3                               │{RESET}")
    print(f"{GRAY}    └──────────────────────────────────────────────┘{RESET}\n")

    print(f"{YELLOW}    Target Code: 8809 = ?{RESET}\n")
    print("-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER THE NUMBER: {RESET}").strip()

        # الإجابة هي 6 (الرقم 8 يحتوي على دائرين، 8 الثانية دائرتين، 0 دائرة، 9 دائرة -> 2+2+1+1 = 6)
        if answer == "6":
            level2_puzzles_solved[1] = True
            print(f"\n{GREEN}✓ PUZZLE 02 SOLVED. Sequence verified!{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ WRONG VALUE.{RESET}")
            time_penalty(30, "Incorrect evaluation! The system resets...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! Time is running out...")
        time.sleep(1)


def level2_puzzle_3():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 03                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE SHIFTED KEYBOARD SYSTEM{RESET}")
    print(f"\n{WHITE}Decode the encrypted terminal password to override the lock:{RESET}")
    
    # جملة توجيهية خفيفة تحث اللاعب على الاستكشاف
    print(f"\n{GRAY}👁  [ Someone scribbled a note about the terminal keyboard in this room... ]{RESET}\n")

    print(f"{YELLOW}    Encrypted Password: JUSA{RESET}\n")
    print("-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER DECRYPTED PASSWORD: {RESET}").strip().upper()

        if answer == "KIDS":
            level2_puzzles_solved[2] = True
            print(f"\n{GREEN}✓ PUZZLE 03 SOLVED. Terminal unlocked!{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ ACCESS DENIED.{RESET}")
            time_penalty(30, "Wrong password! Security lockdown active...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! Time is running out...")
        time.sleep(1)

def level2_puzzle_4():
    clear_screen()
    
    # الكود المستنتج (5150)
    target_code = [5, 1, 5, 0]
    
    # توليد رمز عشوائي للبداية
    current_code = [random.randint(0, 9) for _ in range(4)]
    while current_code == target_code:
        current_code = [random.randint(0, 9) for _ in range(4)]

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 04                       ║
    ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{CYAN}MR. SALEH'S DORMITORY SAFE{RESET}")
        print(f"\n{WHITE}Decode the digits of the Director's name, time limit, and departed children:{RESET}\n")

        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")

        print(f"{GRAY}👁  [ Count 'SALEH' letters, add your remaining minutes, then the number of children who left... ]{RESET}\n")
        print("-" * 50)
        print(f"{WHITE}Controls:{RESET}")
        print(f"  {CYAN}[1, 2, 3, 4]{RESET} Rotate dial 1, 2, 3, or 4")
        print(f"  {GREEN}[S]{RESET} Submit Combination")
        print(f"  {RED}[Q]{RESET} Quit Attempt\n")

        choice = input(f"{RED}☠ Choose action: {RESET}").strip().lower()

        if choice == '1':
            current_code[0] = (current_code[0] + 1) % 10
        elif choice == '2':
            current_code[1] = (current_code[1] + 1) % 10
        elif choice == '3':
            current_code[2] = (current_code[2] + 1) % 10
        elif choice == '4':
            current_code[3] = (current_code[3] + 1) % 10

        elif choice == 's':
            if current_code == target_code:
                level2_puzzles_solved[3] = True
                print(f"\n{GREEN}✓ PUZZLE 02 SOLVED. Mr. Saleh's safe unlocks!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ INCORRECT COMBINATION.{RESET}")
                time_penalty(30, "The safe mechanism snaps! Cold hands touch your shoulder...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted safe interaction.{RESET}")
            time.sleep(1)
            break

import sys
import time

def slow_print(text, delay=0.04):
    """دالة لطباعة النص حرفاً بحرف لإعطاء تأثير الرعب والتشويق"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def empty_corner_level2():
    clear_screen()
    
    # مقدمة قصصية مرعبة تظهر بطباعة بطيئة
    slow_print(f"{RED}{BOLD}You step into the pitch-black corner of the room...{RESET}\n", 0.05)
    time.sleep(0.5)
    slow_print(f"{GRAY}The air is cold. Your flashlight flickers and shines upon a bloody table.{RESET}", 0.04)
    slow_print(f"{GRAY}Beneath it, a torn piece of paper is pinned with a rusty nail...{RESET}\n", 0.04)
    time.sleep(0.8)

    # شكل الورقة المرعبة
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║                 THE VICTIM'S NOTE                    ║
    ╠══════════════════════════════════════════════════════╣{RESET}""")
    
    # نص الملاحظة يظهر ببطء ليحبس الأنفاس
    slow_print(f"{YELLOW}   'If you are reading this... I am already gone.{RESET}", 0.05)
    slow_print(f"{YELLOW}    He changed the terminal key mappings to trap us.{RESET}", 0.05)
    slow_print(f"{YELLOW}    EVERY KEY IS SHIFTED ONE STEP TO THE RIGHT.{RESET}", 0.06)
    slow_print(f"{YELLOW}    Look at the keyboard... Move them back...'{RESET}", 0.05)
    
    print(f"""{RED}{BOLD}    ║                                                      ║
    ║   [ Example:  J ──> K  │  U ──> I  │  A ──> S ]      ║
    ╚══════════════════════════════════════════════════════╝
    {RESET}""")

    time.sleep(0.5)
    input(f"\n{RED}☠ Press Enter to turn back before IT sees you...{RESET}")



# ROOM 3 LEVEL 2
def room3_level2(username):
    global remaining_seconds
    global level2_hint_used
    global level2_puzzles_solved
    global timer_running
    player_data = get_player_data(username)
    room3_badge = player_data["room3_badge"]
    if room3_badge == "LOCKED":
        clear_screen()
        print(f"""{RED}{BOLD}
        ╔══════════════════════════════════════════════════╗
        ║                                                  ║
        ║               🔒 ACCESS DENIED 🔒               ║
        ║                                                  ║
        ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{RED}You must complete LEVEL 01 first.{RESET}")
        input(f"\n{WHITE}Press ENTER to return...{RESET}")
        return "ROOM3"
    
    while True:
        choice = input("\nDo you want to hear the story again? (Y/N): ").strip().upper()
        if choice == "Y":
            clear_screen()
            play_story()  # هنا هتتعاد القصة بـ أصوات القصة كاملة
            break
        elif choice == "N":
            # إيقاف موسيقى المنيو
            stop_menu_music()
            # تشغيل موسيقى الباك جراوند فقط (بدون أي أصوات للقصة)
            play_sound2_only()
            break
        else:
            print(f"{RED}Invalid choice! Please enter 'Y' or 'N'.{RESET}")
        
    remaining_seconds = 15 * 60
    level2_hint_used = False
    level2_puzzles_solved = [False, False, False,False]
    timer_running = False
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    LEVEL 02                      ║
    ║               MR. SALEH'S BASEMENT               ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}You entered the hidden basement of Mr. Saleh...{RESET}", 0.04)
    type_text(f"{RED}The spirits of all lost children gather here.{RESET}", 0.04)
    type_text(f"{YELLOW}You have 15 minutes to name them all and escape.{RESET}", 0.04)

    input(f"\n{WHITE}Press ENTER to continue...{RESET}")
    start_timer()
    return level2_game_loop(username)

def level2_hint():
    global level2_hint_used
    if level2_hint_used:
        print(f"\n{RED}{BOLD}⚠ THE SYSTEM HAS ALREADY GIVEN YOU ONE HINT.{RESET}")
        print(f"{GRAY}You cannot ask for another hint in this level.{RESET}")
        time.sleep(2)
        return
    print(f"""{YELLOW}{BOLD}
        ╔════════════════════════════════════════════╗
        ║              CHOOSE YOUR HINT              ║
        ╚════════════════════════════════════════════╝
        {RESET}""")

    for number in available_hints(level2_puzzles_solved):
        print(f"{number} - [Puzzle {number:02d}]")    
    h = input(f"\n{YELLOW}Which question would you like help with? >>> {RESET}")
    if h == "1":
        level2_hint_used = True
        time_penalty(60, "You asked the orphan archives for help...")
        print(f"""{YELLOW}{BOLD}💡 HINT:
    "Every letter in the encrypted message has been pushed forward in the alphabet by the exact same number of steps{RESET}{GRAY}\nLook closely at how 'KHOOR' steps backward into 'HELLO'."{RESET}""")
    elif h == "2":
        level2_hint_used = True
        time_penalty(60, "You asked the orphan archives for help...")
        print(f"""{YELLOW}{BOLD}💡 HINT:
        "Stop doing math. Instead, draw each digit on paper and count how many closed circles or loops you create with your pen."{RESET}""")
    elif h == "3":
        level2_hint_used = True
        time_penalty(60, "You asked the orphan archives for help...")
        print(f"""\n{YELLOW}{BOLD}💡 HINT:
        "Don't waste time staring at the screen. The answer won't make sense until you search the room"{RESET}{GRAY}\nfind the note hidden near the table.{RESET}""")
    elif h == "4":
            level2_hint_used = True
            time_penalty(60, "You asked the orphan archives for help...")
            print(f"""\n{YELLOW}{BOLD}💡 HINT:
            "First dial: count the letters in 'SALEH'. Second & third dials: the 15-minute countdown"{RESET}{GRAY}\nFourth dial: how many children actually left the orphanage?{RESET}""")    
    else:
        print(f"\n{RED}❌ Please choose 1, 2, or 3.{RESET}")
        time.sleep(2)
        return
    print(f"""\n{RED}{BOLD}⚠ YOUR ONE HINT HAS BEEN USED.\n{RESET}""")
    input(f"\n{GRAY}Press ENTER to continue...{RESET}")

def level2_game_loop(username):
    while True:
        if remaining_seconds <= 0:
            game_over()
            return "ROOM3"
        clear_screen()
        print(f"""{RED}{BOLD}
╔════════════════════════════════════════════════════════════╗
║ ROOM 03 | LEVEL 02 | TIME: {get_time()} | HINT: {'🔒' if level2_hint_used else '🔓'}                 ║
║ PUZZLES: {"✓" if level2_puzzles_solved[0] else "✗"}  {"✓" if level2_puzzles_solved[1] else "✗"}  {"✓" if level2_puzzles_solved[2] else "✗"}   {"✓" if level2_puzzles_solved[3] else "✗"}     ║
╚════════════════════════════════════════════════════════════╝
{RESET}""")

# واجهة دار النور الملعونة (Dar Al Noor Orphanage Dormitory)
        print(f"{B}        🧸   [ DAR AL NOOR ORPHANAGE :: DORMITORY 1975 ]   🧸{RESET}")
        print(f"{D}  -- THE CHILDREN ARE SLOWLY SINGING MR. SALEH'S LULLABY... --{RESET}\n")
        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(f"  {R}▲ [LEFT CORNER]{RESET}                                             {R}[RIGHT CORNER] ▲{RESET}")
        print(f"  {Y}[1]{RESET} {CYAN}🛏️  Inspect Perfectly Made Beds{RESET}           {Y}[2]{RESET} {CYAN}🧸 Examine Dolls With Named Pillows{RESET}\n")
        print(f"                            {B}☠️  [SIDE CORNER]  ☠️{RESET}")
        print(f"                {Y}[3]{RESET} {P}🛏️One of the children's beds{RESET}\n")
        # المركز (مكتب أستاذ صالح وحقيقته)
        print(f"                            {B}☠️  MR. SALEH'S DESK  ☠️{RESET}")
        print(f"                {Y}[4]{RESET} {P}📜 Search Forgotten Adoption Records{RESET}\n")

        # القاعدة (خيارات التفاعل والهروب)
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"  {Y}[5]{RESET} {P}🔍 Search Dark Room Corners{RESET} │  {Y}[6]{RESET} {P}💡 Listen to Whispered Lullaby{RESET} │  {Y}[7]{RESET} {B}🚪 Force Locked Dormitory Door{RESET}")
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"{B}  🩸  "+ "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2+ " ALL DOLLS HAVE OPENED THEIR EYES... THEY ARE WATCHING YOU "+ "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2+ f"  🩸{RESET}")
        
        try:
            choice = int(input(f"\n{B}🩸 [15-MIN TIMEOUT] Name the children before they keep you forever [1-7]: {RESET}"))

            if choice == 1:
                if level2_puzzles_solved[0]:
                    print(f"\n{GREEN}🛏️ The children's beds are empty. True names revealed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_1()

            elif choice == 2:
                if level2_puzzles_solved[1]:
                    print(f"\n{GREEN}🧸 The dolls under the pillows have closed their eyes. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_2()

            elif choice == 3:
                if level2_puzzles_solved[2]:
                    print(f"\n{GREEN}📜 Mr. Saleh's dark adoption lies are exposed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_3()

            elif choice == 4:
                if level2_puzzles_solved[3]:
                    print(f"\n{GREEN}🛏️ The children's beds are empty. True names revealed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_4()       

            elif choice == 5:
                empty_corner_level2()

            elif choice == 6:
                level2_hint()

            elif choice == 7:
                print(
                    f"\n{Y}⚠️ THE DORMITORY DOOR SNAPPED LOCKED BEHIND YOU!\nTHE ORPHANAGE WILL NOT LET YOU LEAVE WITHOUT A CHILD.{RESET}"
                )
                time.sleep(2.5)
                continue

            else:
                print(
                    f"\n{R}❌ INVALID CHOICE. A child's distorted lullaby gets closer...{RESET}"
                )
                time.sleep(1)
                clear_screen()

        except ValueError:
            print(
                f"\n{R}❌ NUMBERS ONLY! The whisperer asks: 'Which one of you will stay with us?'{RESET}"
            )

        if all(level2_puzzles_solved):
            return level2_complete(username)

def level2_complete(username):
    global timer_running
    timer_running = False
    update_room_badge(username, 3, "GOLD")
    clear_screen()
    print(f"""\n{GREEN}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║                LEVEL 02 CLEARED                  ║
    ║                                                  ║
    ║                   🥇🏆 GOLD                      ║
    ║                                                  ║
    ║                ROOM 03 COMPLETED                 ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}\n""")
    type_text(f"{WHITE}The names of all forgotten children have been spoken...{RESET}", 0.04)
    type_text(f"{GRAY}Their spirits are finally free.{RESET}", 0.04)

    input(f"\n{WHITE}Press ENTER to continue...{RESET}")
    print("\n[1] RETURN TO MAIN MENU")
    print("[2] EXPLORE ANOTHER ROOM")

    while True:
        try:
            choice = int(input("\n☠ ENTER YOUR CHOICE: "))
            if choice == 1:
                clear_screen()
                stop_background_music()
                return "MENU"
            elif choice == 2:
                clear_screen()
                stop_background_music()
                return "EXPLORE"
            else:
                print(f"{RED}☠ INVALID CHOICE.{RESET}")
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}")

def room3(username):
    return room3_level1(username)