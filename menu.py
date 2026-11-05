#file menu.py
from Kill_User_py import room1, room1_level2
from dr_ragheb import room2, room2_level2
from dar_al_noor import room3, room3_level2
from music_of_game import start_menu_music
import csv
import os
import time

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

FILE_NAME = "users.csv"

# MAIN MENU
def menu(username):

    
    while True:
        start_menu_music()
        clear_screen()
        print(f"""{RED}{BOLD}
        ╔══════════════════════════════════════════════════╗
        ║                    MAIN MENU                     ║
        ╚══════════════════════════════════════════════════╝{RESET}""")
        print(f"\n{WHITE}[1] Explore Rooms{RESET}\n{WHITE}[2] My Profile{RESET}\n{WHITE}[3] How to Play{RESET}\n{WHITE}[4] Logout{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ CHOOSE AN OPTION: {RESET}"))
            if choice == 1:
                explore_room(username)
                continue
            elif choice == 2:
                clear_screen()
                show_profile(username)
            elif choice == 3:
                how()
            elif choice == 4:
                logout()
                return
            else:
                print(f"{RED}❌ INVALID CHOICE.{RESET}")
                time.sleep(1)
        except ValueError:
            print( f"{RED}❌ PLEASE ENTER A NUMBER.{RESET}")
            time.sleep(1)

# CLEAR SCREEN
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_horror_messages(*messages, **options):
    color = options.get("color", WHITE)
    prefix = options.get("prefix", "")
    for message in messages:
        print(f"{color}{prefix}{message}{RESET}")

