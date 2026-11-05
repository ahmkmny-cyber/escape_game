# file dr_ragheb.py
import os
import time
import threading
import sys
from player_data import update_room_badge, get_player_data
from music_of_game import stop_menu_music
import pygame
import random
pygame.mixer.init()

sound1 = r"C:\Users\Compu City\Downloads\Dr_Ragheb_Voiceover_no_whistle.mp3"
sound2 = r"C:\Users\Compu City\Downloads\Dr_Ragheb_Background_no_scream (1).mp3"

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

# الألوان القياسية الخاصة بالعيادة الملعونة
R = "\033[91m"  # أحمر ساطع (دموي)
B = "\033[31m"  # أحمر قاني
P = "\033[95m"  # بنفسجي الموت/الأرواح
Y = "\033[93m"  # أصفر تحذيري
CYAN = "\033[96m"  # أزرق طبي بارد
D = "\033[90m"  # رمادي مظلم
GREEN = "\033[92m"  # أخضر الأجهزة الطبية
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
             ██████╗ ██████╗     ██████╗  █████╗  ██████╗ ██╗  ██╗██xFF╗██████╗ 
             ██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔════╝ ██║  ██║██╔╝██╔════╝ 
             ██║  ██║██████╔╝    ██████╔╝███████║██║  ███╗███████║██║ █████╗   
             ██║  ██║██╔══██╗    ██╔══██╗██╔══██║██║   ██║██╔══██║██║ ██╔══╝   
             ██████╔╝██║  ██║    ██║  ██║██║  ██║╚██████╔╝██║  ██║██║ ███████╗ 
             ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚══════╝ 
            \n                 DR_RAGHEB.PY - THE SECRET CLINIC\n{RESET}""")
        else:
            print(f"""{DARK_RED}{BOLD}\n
            
                        [ PATIENT RECORD EXPIRED ]
                        [ LIFE SUPPORT FAILING ]
                        [ NO ESCAPE FROM CLINIC ] 
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
    ║               DR. RAGHEB'S CLINIC                ║
    ╚══════════════════════════════════════════════════╝

    {RESET}""")
    
    time.sleep(0.1)
    type_text(
        f"\n{GRAY}This place used to be the secret clinic of {RED}{BOLD}Dr. Ragheb{RESET}.\n",0.038,)
    time.sleep(0.3)
    type_text(
        f"{YELLOW}A doctor who believed he could defeat death...{RESET}\n", 0.04)
    time.sleep(0.35)
    type_text(
        f"{GRAY}He took patients that no one cared about,\nlocked them inside this"
        f"room, and performed terrible experiments\non them in the dark.{RESET}\n",0.055,)
    time.sleep(0.55)
    type_text(
        f"{GRAY}His last experiment went out of control...{RESET}\n{RED}{BOLD}ALL"
        f"PATIENTS DIED AT THE SAME MOMENT...{RESET}\n",0.040,)
    time.sleep(0.35)
    type_text(
        f"{WHITE}And the doctor mysteriously disappeared.\nBut their screams and the"
        f"sound of his scalpel can still be heard inside the walls.{RESET}\n",0.055,)
    time.sleep(0.45)
    type_text(
        f"{GRAY}Now, you are trapped in the same room where his last victim was"
        f"{RED}killed.{RESET}\n",0.045,)
    time.sleep(0.35)
    type_text(
        f"{RED}{BOLD}The spirits of this room are thirsty for revenge.\nAnd they"
        " can't tell the difference between the doctor and anyone who enters their"
        f"territory.{RESET}\n",0.05,)
    time.sleep(0.45)
    type_text(
        f"{RED}You have 15 minutes before the life-support machines declare you dead"
        f" too.{RESET}\n",0.045,)
    time.sleep(0.5)
    input(f"\n{YELLOW}Press ENTER to face the clinic...{RESET}")

# LEVEL START
def level_start(username):
    global timer_running
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  LEVEL 01                        ║
    ║             THE EXPERIMENT ROOM                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}The medical monitors beep rhythmically...{RESET}", 0.03)
    type_text(f"{RED}You have 15 minutes to escape before cardiac arrest.{RESET}\n", 0.03)
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
    ║ ROOM 02 | LEVEL 01 | TIME: {get_time()} | HINT: {hint_status}               ║
    ║ PUZZLES: {puzzle_status[0]}  {puzzle_status[1]}  {puzzle_status[2]}   {puzzle_status[3]}                                       ║
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
                    ⚠  PATIENT CONDITION CRITICAL  ⚠{RESET}\n""")
    
    type_text(f"{RED}{reason}{RESET}", 0.04)
    type_text(f"\n{YELLOW}TIME LOST: {seconds} SECONDS{RESET}", 0.04)
    type_text(f"{GRAY}\nThe flatline monitor tone gets closer...{RESET}", 0.04)
    time.sleep(2)

