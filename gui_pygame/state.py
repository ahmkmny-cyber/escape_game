from dataclasses import dataclass, field


@dataclass
class Puzzle:
    id: int
    title: str
    prompt_lines: list
    code_lines: list
    answer: str
    hint: str
    solved: bool = False


def get_room1_level1_puzzles():
    # Mirrors Kill_User_py.py puzzle_1..4 (answers unchanged)
    return [
        Puzzle(
            id=1,
            title="PUZZLE 01 - Hidden Condition",
            prompt_lines=[
                "The program contains a hidden condition.",
                "What exact word will print on the screen?",
            ],
            code_lines=[
                'status = "DEAD"',
                'status.replace("DEAD", "ALIVE")',
                "print(status)",
            ],
            answer="DEAD",
            hint="Changing a string doesn't always change the original. Did you save the result of replace() anywhere?",
        ),
        Puzzle(
            id=2,
            title="PUZZLE 02 - Evil Scope Trap",
            prompt_lines=[
                "What INTEGER number will print on the screen?",
            ],
            code_lines=[
                "i = 99",
                "for i in range(5):",
                "    pass",
                "print(i)",
            ],
            answer="4",
            hint="99 is just a distraction... the loop has other plans for i",
        ),
        Puzzle(
            id=3,
            title="PUZZLE 03 - Search For The Key",
            prompt_lines=[
                "What INTEGER number will print on the screen?",
            ],
            code_lines=[
                'log = "ERROR_SYSTEM_FAILURE_NO_ACCESS"',
                'code = log.find("KEY")',
                "print(code)",
            ],
            answer="-1",
            hint="If the key cannot be found, what negative number tells you it doesn't exist?",
        ),
        Puzzle(
            id=4,
            title="PUZZLE 04 - Binary Year Terminal",
            prompt_lines=[
                "Prototype shows first 3 puzzles fully.",
                "Puzzle 04 (binary toggle) comes in full version.",
                "Enter 0011 to solve (last digit of 2023 = 3).",
            ],
            code_lines=[
                "target = 4-bit binary of 3",
                "slots = [8 - 4 - 2 - 1]",
            ],
            answer="0011",
            hint="3 = 2 + 1, so bits: 0 0 1 1",
        ),
    ]


@dataclass
class LevelState:
    puzzles: list = field(default_factory=get_room1_level1_puzzles)
    remaining: int = 15 * 60
    hint_used: bool = False
    over: bool = False
    won: bool = False

    def apply_penalty(self, seconds: int):
        self.remaining = max(0, self.remaining - seconds)
        if self.remaining == 0:
            self.over = True

    def check_win(self):
        if all(p.solved for p in self.puzzles):
            self.won = True
        return self.won

    @property
    def time_str(self):
        m = self.remaining // 60
        s = self.remaining % 60
        return f"{m:02d}:{s:02d}"
