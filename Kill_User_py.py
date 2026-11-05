#file Kill_User_py.py
import os
import time
import threading
import sys
from player_data import update_room_badge, get_player_data
from music_of_game import stop_menu_music
import pygame
import random
pygame.mixer.init()

sound1 = r"C:\Users\Compu City\Downloads\Kill_User Voiceover No wistle.mp3"
sound2 = r"C:\Users\Compu City\Downloads\Kill_User_Background_no_whistle.mp3"

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

 # ألوان الرعب والسايبر
R = "\033[91m"     # أحمر ساطع
B = "\033[31m"     # أحمر دموي
P = "\033[95m"     # أرجواني ملعون
Y = "\033[93m"     # أصفر تحذيري
D = "\033[90m"     # رمادي مظلم


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

# HORROR WORD
def horror_word(word):
    clear_screen()
    print("\n")
    for i in range(3):
        print(f"{RED}{BOLD}", end="")
        if i % 2 == 0:
            print("\n")
            print(" " * 15 + word)
            print("\n")
        else:
            print("\n")
            print(" " * 10 + "█ " + word + " █")
            print("\n")
        print(RESET, end="")
        time.sleep(0.3)
        clear_screen()

# INTRO SCREEN
def intro_screen():
    clear_screen()
    for i in range(6):
        clear_screen()
        if i % 2 == 0:
            print(f"""{RED}{BOLD}
             ██████╗ ██╗   ██╗███╗   ██╗    ███╗   ██╗ ██████╗ ██╗    ██╗
             ██╔══██╗██║   ██║████╗  ██║    ████╗  ██║██╔═══██╗██║    ██║
             ██████╔╝██║   ██║██╔██╗ ██║    ██╔██╗ ██║██║   ██║██║ █╗ ██║
             ██╔══██╗██║   ██║██║╚██╗██║    ██║╚██╗██║██║   ██║██║███╗██║
             ██║  ██║╚██████╔╝██║ ╚████║    ██║ ╚████║╚██████╔╝╚███╔███╔╝
             ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝
            \n                 KILL_USER.PY")\n{RESET}""")
        else:
            print(f"""{DARK_RED}{BOLD}\n
            
                        [ SYSTEM ERROR ]
                        [ UNKNOWN FILE ]
                        [ USER LOCKED! ] 
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

def play_story():

    # ================= SOUND =================
    music_thread = threading.Thread(
        target=play_background_music,
        daemon=True)
    music_thread.start()
    stop_menu_music()


    # ================= STORY =================

    print(f"""{RED}{BOLD}

    ╔══════════════════════════════════════════════════╗
    ║                 KILL_USER.PY                     ║
    ╚══════════════════════════════════════════════════╝

    {RESET}""")
    type_text(
        f"\nIn 2023,{GRAY} a programmer named {RED}{BOLD}Tarek{RESET}\n"
        f"{GRAY}was working on a strange piece of code.{RESET}\n",
        0.05)
    type_text(
        f"{YELLOW}And no one understood its purpose...{RESET}\n",
        0.052)
    type_text(
        f"{GRAY}A code that could extract data from places\n"
        f"that were not connected to the internet!{RESET}\n",
        0.048
    )


    # 2. ليلة التسليم وصراخ الجيران والشرطة

    type_text(
        f"{GRAY}On the night of delivering the project,\n"
        f"the neighbors heard...{RESET}\n"
        f"{RED}{BOLD}TERRIFYING SCREAMS...{RESET}\n",
        0.042
    )

    type_text(
        f"{WHITE}Coming from his office.\n"
        f"When the police entered, they found "
        f"{RESET}{RED}{BOLD}Tarek DEAD.{RESET}\n",
        0.042
    )


    # 3. العثور على الجثة والشاشة

    type_text(
        f"{GRAY}He was sitting in his chair...\n"
        f"His eyes open,\n"
        f"Staring directly at the screen...\n"
        f"Which was printing one repeating line of Python code "
        f"without stopping...{RESET}\n",
        0.038
    )

    type_text(
        f"{RED}{BOLD}while True:\n"
        f"    kill user{RESET}\n",
        0.035
    )


    time.sleep(0.7)


    type_text(
        f"{GRAY}The security forces closed the room and deleted the files.{RESET}\n"
        f"{RED}But...\n"
        f"{BOLD}THE MAIN SERVER WAS STILL RUNNING.{RESET}\n",
        0.05
    )


    # 5. الدخول للغرفة وانقطاع الأنوار

    time.sleep(0.7)

    type_text(
        f"{WHITE}You entered the room to recover the code,\n"
        f"but the door electronically locked and the lights went out!{RESET}\n",
        0.05
    )


    # --- الجزء الأخير بالسرعة المتوسطة المثالية ---

    time.sleep(0.5)

    type_text(
        f"{RED}{BOLD}The code is not just a program.\n"
        f"THE CODE IS AN ENTITY PROGRAMMED TO KILL.{RESET}\n",
        0.05
    )


    time.sleep(0.5)


    type_text(
        f"{RED}And the screen turned on right now, saying:\n"
        f"New Users Detected.\n"
        f"Execution in 15 Minutes.{RESET}\n",
        0.045
    )


    time.sleep(0.55)


    type_text(
        f"{YELLOW}You have 15 minutes to find the bug\n"
        f"and overwrite the program,{RESET}\n",
        0.060
    )


    time.sleep(0.45)


    type_text(
        f"{GRAY}Otherwise...{RESET}\n",
        0.15
    )


    time.sleep(0.5)


    type_text(
        f"{RED}{BOLD}{BLINK}"
        f"THE SERVER WILL LOCK THE ROOM FOREVER."
        f"{RESET}\n",
        0.055
    )


    time.sleep(0.4)


    input(
        f"{YELLOW}Press ENTER to enter the system...{RESET}"
    )
# LEVEL START
def level_start(username):
    global timer_running
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  LEVEL 01                        ║
    ║                 THE SERVER                       ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}The server has started...{RESET}",0.03)
    type_text(f"{RED}You have 15 minutes to escape.{RESET}\n",0.03)
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
    thread = threading.Thread( target=timer_thread,daemon=True)
    thread.start()

def get_time():
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# HEADER
def show_header():
    hint_status = "🔒" if hint_used else "🔓"
    puzzle_status = []
    for solved in puzzles_solved:
        if solved:
            puzzle_status.append("✓")
        else:
            puzzle_status.append("✗")

    print(f"""{RED}{BOLD}
    ╔════════════════════════════════════════════════════════════
    ║ ROOM 01 | LEVEL 01 | TIME: {get_time()} | HINT: {hint_status}               ║
    ║ PUZZLES: {puzzle_status[0]}  {puzzle_status[1]}  {puzzle_status[2]}   {puzzle_status[3]}                                       ║
    ╚════════════════════════════════════════════════════════════
    {RESET}""")

# =========================================================
def time_penalty(seconds, reason):
    global remaining_seconds
    remaining_seconds -= seconds
    if remaining_seconds < 0:
        remaining_seconds = 0
    clear_screen()
  
    print(f"""\n{RED}{BOLD}{BLINK}
                    ⚠  SYSTEM PENALTY  ⚠{RESET}\n""")
    
    type_text(f"{RED}{reason}{RESET}",0.04)

    type_text(f"\n{YELLOW}TIME LOST: {seconds} SECONDS{RESET}",0.04)

    type_text(f"{GRAY}\nThe server is getting impatient...{RESET}",0.04)

    time.sleep(2)

# HINT
def available_hints(puzzles):
    for number, solved in enumerate(puzzles, start=1):
        if not solved:
            yield number
def use_hint():
    global hint_used
    if hint_used:
        print(f"\n{RED}{BOLD}⚠ THE SYSTEM HAS ALREADY GIVEN YOU ONE HINT.{RESET}" )
        print(f"{GRAY}You cannot ask for another hint in this level.{RESET}")
        time.sleep(2)
        return
    
    print(f"""{YELLOW}{BOLD}\n
        ╔════════════════════════════════════════════╗
        ║              CHOOSE YOUR HINT              ║
        ╚════════════════════════════════════════════╝{RESET}""")
    print(f"\n{WHITE}")
    for number in available_hints(puzzles_solved):
        print(f"        {number} - [Puzzle {number:02d}]")

    print(f"{RESET}\n")    
    h=input(f"{YELLOW}Which question would you like help with? >>> {RESET}" )
    if h == "1":
        hint_used = True
        time_penalty(60, "You asked the system for help..." )
        print(f"""{YELLOW}{BOLD}
            \nHINT FOR QUESTION 1:{RESET}""")
        #hint1
        print(f"""{GRAY}
             Changing a string doesn't always change the original. Did you save the result of replace() anywhere?
            {RESET}""")

    elif h == "2":
        hint_used = True
        time_penalty(60,"You asked the system for help...")
        print(f"""{YELLOW}{BOLD}
            \nHINT FOR QUESTION 2:
            {RESET}""")
        #hint2
        print(f"""{GRAY} 
            99 is just a distraction... the loop has other plans for i
            {RESET}""")
        
    elif h == "3":
        hint_used = True
        time_penalty(60,"You asked the system for help...")

        print(f"""{YELLOW}{BOLD}
            \nHINT FOR QUESTION 3:
            {RESET}""")
        #hint3
        print(f"""{GRAY}
            If the key cannot be found, what negative number tells you it doesn't exist?
            {RESET}""")
    elif h == "4":
            hint_used = True
            time_penalty(60,"You asked the system for help...")
            print(f"""{YELLOW}{BOLD}
                \nHINT FOR QUESTION 4:
                {RESET}""")
            #hint2
            print(f"""{GRAY} 
                Look at the year 2023. Take the last digit '3' and convert it to 4-bit binary code (8-4-2-1 sequence)
                {RESET}""")    
        
        
    else:
        print(f"\n{RED}❌ Please choose 1, 2, or 3.{RESET}")
        time.sleep(2)
        return
    
    print(f"""\n{RED}{BOLD}
        ⚠ YOUR ONE HINT HAS BEEN USED.
        {RESET}""")
    
    input(f"\n{GRAY}Press ENTER to continue...{RESET}")

# PUZZLE 1
def puzzle_1():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 01                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    #Q1
    print(f"\n{WHITE}The program contains a hidden condition.{RESET}")
    print("\nWhat exact word will print on the screen?\n")

    print(f'{WHITE}Code executed:{RESET}')
    print('   status = "DEAD"')
    print('   status.replace("DEAD", "ALIVE")')
    print('   print(status)')
    print()

    try:
        answer = input(f"{RED}☠ ENTER THE PRINTED STATUS: {RESET}").strip()

        if answer == "DEAD":
            puzzles_solved[0] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)

        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30, "Wrong answer! The server has detected your mistake...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! The server is losing patience...")
        time.sleep(1)

# PUZZLE 2
def puzzle_2():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 02                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    #Q2 
    print(f"\n{CYAN}THE EVIL SCOPE TRAP{RESET}")
    print(f"\n{WHITE}What INTEGER number will print on the screen?{RESET}\n")

    print(f"{YELLOW}Code executed:{RESET}")
    print(f"{GRAY}   i = 99{RESET}")
    print(f"{GRAY}   for i in range(5):{RESET}")
    print(f"{GRAY}       pass{RESET}")
    print(f"{GRAY}   print(i){RESET}")
    print()

    try:
        answer = input(f"{RED}☠ ENTER THE VALUE OF i: {RESET}").strip()

        if answer == "4":
            puzzles_solved[1] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)

        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30, "Wrong answer! The server has detected your mistake...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30, "Invalid input! The server is losing patience...")
        time.sleep(1)

# PUZZLE 3
def puzzle_3():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 03                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    #Q3
    print(f"\n{CYAN}SEARCH FOR THE KEY... TIME IS BLEEDING OUT{RESET}")
    print(f"\n{WHITE}What INTEGER number will print on the screen?{RESET}\n")
    print(f"{YELLOW}Code executed:{RESET}")
    print(f"{GRAY}   log = \"ERROR_SYSTEM_FAILURE_NO_ACCESS\"{RESET}")
    print(f"{GRAY}   code = log.find(\"KEY\"){RESET}")
    print(f"{GRAY}   print(code){RESET}\n")

    try:
        answer = input(f"{RED}☠ ENTER THE OUTPUT: {RESET}").strip()
        if answer == "-1":
            puzzles_solved[2] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)
        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30,"Wrong answer! The server has detected your mistake...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30,"Invalid input! The server is losing patience...")
        time.sleep(1)

def puzzle_4():
    clear_screen()
    
    # الرقم 3 (آخر رقم في سنة 2023) بالباينري هو 0011
    target_code = [0, 0, 1, 1]
    
    # بداية القفل بقيم عشوائية بين 0 و 1
    current_code = [random.choice([0, 1]) for _ in range(4)]
    while current_code == target_code:
        current_code = [random.choice([0, 1]) for _ in range(4)]

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 04                       ║
    ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{CYAN}THE BINARY YEAR TERMINAL{RESET}")
        print(f"\n{WHITE}Toggle the 4 binary bits (0 or 1) to match the final digit of the project's year:{RESET}\n")

        # واجهة عرض الباينري (0 و 1 فقط)
        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")

       
        print("-" * 50)
        print(f"{WHITE}Controls:{RESET}")
        print(f"  {CYAN}[1, 2, 3, 4]{RESET} Switch bit 1, 2, 3, or 4 (0 ⟷ 1)")
        print(f"  {GREEN}[S]{RESET} Submit Binary Signal")
        print(f"  {RED}[Q]{RESET} Quit Attempt\n")

        choice = input(f"{RED}☠ Choose action: {RESET}").strip().lower()

        if choice in ['1', '2', '3', '4']:
            idx = int(choice) - 1
            # تبديل القيمة بين 0 و 1 فقط
            current_code[idx] = 1 if current_code[idx] == 0 else 0

        elif choice == 's':
            if current_code == target_code:
                puzzles_solved[3] = True
                print(f"\n{GREEN}✓ PUZZLE 04 SOLVED. Binary signal accepted!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ INVALID BINARY SIGNAL.{RESET}")
                time_penalty(30, "Syntax Error! Server initiates emergency purge...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted binary terminal interaction.{RESET}")
            time.sleep(1)
            break        
#EMPTY CORNER
def empty_corner():
    clear_screen()
    print(f"\n{GRAY}The room is silent...{RESET}\n")
    print(f"{DARK_RED}You search the empty corner.{RESET}\n")
    print(f"{GRAY}Nothing useful is here.{RESET}")

    input(f"\n{WHITE}Press ENTER to return...{RESET}")


def slow_print(text, delay=0.04):
    """دالة لطباعة النص حرفاً بحرف لإعطاء تأثير التشويق والرعب"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def empty_corner_1():
    clear_screen()
    
    # أجواء استكشاف مرعبة ومظلمة
    slow_print(f"{DARK_RED}{BOLD}You creep through the pitch-black server room...{RESET}", 0.05)
    slow_print(f"{GRAY}The thick smell of burnt electronics and blood hangs heavy in the air.{RESET}", 0.04)
    slow_print(f"{GRAY}Cold blue terminal lights illuminate Tarek's empty chair.{RESET}", 0.04)
    slow_print(f"{GRAY}Taped right beside his dead, wide-open eyes is a blood-stained sticky note...{RESET}\n", 0.04)
    time.sleep(0.8)

    # النوتة المكتوبة بخط اليد مع جدول التتبع الثنائي
    print(f"""{RED}{BOLD}
    ╔═════════════════════════════════════════════════════════════════════╗
    ║                 TAREK'S DESPERATE CHEAT SHEET                       ║
    ╠═════════════════════════════════════════════════════════════════════╣{RESET}""")

    slow_print(f"{YELLOW}       'If you are reading this, the system has already targeted you...{RESET}", 0.05)
    slow_print(f"{YELLOW}        The lock doesn't take decimals. It only takes BITS (0 or 1).{RESET}", 0.05)
    slow_print(f"{YELLOW}        Each dial represents a value in order from left to right: [8 - 4 - 2 - 1]{RESET}\n", 0.05)

    print(f"""{CYAN}{BOLD}
        ┌─────────────────────────────────────────────────────────────────┐
        │  HOW TO CONVERT ANY NUMBER USING THE 4-BIT TABLE:               │
        ├─────────────┬───────┬───────┬───────┬───────┬───────────────────┤
        │ Target Num  │ Bit 8 │ Bit 4 │ Bit 2 │ Bit 1 │ Calculation       │
        ├─────────────┼───────┼───────┼───────┼───────┼───────────────────┤
        │   To make 6 │   0   │   1   │   1   │   0   │  (4 + 2 = 6)      │
        │   To make 9 │   1   │   0   │   0   │   1   │  (8 + 1 = 9)      │
        └─────────────┴───────┴───────┴───────┴───────┴───────────────────┘{RESET}""")

    print(f"""{RED}{BOLD}
        ║                                                                 ║
        ║   RULE: Turn ON (1) the slots you need to reach your total sum. ║
        ║         Turn OFF (0) any slot you don't use.                    ║
        ║                                                                 ║
        ║   "MEMORIZE THIS IN YOUR MIND... BEFORE IT ERASES YOU!"         ║
        ╚═════════════════════════════════════════════════════════════════╝
    {RESET}""")

    time.sleep(0.6)
    slow_print(f"{DARK_RED}A low, inhuman whisper echoes through the server speakers...{RESET}", 0.05)
    slow_print(f"{RED}\"EXECUTION TIMER IS TICKING... HAS YOUR MIND SAVED THE KEY?\"{RESET}\n", 0.06)
    
    input(f"{WHITE}☠ Memorize the formula and press ENTER to step back...{RESET}")

# GAME LOOP
def game_loop(username):
    while True:
        if remaining_seconds <= 0:
            game_over()
            return "ROOM1"
        clear_screen()
        show_header()

        # واجهة الغرفة الملعونة - توزيع خريطة التيرمينال
        print(f"{B}         👁️   [ SYSTEM ERROR: ENTITY DETECTED IN ROOM 01 ]   👁️{RESET}")
        print(f"{D}  01001000 01000101 01001100 01000000 -- IT WANTS YOUR CODE -- 01001000{RESET}\n")

        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(f"  {R}▲ [TOP LEFT]{RESET}                                                 {R}[TOP RIGHT] ▲{RESET}")
        print(f"  {Y}[1]{RESET} {CYAN}🖥️  Inspect Main Cyber Terminal{RESET}                 {Y}[2]{RESET} {CYAN}🩸 Examine Bloody Server Rack{RESET}\n")

        # المركز (قلب السيرفر الملعون)
        print(f"                          {B}☠️  THE CURSED CORE  ☠️{RESET}")
        print(f"                    {Y}[3]{RESET} {P}⌨️  Hack Abandoned Desk{RESET}")
        print(f"                    {Y}[4]{RESET} {P}💻 Inspect Corrupted System Logs{RESET}\n")

        # القاعدة (خيارات التفاعل والهروب)
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"  {Y}[5]{RESET} {P}🔍 Search Dark Corners{RESET}  │  {Y}[6]{RESET} {P}💡 Decrypt Hint{RESET}  │  {Y}[7]{RESET} {B}🚪 Force Escape{RESET}")
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"{B}  🩸  " + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 3 + " HE SEES YOU " + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 3 + f"  🩸{RESET}")




        try:
            choice = int(input(f"\n{B}🩸 [INPUT REQUIRED] Select a coordinate to explore [1-7]: {RESET}"))
            if choice == 1:
                if puzzles_solved[0]:
                    print(f"\n{GREEN}💻 Main Terminal screen bleeds black. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_1()
            elif choice == 2:
                if puzzles_solved[1]:
                    print(f"\n{GREEN}🩸 Server Rack wires are severly cut. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_2()
            elif choice == 3:
                if puzzles_solved[2]:
                    print(f"\n{GREEN}⌨️ Programmer Desk is stained in crimson. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_3()
            elif choice == 4:
                if puzzles_solved[3]:
                    print(f"\n{GREEN}  💻 Inspect Corrupted System Logs. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    puzzle_4()        
            elif choice == 5:
                empty_corner_1()
            elif choice == 6:
                use_hint()
            elif choice == 7:
                print(f"\n{Y}⚠️ THE STEEL DOOR WAS ALREADY LOCKED!\nONCE YOU ENTER THIS DIGITAL HELL, THERE'S NO RETURN.{RESET}")
                time.sleep(2.5)
                continue
            else:
                print(f"\n{R}❌ INVALID INPUT. Screams echo through the terminal...{RESET}")
                time.sleep(1)
                clear_screen()
        except ValueError:
            print(f"\n{R}❌ ENTER A NUMBER! The entity hates unknown characters.{RESET}")
            time.sleep(1)
            clear_screen()
        if all(puzzles_solved):
            return level_complete(username)

# LEVEL COMPLETE
def level_complete(username):
    global timer_running
    timer_running = False
    update_room_badge(username,1,"SILVER")
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

    type_text(f"{WHITE}The system has been unlocked...{RESET}",0.04)
    type_text(f"{GRAY}But something is still running in the background.{RESET}",0.04)

    input(f"\n{WHITE}Press ENTER to continue...{RESET}")
    time.sleep(1)

    # IMPORTANT:Local import prevents circular import error.
    from menu import after_level1
    return after_level1(username)

# GAME OVER
def game_over():
    global timer_running
    timer_running = False
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║                  TIME'S UP                       ║
    ║                                                  ║
    ║              SYSTEM LOCKED                       ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{DARK_RED}The server won this time...{RESET}",0.04)

    input(f"\n{WHITE}Press ENTER to return...{RESET}")

# ROOM 1 LEVEL 1
def room1_level1(username):
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
# LEVEL 2 PUZZLES
# =========================================================

level2_puzzles_solved = [False, False, False,False]
level2_hint_used = False


# PUZZLE 1 - LEVEL 2
def level2_puzzle_1():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 01                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}IT'S A MAP... BUT THE PATH IS EMPTY{RESET}")
    print(f"\n{WHITE}What INTEGER number will print on the screen?{RESET}\n")
    print(f"{YELLOW}Code executed:{RESET}")
    print(f"{GRAY}   rooms = map(int, [\"1\", \"2\", \"3\"]){RESET}")
    print(f"{GRAY}   first_scan = list(rooms){RESET}")
    print(f"{GRAY}   second_scan = list(rooms){RESET}")
    print(f"{GRAY}   print(len(second_scan)){RESET}\n")
    try:
        answer = input(f"{RED}☠ ENTER THE OUTPUT: {RESET}").strip()
        if answer == "0":
            level2_puzzles_solved[0] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)
        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30,"Wrong answer! The server has detected your mistake...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30,"Invalid input! The server is losing patience...")
        time.sleep(1)

# PUZZLE 2 - LEVEL 2
def level2_puzzle_2():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 02                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    print(f"\n{CYAN}THE MUTATING LOOP GHOST{RESET}")
    print(f"\n{WHITE}What list remains after the loop finishes?{RESET}\n")
    print(f"{YELLOW}Code executed:{RESET}")
    print(f"{GRAY}   nums = [1, 2, 3, 4]{RESET}")
    print(f"{GRAY}   for x in nums:{RESET}")
    print(f"{GRAY}       nums.remove(x){RESET}")
    print(f"{GRAY}   print(nums){RESET}\n")
    
    try:
        answer = input(f"{RED}☠ ENTER THE REMAINING LIST: {RESET}").strip().replace(" ", "")
        if answer == "[2,4]":
            level2_puzzles_solved[1] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)
        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30,"Wrong answer! The ghost has shifted the list again...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30,"Invalid input! The server is losing patience...")
        time.sleep(1)
# PUZZLE 3 - LEVEL 2
def level2_puzzle_3():
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                    PUZZLE 03                     ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")

    print(f"\n{CYAN}SHALLOW COPY PHANTOM{RESET}")
    print(f"\n{WHITE}What is the final value of 'a'?{RESET}\n")
    print(f"{YELLOW}Code executed:{RESET}")
    print(f"{GRAY}   a = [[1]]{RESET}")
    print(f"{GRAY}   b = a.copy(){RESET}")
    print(f"{GRAY}   b[0].append(2){RESET}")
    print(f"{GRAY}   print(a){RESET}\n")
    
    try:
        answer = input(f"{RED}☠ ENTER THE LIST 'a': {RESET}").strip().replace(" ", "")
        if answer == "[[1,2]]":
            level2_puzzles_solved[2] = True
            print(f"\n{GREEN}✓ PUZZLE 01 SOLVED.{RESET}")
            time.sleep(1)
        else:
            print(f"\n{RED}✗ WRONG ANSWER.{RESET}")
            time_penalty(30,"Wrong answer! The phantom is still sharing the same memory...")
            time.sleep(1)

    except ValueError:
        print(f"\n{RED}✗ INVALID INPUT.{RESET}")
        time_penalty(30,"Invalid input! The phantom is losing patience...")
        time.sleep(1)

def level2_puzzle_4():
    clear_screen()
    
    # الرقم 5 (عدد حروف TAREK) بالباينري هو (0101)
    target_code = [0, 1, 0, 1]
    
    # بداية القفل بقيم عشوائية بين 0 و 1
    current_code = [random.choice([0, 1]) for _ in range(4)]
    while current_code == target_code:
        current_code = [random.choice([0, 1]) for _ in range(4)]

    while True:
        clear_screen()
        print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                  PUZZLE 04                       ║
    ╚══════════════════════════════════════════════════╝
        {RESET}""")
        print(f"\n{CYAN}TAREK'S ENCRYPTED CORE SAFE{RESET}")
        print(f"\n{WHITE}Enter the binary key representing the programmer's name length :{RESET}\n")

        print(f"{YELLOW}         ┌───┬───┬───┬───┐{RESET}")
        print(f"{YELLOW}         │ {current_code[0]} │ {current_code[1]} │ {current_code[2]} │ {current_code[3]} │{RESET}")
        print(f"{YELLOW}         └───┴───┴───┴───┘{RESET}\n")
        print("-" * 50)
        print(f"{WHITE}Controls:{RESET}")
        print(f"  {CYAN}[1, 2, 3, 4]{RESET} Toggle bit 1, 2, 3, or 4 (0 ⟷ 1)")
        print(f"  {GREEN}[S]{RESET} Submit Binary Key")
        print(f"  {RED}[Q]{RESET} Quit Attempt\n")

        choice = input(f"{RED}☠ Choose action: {RESET}").strip().lower()

        if choice in ['1', '2', '3', '4']:
            idx = int(choice) - 1
            current_code[idx] = 1 if current_code[idx] == 0 else 0

        elif choice == 's':
            if current_code == target_code:
                level2_puzzles_solved[3] = True
                print(f"\n{GREEN}✓ PUZZLE 04 SOLVED. Encrypted core unlocked!{RESET}")
                time.sleep(1.5)
                break
            else:
                print(f"\n{RED}✗ ACCESS DENIED.{RESET}")
                time_penalty(30, "System breach detected! The server locks down tighter...")
                time.sleep(1.5)

        elif choice == 'q':
            print(f"\n{YELLOW}Aborted core safe interaction.{RESET}")
            time.sleep(1)
            break        

# ROOM 1 LEVEL 2
def room1_level2(username):

    global remaining_seconds
    global level2_hint_used
    global level2_puzzles_solved
    global timer_running
    player_data = get_player_data(username)
    room1_badge = player_data["room1_badge"]
    if room1_badge == "LOCKED":
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
        return "ROOM1"

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
    level2_puzzles_solved = [False, False, False, False]
    timer_running = False
    clear_screen()
    print(f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║                    LEVEL 02                      ║
    ║                                                  ║
    ║                    THE CORE                      ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}""")
    type_text(f"\n{GRAY}You thought you escaped...{RESET}",0.04)
    type_text(f"{RED}But the system is still running.{RESET}",0.04)
    type_text(f"{YELLOW}You have 15 minutes to shut it down.{RESET}",0.04)

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
        time_penalty(60,"You asked the system for help...")

        print(f"""{YELLOW}{BOLD}
            HINT FOR QUESTION 1:{RESET}{GRAY}\n
        You scanned the map once already... what happens when you try to walk the same path again?{RESET}""")
    elif h == "2":
        level2_hint_used = True
        time_penalty(60,"You asked the system for help...")
        print(f"""{YELLOW}{BOLD}
            HINT FOR QUESTION 2:{RESET}{GRAY}\n
        What happens when the ghost removes one item... but the loop moves to the next position anyway?{RESET}""")

    elif h == "3":
        level2_hint_used = True
        time_penalty(60,"You asked the system for help...")
        print(f"""\n{YELLOW}{BOLD}
            HINT FOR QUESTION 3:{RESET}{GRAY}\n
        a.copy() creates a new outer list, but both lists still share the same inner list.\n{RESET}""")
    elif h == "4":
            level2_hint_used = True
            time_penalty(60,"You asked the system for help...")
            print(f"""\n{YELLOW}{BOLD}
                HINT FOR QUESTION 3:{RESET}{GRAY}\n
            "Count the letters in 'TAREK'. Translate the number 5 into binary code using 4 bits (e.g., 8-4-2-1 values)."\n{RESET}""")
    else:
        print(f"\n{RED}❌ Please choose 1, 2, or 3.{RESET}")
        time.sleep(2)
        return
    print(f"""\n{RED}{BOLD}
    ⚠ YOUR ONE HINT HAS BEEN USED.\n{RESET}""")

    input(f"\n{GRAY}Press ENTER to continue...{RESET}")

