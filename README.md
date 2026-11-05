# ESCAPE THE NIGHT

> **A Python Terminal Escape Room Game**

**Escape The Night** is an interactive horror-themed escape room game built with Python. The player creates an account, explores different story-driven rooms, solves logic and programming-inspired puzzles, manages a countdown timer, uses limited hints, and earns progress badges based on completed levels.

The project combines Python programming concepts with storytelling, terminal effects, sound design, file handling, and persistent player progress.

---

## 🎮 Game Overview

The game is designed as a collection of connected horror escape-room experiences. Each room has its own story, atmosphere, puzzles, timer, hints, and two levels of increasing difficulty.

### Current Rooms

| Room | Theme | Levels |
|---|---|---:|
| **Room 01 – The Server** | A mysterious cyber/server room involving a programmer and a dangerous system | 2 |
| **Room 02 – Dr. Ragheb** | A dark and mysterious medical setting filled with puzzles and danger | 2 |
| **Room 03 – Dar Al Noor** | A haunted orphanage connected to a disturbing hidden story | 2 |

Each level contains multiple puzzles that must be solved before the player can escape.

---

## ✨ Main Features

- 🔐 **Account System**
  - Create a new account with username and password validation.
  - Login using saved account credentials.
  - User data is stored persistently in a CSV file.

- 👤 **Player Profile**
  - View saved player information and room progress.
  - Track badges for each room.
  - Room progress is stored between sessions.

- 🧩 **Puzzle-Based Gameplay**
  - Logic and problem-solving challenges.
  - Programming-inspired puzzles.
  - Number, code, maze, pattern, and deduction challenges.

- ⏳ **Timed Levels**
  - Each level has a countdown timer.
  - Wrong answers can apply time penalties.
  - The player must manage time while solving the puzzles.

- 💡 **Hint System**
  - Players can use hints during levels.
  - Hints are limited to keep the game challenging.

- 🏆 **Progress & Badges**
  - `LOCKED` → The room has not been completed yet.
  - `SILVER` → Level 01 of the room is completed.
  - `GOLD` → Both levels of the room are completed.

- 🔊 **Background Music & Voiceovers**
  - Menu background music.
  - Room-specific background music.
  - Story voiceovers and sound effects.

- 👻 **Horror Terminal Experience**
  - Typewriter text effects.
  - Loading and glitch effects.
  - Colored terminal messages.
  - Story screens and atmospheric interactions.

---

## 🛠️ Technologies Used

- **Python 3**
- **CSV** for persistent player data
- **Regular Expressions (`re`)** for input validation
- **PyGame** for audio and music playback
- **Threading** for background audio and timed gameplay
- **Pytest** for automated testing

### Python Concepts Demonstrated

The project also demonstrates several important Python concepts, including:

- Functions and modular programming
- Multiple Python modules
- File I/O
- CSV data persistence
- `csv.DictReader` and `csv.DictWriter`
- Exception handling
- Regular expressions
- Loops and conditional logic
- Lists and dictionaries
- Global/local state management
- Threads
- Generators / advanced function techniques
- Lambda and collection processing
- Automated unit testing

---

## 📁 Project Structure

```text
Escape room/
│
├── main.py
├── auth.py
├── menu.py
├── player_data.py
├── music_of_game.py
│
├── Kill_User_py.py
├── dr_ragheb.py
├── dar_al_noor.py
│
├── users.csv
│
├── Kill_User_Background.mp3
├── Kill_User_Voiceover.mp3
├── Dr_Ragheb_Background.mp3
├── Dr_Ragheb_Voiceover.mp3
├── Dar_ELnoor_Background.mp3
├── Dar_ELnoor_Voiceover.mp3
└── Game_Background.mp3
```

### File Responsibilities

| File | Purpose |
|---|---|
| `main.py` | Main entry point of the application. |
| `auth.py` | Registration, login, username/password validation, and account creation. |
| `menu.py` | Main menu, room selection, profile, progress display, and navigation. |
| `player_data.py` | Reads and updates room progress and player badges. |
| `music_of_game.py` | Handles menu music and background audio playback. |
| `Kill_User_py.py` | Implements Room 01 and its two levels. |
| `dr_ragheb.py` | Implements Room 02 and its two levels. |
| `dar_al_noor.py` | Implements Room 03 and its two levels. |
| `users.csv` | Stores account information and room progress. |

---

## ⚙️ Requirements

Make sure you have:

- Python 3 installed
- `pip` available in your terminal
- A terminal/command prompt that supports standard console output

Install the required third-party packages with:

```bash
pip install pygame
pip install pytest
```

Or install both at once:

```bash
pip install pygame pytest
```

---

## ▶️ How to Run

1. Open the project folder in VS Code or your preferred Python IDE.
2. Open a terminal inside the project folder.
3. Install the required packages.
4. Run the main file:

```bash
python main.py
```

The game will start from the main menu, where you can register, login, and enter the game.

---

## 🕹️ How to Play

### 1. Create an Account

Choose **Register** and enter a valid username and password.

The input validation checks the entered data before saving the account.

### 2. Login

Choose **Login** and enter your account credentials.

After a successful login, you can access the game menu and your profile.

### 3. Explore Rooms

Select an available room and start Level 01.

Some rooms unlock their second level only after Level 01 has been completed.

### 4. Solve the Puzzles

Read the clues carefully, inspect the room, use the available actions, and solve the puzzles before the timer reaches zero.

### 5. Earn Badges

Your progress is automatically saved.

```text
LOCKED  → Room not completed
SILVER  → Level 01 completed
GOLD    → Level 01 + Level 02 completed
```

---

## 💾 Data Persistence

Player information and progress are stored in:

```text
users.csv
```

The CSV file contains fields for the player account and room badges, allowing progress to remain available after the program is closed and opened again.

Example structure:

```text
username,password,room1_badge,room2_badge,room3_badge
```

> **Important:** `users.csv` contains account data. Do not publish real passwords or sensitive personal information when sharing the project publicly.

---

## 🧪 Testing

The project can be tested using **pytest**.

Run all tests with:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

The testing suite is intended to verify important parts of the application's core logic, including valid and invalid inputs and expected exceptions.

---

## 🔊 Audio Setup

The project uses MP3 files for background music and voiceovers.

Make sure all audio files remain in the project folder and that the paths used by the Python files match their actual location on your computer.

If the project is moved to another computer, update any hard-coded audio paths so they point to the new project location.

---

## 🧠 Project Design Goals

The project was developed to combine:

1. **Python programming** – functions, modules, data structures, file handling, validation, and exception handling.
2. **Game logic** – levels, puzzles, timers, hints, progress tracking, and win/lose states.
3. **Storytelling** – separate horror stories and atmospheres for each room.
4. **User experience** – terminal animations, colors, sounds, and interactive menus.
5. **Data persistence** – saving player accounts and room progress using CSV.

---

## 🚀 Future Improvements

Possible future extensions include:

- More escape rooms and story chapters
- Additional puzzle types
- A global leaderboard
- More player statistics
- Difficulty settings
- Better cross-platform audio path handling
- A graphical user interface (GUI)
- More automated tests

---

## 👥 Project

**ESCAPE THE NIGHT**

A Python-based terminal escape room project focused on combining programming concepts with interactive storytelling and puzzle solving.

---

### Enjoy the game... if you can escape. 👁️
#   e s c a p e _ g a m e  
 #   e s c a p e _ g a m e  
 