def type_text(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
def loading_effect():
    print()
    for i in range(3):
        print(RED + "ACCESSING NIGHTMARE" + "." * (i + 1) + RESET, end="\r")
        time.sleep(0.5)
    print(" " * 40, end="\r")
def glitch_effect():
    clear_screen()
    glitch_words = [
        "𝐂𝐚𝐭𝐜𝐡 𝐔𝐬 𝐈𝐟 𝐘𝐨𝐮 𝐂𝐚𝐧🔪",
        "☠ YOU ARE NOT ALONE ☠",
        "⚠ DO NOT OPEN THE DOOR ⚠",
        "👁 IT KNOWS YOUR NAME",
        "⚠ DON'T LOOK BACK ⚠"
        "𝐂𝐚𝐭𝐜𝐡 𝐔𝐬 𝐈𝐟 𝐘𝐨𝐮 𝐂𝐚𝐧🔪"
    ]
    for word in glitch_words:
        print(RED + BLINK + ">>> " + word + " <<<" + RESET,flush=True)
        time.sleep(0.35)
    time.sleep(0.5)
    clear_screen()    

# EXPLORE ROOMS
def explore_room(username):

    glitch_effect()
    loading_effect()
    type_text(RED +"\n          WELCOME TO THE ESCAPE GAME..." +RESET,0.05)
    time.sleep(0.8)
    clear_screen()
    while True:
        start_menu_music()
        print(LIGHT_RED +r"""
        ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗
        ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
        █████╗  ███████╗██║     ███████║██████╔╝█████╗
        ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝
        ███████╗███████║╚██████╗██║  ██║██║     ███████╗
        ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝
        """+ RESET)
        print(f"""{RED}{BOLD}
        ╔══════════════════════════════════════════════════╗
        ║                   EXPLORE ROOMS                  ║
        ╚══════════════════════════════════════════════════╝{RESET}\n""")
        print()
        print(
            f"{RED}{BOLD}              ☠  THE ESCAPE  ☠{RESET}"
        )
        print(
            f"\n{WHITE}[1] KILL_USER.PY{RESET}\n{WHITE}[2] FINAL_PATIENT{RESET}\n{WHITE}[3] GOOD_NIGHTMARE{RESET}\n{WHITE}[4] EXIT{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            if choice == 1:
                result = room1_levels(username)
                if result == "MENU":
                    return
                elif result == "EXPLORE":
                    continue
                else:
                    continue
            elif choice == 2:
                result = room2_levels(username)
                if result == "MENU":
                    return
                elif result == "EXPLORE":
                    continue
                else:
                    continue

            elif choice == 3:
                result = room3_levels(username)
                if result == "MENU":
                    return
                elif result == "EXPLORE":
                    continue
                else:
                    continue

            elif choice == 4:
                return
            else:
                print( f"{RED}☠ INVALID CHOICE.{RESET}")
                time.sleep(1)
                clear_screen()
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}" )
            time.sleep(1)
            clear_screen()
# =========================================================
# ROOM 1 LEVELS
# =========================================================
def room1_levels(username):
    while True:
        clear_screen()
        room1_badge = get_room_badge(username,1)
        print(f"{RED}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║                  KILL_USER.PY                    ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)
        

        level1_status = "LEVEL 01 STATUS : NOT COMPLETED"
        level2_status = "LEVEL 02 STATUS : 🔒 LOCKED"
        if room1_badge == "SILVER":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : 🔓 UNLOCKED"

        elif room1_badge == "GOLD":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : ✓ COMPLETED — GOLD🏅🏆"
        

        print(f"{WHITE}[1] [{level1_status}]{RESET}\n{WHITE}[2] [{level2_status}]{RESET}\n{WHITE}[3] BACK{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            # LEVEL 1
            if choice == 1:
                result = room1(username)
                if result == "EXPLORE":
                    return "EXPLORE"
                elif result == "MENU":
                    return "MENU"
                else:
                    continue
            # ---------------------------------------------
            # LEVEL 2
            # ---------------------------------------------
            elif choice == 2:
                room1_badge = get_room_badge(username,1)
                if room1_badge == "LOCKED":
                    clear_screen()
                    print(f"{RED}{BOLD}")
                    print("╔══════════════════════════════════════════╗")
                    print("║              ACCESS DENIED               ║")
                    print("╚══════════════════════════════════════════╝")
                    print(RESET)
                    print(f"\n{RED}☠ LEVEL 01 MUST BE COMPLETED FIRST.{RESET}\n")
                    input(f"{WHITE}Press ENTER to return...{RESET}")
                else:
                    result = room1_level2(username)
                    if result == "MENU":
                        return "MENU"
                    elif result == "EXPLORE":
                        return "EXPLORE"
                    else:
                        continue

            # ---------------------------------------------
            # BACK
            # ---------------------------------------------
            elif choice == 3:
                clear_screen()
                return
            
            else:
                print(f"{RED}☠ INVALID CHOICE.{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}")
            time.sleep(1)
# =========================================================
# AFTER LEVEL 1
# =========================================================
def after_level1(username):
    while True:
        clear_screen()
        print(f"{GREEN}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║                                                  ║")
        print("║              LEVEL 01 CLEARED                    ║")
        print("║                                                  ║")
        print("║                 BADGE: SILVER                    ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)
        print(f"\n{WHITE}[1] Continue to LEVEL 02{RESET}\n{WHITE}[2] Explore Another Room{RESET}\n{WHITE}[3] Return to Main Menu{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}" ))
            # ---------------------------------------------
            # CONTINUE LEVEL 2
            # ---------------------------------------------
            if choice == 1:
                clear_screen()
                result=room1_level2(username)
                return result
            # ---------------------------------------------
            # EXPLORE ANOTHER ROOM
            # ---------------------------------------------
            elif choice == 2:
                from Kill_User_py import stop_background_music
                stop_background_music()
                clear_screen()
                return "EXPLORE"
            # ---------------------------------------------
            # MAIN MENU
            # ---------------------------------------------
            elif choice == 3:
                from Kill_User_py import stop_background_music
                stop_background_music()
                clear_screen()
                return "MENU"
            else:
                print(f"{RED}☠ INVALID CHOICE...{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER...{RESET}")
            time.sleep(1)
# =========================================================
# GET ROOM BADGE
# =========================================================
def get_room_badge(username, room_number):
    try:
        with open(FILE_NAME,"r",newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username:
                    column = ("room"+ str(room_number)+ "_badge")
                    return row.get(column,"LOCKED")
    except FileNotFoundError:
        return "LOCKED"
    return "LOCKED"

def get_completed_rooms(username):
    rooms = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["username"] == username:

                room_data = [
                    {"name": "KILL_USER.PY", "badge": row["room1_badge"]},
                    {"name": "FINAL_PATIENT", "badge": row["room2_badge"]},
                    {"name": "GOOD_NIGHTMARE", "badge": row["room3_badge"]}
                ]

                completed_rooms = filter(
                    lambda room: room["badge"] != "LOCKED",
                    room_data
                )

                return list(completed_rooms)

    return rooms
# =========================================================
# MY PROFILE
# =========================================================
def show_profile(username):
    # الألوان
    R = "\033[91m"  # أحمر فاتح
    B = "\033[31m"  # أحمر دموي
    P = "\033[95m"  # أرجواني
    Y = "\033[93m"  # أصفر (للـ GOLD)
    W = "\033[97m"  # أبيض (للـ SILVER)
    D = "\033[90m"  # رمادي غامق
    RESET = "\033[0m"
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                room1_badge = row["room1_badge"]
                room2_badge = row["room2_badge"]
                room3_badge = row["room3_badge"]
                completed_rooms = get_completed_rooms(username)
                completed_rooms_count = len(completed_rooms)
                levels_completed = 0
                if room1_badge == "SILVER":
                    levels_completed += 1
                elif room1_badge == "GOLD":
                    levels_completed += 2
                if room2_badge == "SILVER":
                    levels_completed += 1
                elif room2_badge == "GOLD":
                    levels_completed += 2
                if room3_badge == "SILVER":
                    levels_completed += 1
                elif room3_badge == "GOLD":
                    levels_completed += 2
                # دالة تلوين الشارة وضبط مسافتها بدقة
                def format_badge(badge):
                    if badge == "GOLD":
                        color = Y
                    elif badge == "SILVER":
                        color = W
                    else:
                        color = D
                    # pad_spaces لضمان أن طول النص دائماً 8 حروف
                    spaces = " " * (8 - len(badge))
                    return f"{color}{badge}{spaces}{R}"
                b1 = format_badge(room1_badge)
                b2 = format_badge(room2_badge)
                b3 = format_badge(room3_badge)
                # ضبط طول اسم المستخدم ليكون 15 حرفاً تماماً
                u_padded = f"{username:<15}"[:15]
                print()
                print(f"{B}      ☠️  💀  🕸️   🩸  🕯️  ☠️  💀  🕸️   🩸  🕯️  ☠️  💀  🕸️{RESET}")
                print(f"{R}    ╔════════════════════════════════════════════════╗{RESET}")
                print(f"{R}    ║            {P}🕷️  MY HORROR PROFILE  🕸️{R}             ║{RESET}")
                print(f"{R}    ╠════════════════════════════════════════════════╣{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ║   {Y}Username :{RESET}     {R}{u_padded}               ║{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ║   {D}─────────────── PROGRESS ───────────────{R}     ║{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ║   {Y}Levels Completed :{RESET} {B}{levels_completed}/6{R}                       ║{RESET}")
                print(f"{R}    ║   {Y}Rooms Unlocked  :{RESET} {B}{completed_rooms_count}/3{R}                        ║{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ║   {D}───────────── ROOM BADGES ──────────────{R}     ║{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ║   {P}KILL_USER.PY   {RESET}  │ {b1}                  ║{RESET}")
                print(f"{R}    ║   {P}FINAL_PATIENT  {RESET}  │ {b2}                  ║{RESET}")
                print(f"{R}    ║   {P}GOOD_NIGHTMARE  {RESET} │ {b3}                  ║{RESET}")
                print(f"{R}    ║                                                ║{RESET}")
                print(f"{R}    ╚════════════════════════════════════════════════╝{RESET}")
                print(f"{B}     🕯️  🩸  🕸️   💀  ☠️  🕯️  🩸  🕸️   💀  ☠️  🕯️  🩸  🕸️{RESET}")
                input(f"\n{B}Press Enter to return...{RESET}")
                return
        print(f"{R}User not found.{RESET}")
def room2_levels(username):
    while True:
        clear_screen()
        room2_badge = get_room_badge(username, 2)
        print(f"{RED}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║                FINAL_PATIENT                     ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)

        level1_status = "LEVEL 01 STATUS : NOT COMPLETED"
        level2_status = "LEVEL 02 STATUS : 🔒 LOCKED"
        if room2_badge == "SILVER":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : 🔓 UNLOCKED"
        elif room2_badge == "GOLD":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : ✓ COMPLETED — GOLD🏅🏆"

        print(f"{WHITE}[1] [{level1_status}]{RESET}\n{WHITE}[2] [{level2_status}]{RESET}\n{WHITE}[3] BACK{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            if choice == 1:
                result = room2(username)
                if result == "EXPLORE":
                    return "EXPLORE"
                elif result == "MENU":
                    return "MENU"
                else:
                    continue
            elif choice == 2:
                room1_badge = get_room_badge(username,1)
                if room2_badge == "LOCKED":
                    clear_screen()
                    print(f"{RED}{BOLD}")
                    print("╔══════════════════════════════════════════╗")
                    print("║              ACCESS DENIED               ║")
                    print("╚══════════════════════════════════════════╝")
                    print(RESET)
                    print(f"\n{RED}☠ LEVEL 01 MUST BE COMPLETED FIRST.{RESET}\n")
                    input(f"{WHITE}Press ENTER to return...{RESET}")
                else:
                    result = room2_level2(username)
                    if result == "MENU":
                        return "MENU"
                    elif result == "EXPLORE":
                        return "EXPLORE"
                    else:
                        continue        
            elif choice == 3:
                clear_screen()
                return
            else:
                print(f"{RED}☠ INVALID CHOICE.{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}")
            time.sleep(1)

def after_level1_room2(username): 

    while True:
        clear_screen()
        print(f"{GREEN}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║              LEVEL 01 CLEARED                    ║")
        print("║                 BADGE: SILVER                    ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)
        print(f"\n{WHITE}[1] Continue to LEVEL 02{RESET}\n{WHITE}[2] Explore Another Room{RESET}\n{WHITE}[3] Return to Main Menu{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            if choice == 1:
                clear_screen()
                result=room2_level2(username)
                return result
            elif choice == 2:
                from dr_ragheb import stop_background_music
                stop_background_music()
                start_menu_music()
                clear_screen()
                return "EXPLORE"
            elif choice == 3:
                from dr_ragheb import stop_background_music
                stop_background_music()
                start_menu_music()
                clear_screen()
                return "MENU"
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}")
            time.sleep(1)

def room3_levels(username):
    while True:
        clear_screen()
        room3_badge = get_room_badge(username, 3)
        print(f"{RED}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║                   DAR AL NOOR                    ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)
        
        level1_status = "LEVEL 01 STATUS : NOT COMPLETED"
        level2_status = "LEVEL 02 STATUS : 🔒 LOCKED"
        if room3_badge == "SILVER":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : 🔓 UNLOCKED"
        elif room3_badge == "GOLD":
            level1_status = "LEVEL 01 STATUS : ✓ COMPLETED — SILVER🥈"
            level2_status = "LEVEL 02 STATUS : ✓ COMPLETED — GOLD🏅🏆"

        print(f"{WHITE}[1] [{level1_status}]{RESET}\n{WHITE}[2] [{level2_status}]{RESET}\n{WHITE}[3] BACK{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            if choice == 1:
                result = room3(username)
                if result == "EXPLORE":
                    return "EXPLORE"
                elif result == "MENU":
                    return "MENU"
                else:
                    continue
            elif choice == 2:
                room3_badge = get_room_badge(username, 3)
                if room3_badge == "LOCKED":
                    clear_screen()
                    print(f"{RED}{BOLD}")
                    print("╔══════════════════════════════════════════╗")
                    print("║              ACCESS DENIED               ║")
                    print("╚══════════════════════════════════════════╝")
                    print(RESET)
                    print(f"\n{RED}☠ LEVEL 01 MUST BE COMPLETED FIRST.{RESET}\n")
                    input(f"{WHITE}Press ENTER to return...{RESET}")
                else:
                    result = room3_level2(username)
                    if result == "MENU":
                        return "MENU"
                    elif result == "EXPLORE":
                        return "EXPLORE"
                    else:
                        continue
            elif choice == 3:
                clear_screen()
                return
            else:
                print(f"{RED}☠ INVALID CHOICE.{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER.{RESET}")
            time.sleep(1)

def after_level1_room3(username):
    while True:
        clear_screen()
        print(f"{GREEN}{BOLD}")
        print("╔══════════════════════════════════════════════════╗")
        print("║                                                  ║")
        print("║              LEVEL 01 CLEARED                    ║")
        print("║                                                  ║")
        print("║                 BADGE: SILVER                    ║")
        print("║                                                  ║")
        print("╚══════════════════════════════════════════════════╝")
        print(RESET)
        print(f"\n{WHITE}[1] Continue to LEVEL 02{RESET}\n{WHITE}[2] Explore Another Room{RESET}\n{WHITE}[3] Return to Main Menu{RESET}\n")
        try:
            choice = int(input(f"{RED}☠ ENTER YOUR CHOICE: {RESET}"))
            if choice == 1:
                clear_screen()
                result = room3_level2(username)
                return result
            elif choice == 2:
                from dar_al_noor import stop_background_music
                stop_background_music()
                start_menu_music()
                clear_screen()
                return "EXPLORE"
            elif choice == 3:
                from dar_al_noor import stop_background_music
                stop_background_music()
                start_menu_music()
                clear_screen()
                return "MENU"
            else:
                print(f"{RED}☠ INVALID CHOICE...{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}☠ ENTER A NUMBER...{RESET}")
            time.sleep(1)
# =========================================================
# HOW TO PLAY
# =========================================================

def how():
    start_menu_music()

    clear_screen()

    print(f"{PURPLE}{BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                    🎮  HOW TO PLAY  🎮                      ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(RESET)

    print()

    print(
            f"""{WHITE}
    __🔍 1. EXPLORE _______________________________________________
    │ Explore the room and choose anything you want to investigate. │
    │ You don't have to follow a specific order.                    │
    └───────────────────────────────────────────────────────────────┘
    {RESET}""")

    print(
            f"""{WHITE}
    __ 🕵️ 2. INVESTIGATE __________________________________________
    │ The things you investigate may contain:                       │
    │                                                               │
    │   • Clue                                                      │
    │   • Puzzle                                                    │
    │   • Useful Information                                        │
    │   • Story Details                                             │
    │   • Nothing                                                   │
    └───────────────────────────────────────────────────────────────┘
    {RESET}""")

    print(
                f"""{WHITE}
    
    __ 📖 3. SAVE CLUES ___________________________________________
    │ Important information you discover will be saved automatically│
    │ in your Book.                                                 │
    │                                                               │
    │ Type BOOK anytime to review your discovered information.      │
    └───────────────────────────────────────────────────────────────┘

        {RESET}""")
        

    print(
                f"""{WHITE}
    
    __ 🧩 4. SOLVE PUZZLES ________________________________________
    │ Each Level has 3 independent Puzzles.                         │
    │ You can solve them in any order.                              │
    │                                                               │
    │ You don't have to solve one Puzzle to unlock another.         │
    └───────────────────────────────────────────────────────────────┘
    {RESET}""")

    print(
                f"""{WHITE}

    __ 💡 5. USE HINTS ________________________________________
    │    Stuck? You can use a Hint.                             │ 
    |                                                           |
    │   ••Using a Hint costs 30 seconds !!                      | 
    └───────────────────────────────────────────────────────────┘
    {RESET}""")

    print(
                f"""{WHITE}
    __ ⏱️ 6. WATCH THE TIME _______________________________________
    │ Every Level has a 15-minute time limit.                       │
    │                                                               │
    │ The timer continues while exploring, solving puzzles,         │
    │ and reading your Book.                                        │
    └───────────────────────────────────────────────────────────────┘
    {RESET}""")

    print(f"""{WHITE}
    __ ❌ 7. WRONG ANSWERS ________________________________________
    │ A wrong answer costs 30 seconds.                              │
    │                                                               │
    │ You can try again or return to exploration.                   │
    └───────────────────────────────────────────────────────────────┘
    {RESET}""")

    print(f"{GREEN}SILVER = Level 01 completed{RESET}\n")
    print(f"{YELLOW}GOLD = Level 02 completed{RESET}\n")

    print_horror_messages(
        "Explore carefully.",
        "Keep track of your clues.",
        color=WHITE,
        prefix="│   "
    )
        
    print(f"""{RED}
        ╔══════════════════════════════════════════════════════════════╗
        ║                         GOOD LUCK...                         ║                                                           
        ║        Not everything you find is useless.                   ║
        ║        Not everything you see is what it seems.              ║
        ╚══════════════════════════════════════════════════════════════╝{RESET}""")    
    input(f"\n{WHITE}Press ENTER to return...{RESET}")


# =========================================================
# LOGOUT
# =========================================================

def logout():

    clear_screen()

    print(f"{RED}{BOLD}")

    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║               💀 LOGGING OUT ... 💀              ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print(RESET)
    time.sleep(2.5)
    clear_screen()
    


# =========================================================
# END
# =========================================================