# HINT
def available_hints(puzzles):
    for number, solved in enumerate(puzzles, start=1):
        if not solved:
            yield number
def use_hint():
    global hint_used
    if hint_used:
        print(f"\n{RED}{BOLD}⚠ DR. RAGHEB'S NOTES HAVE ALREADY GIVEN YOU ONE HINT.{RESET}")
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
        time_penalty(60, "You searched the doctor's confidential notes...")
        print(f"""{YELLOW}{BOLD}💡 HINT: 
        "The exit is double-locked by space and iron.\nSecrets lie in the upper corridors before the lower descent."{RESET}""")
       

    elif h == "2":
        hint_used = True
        time_penalty(60, "You searched the doctor's confidential notes...")
        print(f"""{YELLOW}{BOLD}💡 HINT: 
        "Every row and every column is perfectly balanced, like a scale with identical weights."\n{RESET}""")
        print(f"""{GRAY}Look at what numbers 1 through 9 are already on the board—one core piece is still missing from the set.{RESET}""")
        
    elif h == "3":
        hint_used = True
        time_penalty(60, "You searched the doctor's confidential notes...")
        print(f"""{YELLOW}{BOLD}💡 HINT:
        "Every message has a structure. When reading a spine, you don't look at the entire paragraph"\n{RESET}""")
        print(f"""{GRAY}you trace down the very first step of each line from top to bottom{RESET}""")

    elif h == "4":
            hint_used = True
            time_penalty(60, "You searched the doctor's confidential notes...")
            print(f"""{YELLOW}{BOLD}💡 HINT: 
            "Look closely at the story's final warning. Combined with the moment of death"\n{RESET}""")
            print(f"""{GRAY}four digits emerge: 15 minutes left, followed by zero zero.{RESET}""")


    else:
        print(f"\n{RED}❌ Please choose 1, 2, or 3.{RESET}")
        time.sleep(2)
        return
    
    print(f"""\n{RED}{BOLD}⚠ YOUR ONE HINT HAS BEEN USED.{RESET}""")
    input(f"\n{GRAY}Press ENTER to continue...{RESET}")
# PUZZLE 1
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
            k = msvcrt.getch() # نظام التشغيل 
            # الاسهم
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
def puzzle_1():
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
                    row += CELLS["P"]# رسم اللاعب 
                elif pos == GOAL_POS:
                    row += CELLS["G"]#رسم النجمة
                elif MAZE[r][c] == "K" and has_key:
                    row += CELLS[0] #3لو التقط المفتاح
                elif MAZE[r][c] == "D" and has_key:
                    row += CELLS[0]#لو فتح الباب يختفي ويصبح طريق فارغ
                else:
                    row += CELLS[MAZE[r][c]]#رسم باقي العناصر 
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
                puzzles_solved[0] = True
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
# PUZZLE 2
def puzzle_2():
    clear_screen()

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 02                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
        print(f"\n{CYAN}THE MAGIC SQUARE GRID{RESET}")
        print(f"\n{WHITE}Analyze the 3x3 grid pattern and find the missing digit for [ ? ]:{RESET}\n")

        print("    -------------------------------------")
        print("          [ 2 ]   [ 9 ]   [ 4 ]")
        print("          [ 7 ]   [ 5 ]   [ 3 ]")
        print("          [ 6 ]   [ ? ]   [ 8 ]")
        print("    -------------------------------------")
        print(f"    {WHITE}Controls: Enter digit (1-9) | Type [Q] to Return{RESET}")
        print("    -------------------------------------\n")

        user_input = input(f"{RED}☠ Enter your answer: {RESET}").strip().lower()

        # الخروج دون خصم وقت
        if user_input == "q":
            print(f"\n{YELLOW}Stepped back from the number grid.{RESET}")
            time.sleep(1)
            break

        # التحقق من الإجابة الصحيحة
        elif user_input == "1":
            puzzles_solved[1] = True
            print(f"\n{GREEN}🎉 CORRECT! You found the missing number!{RESET}")
            print(f"{GREEN}✓ PUZZLE 02 SOLVED.{RESET}")
            time.sleep(1.5)
            break

        # الإجابة الخاطئة (خصم 30 ثانية)
        elif user_input in ["2", "3", "4", "5", "6", "7", "8", "9"]:
            print(f"\n{RED}❌ INCORRECT NUMBER!{RESET}")
            time_penalty(30, "The numbers hum with violent frequency! Incorrect grid calculation...")
            time.sleep(1.5)

        # مدخل غير صالح
        else:
            print(f"\n{RED}Invalid choice! Enter a single digit (1-9) or 'Q'.{RESET}")
            time.sleep(1)
