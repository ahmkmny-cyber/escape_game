#file auth.py
import os
import re
import csv
import time
from menu import clear_screen
from music_of_game import start_menu_music
#______________________________________________validate________________________________________________________
def validate_username(username):
    if username == "":
        return "Username cannot be empty."
    if len(username) < 3:
        return "Username must be at least 3 characters."
    if len(username) > 16:
        return "Username must not exceed 16 characters."
    if not re.match(r"^[A-Za-z]", username):
        return "Username must start with a letter."
    if not re.match(r"^[A-Za-z0-9_]+$", username):
        return "Username can contain only letters, numbers, and _."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Password must contain an uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain a lowercase letter."
    if not re.search(r"\d", password):
        return "Password must contain a number."
    if not re.search(r"[@$!%*?&]", password):
        return "Password must contain a special character."
    return None

def username_exists(username):
    try:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["username"] == username:
                    return True

    except FileNotFoundError:
        return False

    return False
#________________________________________________ register________________________________________________
def register():
    print("3-16 chars | Start with a letter | A-Z, 0-9, _")
    while True:
        username = input("Username: ").strip()
        error = validate_username(username)
        if error:
            print("❌", error)
            continue
        if username_exists(username):
            print("❌ Username already exists.\ntry another Username")            
            continue 
        break

    while True:
        password = input("8+ chars | Uppercase | Lowercase | Number | Special (@$!%*?&)\nPassword: ")
        error = validate_password(password)
        if error:
            print("❌", error)
            continue
        break

    while True:
        confirm_password = input("Confirm Password: ")
        if confirm_password != password:
            print("❌ Passwords do not match.")
            continue
        break 

    with open("users.csv", "a", newline="") as file:
        writer = csv.DictWriter(file,fieldnames = [ "username", "password", "room1_badge", "room2_badge", "room3_badge" ])
        if file.tell()==0:
            writer.writeheader() 
        writer.writerow({"username":username,
                        "password":password,
                        "room1_badge": "LOCKED",
                        "room2_badge": "LOCKED",
                        "room3_badge": "LOCKED"}) 
    print("\n✅ Account created successfully!")
    time.sleep(2)

    return username
#___________________________________________login_________________________________________________
def login():
    username = input("Username: ")
    password = input("Password: ")
    
    with open("users.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                if row["password"] == password:
                    print("\n✅ Login successful!")
                    print(f"Welcome to the game , {username}!")
                    time.sleep(2)
                    return username
                    
                else:
                    print("❌ Incorrect password.")
                    return None
    print("❌ Username not found.")
    return None
#_________________________________________start_____________________________________________
def start():
    start_menu_music()
    # الألوان الدموية والمظلمة
    R = "\033[91m"     # أحمر ساطع
    B = "\033[31m"     # أحمر دموي
    P = "\033[95m"     # أرجواني
    Y = "\033[93m"     # أصفر
    D = "\033[90m"     # رمادي مظلم
    RESET = "\033[0m"  # إعادة ضبط اللون
    while True:
        print(f"""
{B}        .---.      {R}  ____ ____   ____    _    ____  _____   ____    _    __  __ _____ {RESET}
{B}       /     \     {R} / ___/ ___| / ___|  / \  |  _ \| ____| / ___|  / \  |  \/  | ____|{RESET}
{B}      | () () |    {B}| |  \___ \| |     / _ \ | |_) |  _|  | |  _  / _ \ | |\/| |  _|  {RESET}
{B}       \  ^  /     {B}| |______) | |___ / ___ \|  __/| |___ | |_| |/ ___ \| |  | | |___ {RESET}
{B}        |||||      {P} \____|____/ \____/_/   \_\_|   |_____| \____/_/   \_\_|  |_|_____|{RESET}
{B}        '||'       {D} ─────────────────────────────────────────────────────────────────{RESET}
{B}  ☠️   DARKNESS    {P}                   🕷️  THE NIGHTMARE AWAITS YOU  🕸️{RESET}""")
        print(f"{D}=================================================================================={RESET}")
        print(f"   {Y}[1]{RESET} {R}🩸  CLAIM A NEW SOUL{RESET}          {D}(Register){RESET}")
        print(f"   {Y}[2]{RESET} {P}👁️   ENTER THE ABYSS{RESET}          {D}(Login){RESET}")
        print(f"   {Y}[3]{RESET} {B}☠️   ACCEPT YOUR DEATH{RESET}         {D}(Exit){RESET}")
        print(f"{D}=================================================================================={RESET}")
        try:
            choice = int(input(f"\n{B}🩸 Enter your destiny [1-3]: {RESET}"))
            if choice == 1:
                username = register()
                return username
            elif choice == 2:
                username = login()
                if username:
                    return username
                continue
            elif choice == 3:
                print(f"\n{B}☠️ The nightmare never truly ends... Farewell! 👁️{RESET}")
                break
            else:
                print(f"{R}❌ Invalid choice! The monsters feed on your mistakes.{RESET}")
                time.sleep(2)
                clear_screen()
        except ValueError:
            print(f"{R}❌ Type a NUMBER... or give up your soul!{RESET}")
            time.sleep(2)
            clear_screen()

#_____________________________________update____________________________________________________