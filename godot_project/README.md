# Escape The Night — Godot port (Room 01 prototype)

## Run it
1. Install **Godot 4.x** (GL Compatibility): https://godotengine.org/download
2. Open Godot → Import → select the `godot_project` folder → Open.
3. Press **F5** (or ▶). No build step needed.

## Controls
- Menu: ENTER THE SERVER / QUIT.
- Story: ENTER / SPACE / CLICK, or CONTINUE button (first press completes the line).
- Room: click a puzzle terminal, LANTERN HINT (-60s, once), ESC = menu.
- Puzzle: type answer + ENTER / SUBMIT, ESC = back.
- Wrong answer: -30s. Win all 4 → SILVER saved to `users.csv` (next to project.godot).

## What is ported
- Rules: 15:00 timer, penalties, one hint, 4 puzzles with original answers
  (`gui_pygame/state.py` → `scripts/game_data.gd`).
- Audio: menu loop + room loop + voiceover (`scripts/audio_manager.gd`).
- Save: same `username,password,room1_badge,...` CSV columns (`scripts/save_system.gd`).
- Assets reused: `assets/rooms/*.png`, `assets/fonts/` (HelpMe titles, Cairo body), room01 mp3s.

## Next steps
- Login screen (replace demo user `player` in `scripts/main.gd`).
- Rooms 02/03 + Level 2 (add data to `game_data.gd`, reuse scenes).
- Binary-toggle lock for puzzle 04, room 02/03 audio files.
- Export exe: Project → Export → Windows preset (needs export templates).
