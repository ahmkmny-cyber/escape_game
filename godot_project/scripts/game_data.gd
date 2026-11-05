class_name GameData
extends RefCounted
## Ported rules + content from gui_pygame/state.py and Kill_User_py.py.

const LEVEL_TIME: int = 15 * 60
const WRONG_PENALTY: int = 30
const HINT_PENALTY: int = 60

const STORY_LINES: Array = [
	"In 2023, a programmer named Tarek was working on strange code...",
	"A code that could extract data from places not connected to internet!",
	"Neighbors heard TERRIFYING SCREAMS. Police found Tarek DEAD.",
	"Screen kept printing:  while True:  kill user",
	"You entered the room. Door locked. Lights out.",
	"You have 15 minutes to find the bug. Otherwise SERVER LOCKS FOREVER.",
]

# exact=true means case-sensitive compare (mirrors original puzzle 1).
const PUZZLES: Array = [
	{
		"id": 1, "title": "PUZZLE 01 - Hidden Condition",
		"prompt": ["The program contains a hidden condition.", "What exact word will print on the screen?"],
		"code": ['status = "DEAD"', 'status.replace("DEAD", "ALIVE")', "print(status)"],
		"answer": "DEAD",
		"hint": "Changing a string doesn't always change the original. Did you save the result of replace() anywhere?",
		"exact": true,
	},
	{
		"id": 2, "title": "PUZZLE 02 - Evil Scope Trap",
		"prompt": ["What INTEGER number will print on the screen?"],
		"code": ["i = 99", "for i in range(5):", "    pass", "print(i)"],
		"answer": "4",
		"hint": "99 is just a distraction... the loop has other plans for i",
		"exact": false,
	},
	{
		"id": 3, "title": "PUZZLE 03 - Search For The Key",
		"prompt": ["What INTEGER number will print on the screen?"],
		"code": ['log = "ERROR_SYSTEM_FAILURE_NO_ACCESS"', 'code = log.find("KEY")', "print(code)"],
		"answer": "-1",
		"hint": "If the key cannot be found, what negative number tells you it doesn't exist?",
		"exact": false,
	},
	{
		"id": 4, "title": "PUZZLE 04 - Binary Year Terminal",
		"prompt": ["Full binary-toggle lock comes next.", "Enter 0011 (last digit of 2023 = 3)."],
		"code": ["target = 4-bit binary of 3", "slots = [8 - 4 - 2 - 1]"],
		"answer": "0011",
		"hint": "3 = 2 + 1, so bits: 0 0 1 1",
		"exact": false,
	},
]