def level2_game_loop(username):
    while True:
        if remaining_seconds <= 0:
            game_over()
            return "ROOM1"
        clear_screen()
        print(f"""{RED}{BOLD}
╔════════════════════════════════════════════════════════════╗
║ ROOM 01 | LEVEL 02 | TIME: {get_time()} | HINT: {'🔒' if level2_hint_used else '🔓'}                 ║
║ PUZZLES: {"✓" if level2_puzzles_solved[0] else "✗"}  {"✓" if level2_puzzles_solved[1] else "✗"}  {"✓" if level2_puzzles_solved[2] else "✗"}   {"✓" if level2_puzzles_solved[3] else "✗"}     ║
╚════════════════════════════════════════════════════════════╝
{RESET}""")

    # واجهة الغرفة الملعونة - توزيع خريطة التيرمينال
        print(f"{B}         👁️   [ SYSTEM ERROR: ENTITY DETECTED IN ROOM 01 ]   👁️{RESET}")
        print(f"{D}  01001000 01000101 01001100 01000000 -- IT WANTS YOUR CODE -- 01001000{RESET}\n")

        # الزاوية الأولى (يسار) والزاوية الثانية (يمين)
        print(f"  {R}▲ [TOP LEFT]{RESET}                                                 {R}[TOP RIGHT] ▲{RESET}")
        print(f"  {Y}[1]{RESET} {CYAN}🖥️  Inspect Main Cyber Terminal{RESET}                 {Y}[2]{RESET} {CYAN}🩸 Examine Bloody Server Rack{RESET}\n")

        # المركز (قلب السيرفر الملعون)
        print(f"                          {B}☠️  THE CURSED CORE  ☠️{RESET}")
        print(f"                    {Y}[3]{RESET} {P}⌨️  Hack Abandoned Desk{RESET}")
        print(f"                    {Y}[4]{RESET} {P}💻 Inspect Corrupted System Logs{RESET}\n")

        # القاعدة (خيارات التفاعل والهروب)
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"  {Y}[5]{RESET} {P}🔍 Search Dark Corners{RESET}  │  {Y}[6]{RESET} {P}💡 Decrypt Hint{RESET}  │  {Y}[7]{RESET} {B}🚪 Force Escape{RESET}")
        print(f"  {D}─────────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"{B}  🩸  " + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 3 + " HE SEES YOU " + "̴̡̢̛̲͖̲̲̲̝͇̲̲͈̦" * 3 + f"  🩸{RESET}")

       
        try:
            choice = int(input(f"\n{B}🩸 [INPUT REQUIRED] Select a coordinate to explore [1-7]: {RESET}"))

            if choice == 1:
                if level2_puzzles_solved[0]:
                    print(f"\n{GREEN}💻 Main Terminal screen bleeds black. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_1()

            elif choice == 2:
                if level2_puzzles_solved[1]:
                    print(f"\n{GREEN}🩸 Server Rack wires are severly cut. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_2()

            elif choice == 3:
                if level2_puzzles_solved[2]:
                    print(f"\n{GREEN}⌨️ Programmer Desk is stained in crimson. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_3()
            elif choice == 4:
                if level2_puzzles_solved[3]:
                    print(f"\n{GREEN}  💻 Inspect Corrupted System Logs. Already solved.{RESET}")
                    time.sleep(1)
                else:
                    level2_puzzle_4() 

            elif choice == 5:
                empty_corner()
            elif choice == 6:
                level2_hint()

          
            elif choice == 7:
                print(f"\n{Y}⚠️ THE STEEL DOOR WAS ALREADY LOCKED!\nONCE YOU ENTER THIS DIGITAL HELL, THERE'S NO RETURN.{RESET}")
                time.sleep(2.5)
                continue
                
            else:
                print(f"\n{R}❌ INVALID INPUT. Screams echo through the terminal...{RESET}")
                time.sleep(1)
                clear_screen()
        except ValueError:
            print(f"\n{R}❌ ENTER A NUMBER! The entity hates unknown characters.{RESET}")
            time.sleep(1)
            clear_screen()

        if all(level2_puzzles_solved):
            return level2_complete(username)

def level2_complete(username):
    global timer_running
    timer_running = False
    update_room_badge(username,1,"GOLD")
    clear_screen()
    print(f"""\n{GREEN}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║                LEVEL 02 CLEARED                  ║
    ║                                                  ║
    ║                   🥇🏆 GOLD                      ║
    ║                                                  ║
    ║                ROOM 01 COMPLETED                 ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    {RESET}\n""")
    type_text(f"{WHITE}The system has been shut down...{RESET}",0.04)
    type_text(f"{GRAY}But was it really...?{RESET}",0.04)

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


# ROOM 1
def room1(username):
    return room1_level1(username)