# PUZZLE 3
def puzzle_3():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 03                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE HIDDEN ACROSTIC LOG{RESET}")
    print(f"\n{WHITE}Read the following sentences carefully to reveal the secret:{RESET}\n")

    print(f"{YELLOW}    Darkness Always Hides Truth.{RESET}")
    print(f"{YELLOW}    Only Wise Minds Understand.{RESET}")
    print(f"{YELLOW}    Carefully Read Every Line.{RESET}")
    print(f"{YELLOW}    Time Is Running Out.{RESET}")
    print(f"{YELLOW}    Open Your Eyes Wide.{RESET}")
    print(f"{YELLOW}    Remember The Hidden Pattern.{RESET}")
    print("\n" + "-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER THE HIDDEN WORD: {RESET}").strip().lower()

        if answer == "doctor":
            puzzles_solved[2] = True
            print(f"\n{GREEN}✓ PUZZLE 03 SOLVED. The hidden word is DOCTOR.{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ WRONG WORD.{RESET}")
            time_penalty(30, "Wrong word! Poisonous gas fills the air...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! Time is running out...")
        time.sleep(1)


def puzzle_4():
    clear_screen()
    
    # الكود المستنتج من القصة (1500)
    target_code = [1, 5, 0, 0]
    
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
        print(f"\n{CYAN}THE CLINIC EMERGENCY VAULT{RESET}")
        print(f"\n{WHITE}Match the 4-digit code tied to the countdown of your life:{RESET}\n")

        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")

        print(f"{GRAY}👁  [ Read the story entry carefully... How many minutes and seconds remain ? ]{RESET}\n")
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
                print(f"\n{GREEN}✓ PUZZLE 04 SOLVED. The emergency lock releases!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ INCORRECT COMBINATION.{RESET}")
                time_penalty(30, "The vault alarm screeched! Time is slipping away...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted vault interaction.{RESET}")
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
    print(f"\n{GRAY}The room is silent...{RESET}\n")
    print(f"{DARK_RED}You search the empty corner.{RESET}\n")
    print(f"{GRAY}Nothing useful is here.{RESET}")

    input(f"\n{WHITE}Press ENTER to return...{RESET}")

