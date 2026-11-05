class_name SaveSystem
extends RefCounted
## CSV badge storage, same columns as the terminal version (users.csv).
## In the editor this reads/writes res://users.csv next to project.godot.

const COLS: Array = ["username", "password", "room1_badge", "room2_badge", "room3_badge"]
const PATH: String = "res://users.csv"


static func _read_rows() -> Array:
	if not FileAccess.file_exists(PATH):
		return []
	var rows: Array = []
	var f := FileAccess.open(PATH, FileAccess.READ)
	if f == null:
		return []
	# skip header
	if not f.eof_reached():
		f.get_csv_line()
	while not f.eof_reached():
		var line: PackedStringArray = f.get_csv_line()
		if line.size() == COLS.size():
			rows.append(line)
	f.close()
	return rows


static func _write_rows(rows: Array) -> bool:
	var f := FileAccess.open(PATH, FileAccess.WRITE)
	if f == null:
		return false
	f.store_csv_line(PackedStringArray(COLS))
	for r in rows:
		f.store_csv_line(r)
	f.close()
	return true


static func get_badge(username: String, room_number: int) -> String:
	var col: String = "room%d_badge" % room_number
	var idx: int = COLS.find(col)
	for r in _read_rows():
		if r[0] == username:
			return r[idx]
	return "LOCKED"


static func set_badge(username: String, room_number: int, badge: String) -> bool:
	var col: String = "room%d_badge" % room_number
	var idx: int = COLS.find(col)
	var rows: Array = _read_rows()
	var found := false
	for r in rows:
		if r[0] == username:
			r[idx] = badge
			found = true
	if not found:
		var row := PackedStringArray(["", "", "LOCKED", "LOCKED", "LOCKED"])
		row[0] = username
		row[idx] = badge
		rows.append(row)
	return _write_rows(rows)