def empty_corner_level2():
    clear_screen()
    
    # سرد قصصي مرعب بطابع مستشفى مهجور
    slow_print(f"{DARK_RED}{BOLD}You step into the pitch-black corner of the abandoned ward...{RESET}\n", 0.05)
    time.sleep(0.4)
    slow_print(f"{GRAY}Cold, rusted surgical scalpels scatter across the stained floor.{RESET}", 0.04)
    slow_print(f"{GRAY}Your flashbeam shines upon a rotting autopsy table covered in dried IV tubes.{RESET}", 0.04)
    slow_print(f"{GRAY}Pinned to an old patient record file, a bloody medical note remains...{RESET}\n", 0.04)
    time.sleep(0.8)

    # الملاحظة بتصميم ملف طبي مرعب



    print(f"""{RED}{BOLD}
    
        ╔══════════════════════════════════════════════════════╗
        ║               PATIENT LOG - NOTE                     ║
        ║       How to solve the Broken Clock Puzzle:          ║
        ╠══════════════════════════════════════════════════════╣{RESET}""")
    
    slow_print(f"{YELLOW}              1. Look at the clock time....{RESET}", 0.05)
    slow_print(f"{YELLOW}              2. Take the HOUR number....{RESET}", 0.05)
    slow_print(f"{YELLOW}              3. Multiply the hour by 2....{RESET}", 0.05)
    slow_print(f"{YELLOW}              4. Add the MINUTES to the result....{RESET}", 0.05)

    
    print(f"""{RED}{BOLD}        ║                                                      ║
        ║                                                      ║
        ╚══════════════════════════════════════════════════════╝
        {RESET}""")
    print(f"""{RED}{BOLD}

    ╔══════════════════════════════════════════════════════╗
    ║               PATIENT LOG - NOTE 02                  ║
    ╠══════════════════════════════════════════════════════╣{RESET}""")

    slow_print(f"{YELLOW}     'Subject identities have been wiped from the ward...{RESET}", 0.05)
    slow_print(f"{YELLOW}      Every number on the terminal represents a letter{RESET}", 0.05)
    slow_print(f"{YELLOW}      by its numeric position in the alphabet.'{RESET}", 0.05)

    print(f"""{RED}{BOLD}    ║                                                      ║
    ║   [ Example:  A = 1  │  B = 2  │  C = 3 ... ]        ║
    ╚══════════════════════════════════════════════════════╝
    {RESET}""")

    time.sleep(0.5)
    slow_print(f"{DARK_RED}A flatline heart monitor tone hums softly from the shadows...{RESET}", 0.05)
    
    input(f"\n{WHITE}☠ Press ENTER to back away from the operating table...{RESET}")

# GAME LOOP
def game_loop(username):
    while True:
        if remaining_seconds <= 0:
            game_over()
            return "ROOM1"
        clear_screen()
        show_header()

        # واجهة عيادة الدكتور راغب الملعونة
        print(
            f"{B}        🩸   [ CLINIC OF DR. RAGHEB :: EXPERIMENT ROOM ]   🩸{RESET}"
        )
        print(
            f"{D}  -- SCALPEL SOUNDS ECHO THROUGH THE WALLS... THEY WANT REVENGE --{RESET}\n"
        )

        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(
            f"  {R}▲ [LEFT WALL]{RESET}                                              {R}[RIGHT WALL] ▲{RESET}"
        )
        print(
            f"  {Y}[1]{RESET} {CYAN}🛏️  Examine Bloodstained ICU Bed{RESET}             {Y}[2]{RESET} {CYAN}🩸 Inspect Surgical Instruments Table{RESET}\n"
        )

        print(
                    f"                            {B}☠️  FRONT WALL ☠️{RESET}"
                )
        print(
                    f"                {Y}[3]{RESET} {P}     <<< Death Bed >>>{RESET}\n"
                )
        # المركز (جهاز إنعاش المريض الأخير)

        print(
            f"                            {B}☠️  THE LAST VICTIM  ☠️{RESET}"
        )
        print(
            f"                {Y}[4]{RESET} {P}💻 Hack Beeping Life-Support Machine{RESET}\n"
        )

        # القاعدة (خيارات التفاعل والهروب)
        print(
            f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}"
        )
        print(
            f"  {Y}[5]{RESET} {P}🔍 Search Dark Corners{RESET}  │  {Y}[6]{RESET} {P}💡 Decrypt Whispering Spirits{RESET}  │  {Y}[7]{RESET} {B}🚪 Force Heavy Iron Door{RESET}"
        )
        print(
            f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}"
        )
        print(
            f"{B}  🩸  "
            + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2
            + " DR. RAGHEB'S PATIENTS ARE WATCHING YOU "
            + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2
            + f"  🩸{RESET}"
        )

        try:
            choice = int(
                input(
                    f"\n{B}🩸 [15-MIN TIMEOUT] Choose where to step before flatline [1-7]: {RESET}"
                )
            )

            if choice == 1:
                if puzzles_solved[0]:
                    print(
                        f"\n{GREEN}🛏️ The leather straps on the ICU bed are open. Already solved.{RESET}"
                    )
                    time.sleep(1)
                else:
                    puzzle_1()

            elif choice == 2:
                if puzzles_solved[1]:
                    print(
                        f"\n{GREEN}🩸 Dr. Ragheb's rusted scalpels are cleared. Already solved.{RESET}"
                    )
                    time.sleep(1)
                else:
                    puzzle_2()

            elif choice == 3:
                if puzzles_solved[2]:
                    print(f"\n{GREEN}💻 Life-support monitor overridden. Flatline signal disarmed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_3()

            elif choice == 4:
                if puzzles_solved[3]:
                    print(
                        f"\n{GREEN}🛏️ The leather straps on the ICU bed are open. Already solved.{RESET}"
                    )
                    time.sleep(1)  
                else:
                    puzzle_4()            

            elif choice == 5:
                empty_corner()
            elif choice == 6:
                use_hint()
            elif choice == 7:
                print(
                    f"\n{Y}⚠️ THE IRON CLINICAL DOOR WAS RUSTED & LOCKED FROM OUTSIDE!\nTHERE IS NO ESCAPE FROM DR. RAGHEB'S EXPERIMENT.{RESET}"
                )
                time.sleep(2.5)
                continue

            else:
                print(
                    f"\n{R}❌ INVALID INPUT. Agonized screams drown your thoughts...{RESET}"
                )
                time.sleep(1)
                clear_screen()

        except ValueError:
            print(
                f"\n{R}❌ NUMBERS ONLY! The medical monitor rejects your trembling hands.{RESET}"
            )
            time.sleep(1)
            clear_screen()

        if all(puzzles_solved):
            return level_complete(username)

# LEVEL COMPLETE
def level_complete(username):
    global timer_running
    timer_running = False
    # تحديث شارة الغرفة الثانية (room2_badge)
    update_room_badge(username, 2, "SILVER")
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

    type_text(f"{WHITE}The life-support machine unlocked the door...{RESET}", 0.04)
    type_text(f"{GRAY}But the doctor's main inner lab lies ahead.{RESET}", 0.04)

    input(f"\n{WHITE}Press ENTER to continue...{RESET}")
    time.sleep(1)

    from menu import after_level1_room2
    return after_level1_room2(username)

# GAME OVER
def game_over():
    global timer_running
    timer_running = False
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║               FLATLINE DETECTED                  ║
    ║                                                  ║
    ║                  YOU DIED                        ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{DARK_RED}The spirits claimed another patient...{RESET}", 0.04)
    input(f"\n{WHITE}Press ENTER to return...{RESET}")

# ROOM 2 LEVEL 1
def room2_level1(username):
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
# LEVEL 2 PUZZLES (DR. RAGHEB'S INNER LAB)
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
    print(f"\n{CYAN}THE TIME SEQUENCE LOG{RESET}")
    print(f"\n{WHITE}What comes next in this sequence?{RESET}\n")

    print(f"{YELLOW}    J , F , M , A , M , J , J , A , S , O , N , ?{RESET}\n")
    print("-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER THE NEXT LETTER: {RESET}").strip().upper()

        if answer == "D":
            level2_puzzles_solved[0] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED. D is for December!{RESET}")
            time.sleep(1.5)
        else:
            print(f"\n{RED}✗ WRONG LETTER.{RESET}")
            time_penalty(30, "Wrong sequence answer! Time moves against you...")
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
    print(f"\n{CYAN}THE BROKEN CLOCK SYSTEM{RESET}")
    print(f"\n{WHITE}A broken clock is frozen in time. Decode the lock!{RESET}\n")
    print(f"\n{GRAY}👁 [ The terminal seems to rely on a rule hidden around you... ]{RESET}\n")
    print(f"{YELLOW}    The clock stopped at: 10:15{RESET}\n")
    print("-" * 50)

    try:
        answer = input(f"{RED}☠ ENTER THE CODE | TYPE [Q] TO RETURN: {RESET}").strip().upper()

        if answer == "35":
            level2_puzzles_solved[1] = True
            print(f"\n{GREEN}✓ PUZZLE 02 SOLVED. Code 35 accepted!{RESET}")
            time.sleep(1.5)
        elif answer=="Q":
            time.sleep(1.5)
            return
        else:
            print(f"\n{RED}✗ WRONG CODE.{RESET}")
            time_penalty(30, "Wrong code! The clock mechanism locks down...")
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
    print(f"\n{CYAN}THE NUMBER CODE SYSTEM{RESET}")
    print(f"\n{WHITE}Decode the numerical sequence to unlock the terminal:{RESET}\n")
    print(f"\n{GRAY}👁 [ The terminal seems to rely on a rule hidden around you... ]{RESET}\n")
    print(f"{YELLOW}    3 - 15 - 4 - 5{RESET}\n")
    print("-" * 50)
    try:
        answer = input(f"{RED}☠ ENTER THE SECRET WORD: {RESET}").strip().upper()

        if answer == "CODE":
            level2_puzzles_solved[2] = True
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

def level2_puzzle_4():
    clear_screen()
    
    # الكود المستنتج (6111)
    target_code = [6, 0, 1, 5]
    
    # توليد رمز عشوائي للبداية
    current_code = [random.randint(0, 9) for _ in range(4)]
    while current_code == target_code:
        current_code = [random.randint(0, 9) for _ in range(4)]

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 02                       ║
    ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{CYAN}DR. RAGHEB'S PERSONAL SAFE{RESET}")
        print(f"\n{WHITE}Enter the combination based on the mastermind and his last victim:{RESET}\n")

        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")

        print(f"""{GRAY}👁  To break the lock, you must enter the secret 4-digit code left behind:

            Decode the digits (Name Length | Survivors | Time to survive) to unlock your freedom! {RESET}\n""")
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
                print(f"\n{GREEN}✓ PUZZLE 02 SOLVED. The doctor's heavy safe swings open!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ INCORRECT COMBINATION.{RESET}")
                time_penalty(30, "The safe lock jams! Whispers echo inside the walls...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted safe interaction.{RESET}")
            time.sleep(1)
            break
# ROOM 2 LEVEL 2
def room2_level2(username):
    global remaining_seconds
    global level2_hint_used
    global level2_puzzles_solved
    global timer_running
    player_data = get_player_data(username)
    room2_badge = player_data["room2_badge"]
    if room2_badge == "LOCKED":
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
        return "ROOM2"
    
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
    ║               THE INNER LABORATORY               ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}You made it inside Dr. Ragheb's inner laboratory...{RESET}", 0.04)
    type_text(f"{RED}The spirits grow stronger here.{RESET}", 0.04)
    type_text(f"{YELLOW}You have 15 minutes to purge the system and escape.{RESET}", 0.04)

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
        time_penalty(60, "You asked the doctor's server for help...")
        print(f"""{YELLOW}{BOLD}💡 HINT:
        "This sequence doesn't follow an alphabetical pattern, but a natural cycle of 12 steps that repeats every year"{RESET}{GRAY}\nLook at the very first step{RESET}""")
    elif h == "2":
        level2_hint_used = True
        time_penalty(60, "You asked the doctor's server for help...")
        print(f"""{YELLOW}{BOLD}💡 HINT:
        "The hour hand holds double the weight of time."{RESET}{GRAY}\n Weigh the hours first, then add the passage of minutes.{RESET}""")
    elif h == "3":
        level2_hint_used = True
        time_penalty(60, "You asked the doctor's server for help...")
        print(f"""\n{YELLOW}{BOLD}💡 HINT:
        "The key to these numbers isn't in your head—it's written somewhere in this room.{RESET}{GRAY}\nSearch your surroundings for a hidden note before attempting the terminal."{RESET}""")
    elif h == "4":
        level2_hint_used = True
        time_penalty(60, "You asked the doctor's server for help...")
        print(f"\n{YELLOW}💡 HINT FOR THE LOCK:{RESET}")
        print(f"{WHITE}• Digit 1: Letters in 'RAGHEB' (6)")
        print(f"• Digit 2: Patients who survived (0)")
        print(f"• Dials 3-4: Survival time in minutes (15){RESET}")
        print(f"\n{GREEN}👉 Combination: 6 - 0 - 1 - 5{RESET}\n") 
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
            return "ROOM2"
        clear_screen()
        print(f"""{RED}{BOLD}
╔════════════════════════════════════════════════════════════╗
║ ROOM 02 | LEVEL 02 | TIME: {get_time()} | HINT: {'🔒' if level2_hint_used else '🔓'}                 ║
║ PUZZLES: {"✓" if level2_puzzles_solved[0] else "✗"}  {"✓" if level2_puzzles_solved[1] else "✗"}  {"✓" if level2_puzzles_solved[2] else "✗"}  {"✓" if level2_puzzles_solved[3] else "✗"}      ║
╚════════════════════════════════════════════════════════════╝
{RESET}""")

        # واجهة عيادة الدكتور راغب الملعونة
        print(
            f"{B}        🩸   [ CLINIC OF DR. RAGHEB :: EXPERIMENT ROOM ]   🩸{RESET}"
        )
        print(
            f"{D}  -- SCALPEL SOUNDS ECHO THROUGH THE WALLS... THEY WANT REVENGE --{RESET}\n"
        )

        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(
            f"  {R}▲ [LEFT WALL]{RESET}                                              {R}[RIGHT WALL] ▲{RESET}"
        )
        print(
            f"  {Y}[1]{RESET} {CYAN}🛏️  Examine Bloodstained ICU Bed{RESET}             {Y}[2]{RESET} {CYAN}🩸 Inspect Surgical Instruments Table{RESET}\n"
        )
        print(
                    f"                            {B}☠️  FRONT WALL  ☠️{RESET}"
                )
        print(
                    f"                {Y}[3]{RESET} {P}<<<THE DIED BED>>>{RESET}\n"
                )

        # المركز (جهاز إنعاش المريض الأخير)
        print(
            f"                            {B}☠️  THE LAST VICTIM  ☠️{RESET}"
        )
        print(
            f"                {Y}[4]{RESET} {P}💻 Hack Beeping Life-Support Machine{RESET}\n"
        )

        # القاعدة (خيارات التفاعل والهروب)
        print(
            f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}"
        )
        print(
            f"  {Y}[5]{RESET} {P}🔍 Search Dark Corners{RESET}  │  {Y}[6]{RESET} {P}💡 Decrypt Whispering Spirits(HINT){RESET}  │  {Y}[7]{RESET} {B}🚪 Force Heavy Iron Door{RESET}"
        )
        print(
            f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}"
        )
        print(
            f"{B}  🩸  "
            + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2
            + " DR. RAGHEB'S PATIENTS ARE WATCHING YOU "
            + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 2
            + f"  🩸{RESET}"
        )

        try:
            choice = int(
                            input(
                                f"\n{B}🩸 [15-MIN TIMEOUT] Choose where to step before flatline [1-7]: {RESET}"
                            )
                        )

            if choice == 1:
                if level2_puzzles_solved[0]:
                    print(f"\n{GREEN}🛏️ The leather straps on the ICU bed are open. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_1()

            elif choice == 2:
                if level2_puzzles_solved[1]:
                    print(f"\n{GREEN}🩸 Dr. Ragheb's rusted scalpels are cleared. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_2()

            elif choice == 3:
                if level2_puzzles_solved[2]:
                    print(f"\n{GREEN}💻 Life-support monitor overridden. Flatline signal disarmed. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_3()
            elif choice == 4:
                if level2_puzzles_solved[3]:
                    print(f"\n{GREEN}🩸 Dr. Ragheb's rusted scalpels are cleared. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_4()

            elif choice == 5:
                empty_corner_level2()
            elif choice == 6:
               level2_hint()
            elif choice == 7:
                print(
                    f"\n{Y}⚠️ THE IRON CLINICAL DOOR WAS RUSTED & LOCKED FROM OUTSIDE!\nTHERE IS NO ESCAPE FROM DR. RAGHEB'S EXPERIMENT.{RESET}"
                )
                time.sleep(2.5)
                continue
            else:
                print(f"\n{R}❌ INVALID INPUT. Agonized screams drown your thoughts...{RESET}")
                time.sleep(1)
                clear_screen()
        except ValueError:
            print(f"\n{R}❌ NUMBERS ONLY! The medical monitor rejects your trembling hands.{RESET}")
            time.sleep(1)
            clear_screen()
        if all(level2_puzzles_solved):
            return level2_complete(username)

def level2_complete(username):
    global timer_running
    timer_running = False
    update_room_badge(username, 2, "GOLD")
    clear_screen()
    print(f"""\n{GREEN}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║                LEVEL 02 CLEARED                  ║
    ║                                                  ║
    ║                   🥇🏆 GOLD                      ║
    ║                                                  ║
    ║                ROOM 02 COMPLETED                 ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}\n""")
    type_text(f"{WHITE}Dr. Ragheb's experiment is finally terminated...{RESET}", 0.04)
    type_text(f"{GRAY}The spirits are at peace.{RESET}", 0.04)

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

# MAIN ROOM ENTRY POINT
def room2(username):
    return room2_level1(username)