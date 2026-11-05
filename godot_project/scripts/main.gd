extends Control
## Room 01 Level 01 prototype: MENU -> STORY -> ROOM -> PUZZLE + HUD.
## UI is built in code (no editor layout needed). Rules mirror gui_pygame.

const PLAYER := "player" # demo user; full login screen comes next

var _scene: String = "MENU"
var _remaining: int = GameData.LEVEL_TIME
var _hint_used: bool = false
var _solved: Array = [false, false, false, false]
var _active: int = -1
var _over: bool = false
var _won: bool = false
var _story_idx: int = 0
var _story_chars: float = 0.0

var _audio: AudioManager
var _timer_label: Label
var _timer_bar: ProgressBar
var _msg: Label
var _story_label: Label
var _font_title: Font
var _font_body: Font


func _ready() -> void:
	_audio = AudioManager.new()
	add_child(_audio)
	_font_title = load("res://assets/fonts/HelpMe.ttf")
	_font_body = load("res://assets/fonts/Cairo.ttf")
	show_menu()


func _process(delta: float) -> void:
	if _scene == "STORY" and _story_label != null and _story_idx < GameData.STORY_LINES.size():
		_story_chars += delta * 45.0
		var full: String = GameData.STORY_LINES[_story_idx]
		_story_label.text = full.substr(0, int(_story_chars))
	if (_scene == "ROOM" or _scene == "PUZZLE") and not _over and not _won:
		_tick_second(delta)
	if _timer_label != null and (_scene == "ROOM" or _scene == "PUZZLE"):
		_timer_label.text = time_str()
		_timer_label.add_theme_color_override("font_color", Color(1, 0.35, 0.35) if _remaining < 60 else Color.WHITE)
		_timer_bar.value = 100.0 * float(maxi(_remaining, 0)) / float(GameData.LEVEL_TIME)


var _accum: float = 0.0


func _tick_second(delta: float) -> void:
	_accum += delta
	if _accum >= 1.0:
		_accum = 0.0
		_remaining -= 1
		if _remaining <= 0:
			_remaining = 0
			_over = true
			say("TIME'S UP - SYSTEM LOCKED", Color(1, 0.35, 0.35))


func time_str() -> String:
	return "%02d:%02d" % [_remaining / 60, _remaining % 60]


func say(text: String, color: Color = Color(0.7, 0.7, 0.7)) -> void:
	if _msg != null:
		_msg.text = text
		_msg.add_theme_color_override("font_color", color)


# ---------- ui helpers ----------

func _clear() -> void:
	for c in get_children():
		if c != _audio:
			c.queue_free()
	_timer_label = null
	_msg = null
	_story_label = null


func _title(text: String, size: int = 54) -> Label:
	var l := Label.new()
	l.text = text
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	if _font_title != null:
		l.add_theme_font_override("font", _font_title)
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", Color(0.7, 0.08, 0.08))
	return l


func _label(text: String, size: int = 22) -> Label:
	var l := Label.new()
	l.text = text
	if _font_body != null:
		l.add_theme_font_override("font", _font_body)
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", Color.WHITE)
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	return l


func _btn(text: String) -> Button:
	var b := Button.new()
	b.text = text
	if _font_body != null:
		b.add_theme_font_override("font", _font_body)
	b.add_theme_font_size_override("font_size", 24)
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.23, 0.06, 0.06)
	sb.border_color = Color(0.7, 0.15, 0.15)
	sb.set_border_width_all(2)
	sb.set_corner_radius_all(8)
	b.add_theme_stylebox_override("normal", sb)
	var hov := sb.duplicate()
	hov.bg_color = Color(0.45, 0.1, 0.1)
	b.add_theme_stylebox_override("hover", hov)
	var pr := sb.duplicate()
	pr.bg_color = Color(0.35, 0.08, 0.08)
	b.add_theme_stylebox_override("pressed", pr)
	return b


func _panel() -> PanelContainer:
	var p := PanelContainer.new()
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color(0.05, 0.05, 0.08, 0.95)
	sb.border_color = Color(0.7, 0.15, 0.15)
	sb.set_border_width_all(3)
	sb.set_corner_radius_all(12)
	sb.content_margin_left = 36
	sb.content_margin_right = 36
	sb.content_margin_top = 24
	sb.content_margin_bottom = 24
	p.add_theme_stylebox_override("panel", sb)
	return p


func _centered(node: Control, pos: Vector2, size: Vector2) -> Control:
	node.position = pos
	node.size = size
	add_child(node)
	return node


# ---------- scenes ----------

func show_menu() -> void:
	_scene = "MENU"
	_clear()
	_audio.play_menu()
	var bg := ColorRect.new()
	bg.color = Color(0.03, 0.03, 0.05)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)
	_centered(_title("ESCAPE THE NIGHT"), Vector2(240, 150), Vector2(800, 90))
	var sub := _label("KILL_USER.PY - Server Room  (Godot prototype)", 24)
	sub.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_centered(sub, Vector2(240, 250), Vector2(800, 40))
	var start := _btn("ENTER THE SERVER")
	_centered(start, Vector2(440, 380), Vector2(400, 60))
	start.pressed.connect(func() -> void: show_story())
	var quit := _btn("QUIT")
	_centered(quit, Vector2(440, 455), Vector2(400, 60))
	quit.pressed.connect(func() -> void: get_tree().quit())


func show_story() -> void:
	_scene = "STORY"
	_story_idx = 0
	_story_chars = 0.0
	_clear()
	_audio.stop_all()
	_audio.play_room()
	var bg := ColorRect.new()
	bg.color = Color(0.03, 0.03, 0.05)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)
	var head := _label("CASE FILE - TAREK  (ENTER / CLICK to continue)", 24)
	_centered(head, Vector2(90, 100), Vector2(1100, 40))
	_story_label = _label("", 22)
	_centered(_story_label, Vector2(90, 180), Vector2(1100, 300))
	_next_btn()


func _next_btn() -> void:
	var b := _btn("CONTINUE  >>")
	_centered(b, Vector2(980, 620), Vector2(220, 50))
	b.pressed.connect(advance_story)


func advance_story() -> void:
	if _scene != "STORY":
		return
	var full: String = GameData.STORY_LINES[_story_idx]
	if _story_chars < float(full.length()):
		_story_chars = float(full.length())
		return
	_story_idx += 1
	_story_chars = 0.0
	if _story_idx >= GameData.STORY_LINES.size():
		start_level()
	else:
		show_story_page()


func show_story_page() -> void:
	# rebuild keeping audio playing
	var keep_audio := _audio
	_clear()
	_audio = keep_audio
	var bg := ColorRect.new()
	bg.color = Color(0.03, 0.03, 0.05)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)
	var head := _label("CASE FILE - TAREK  (%d/%d - ENTER / CLICK)" % [_story_idx + 1, GameData.STORY_LINES.size()], 24)
	_centered(head, Vector2(90, 100), Vector2(1100, 40))
	var done := VBoxContainer.new()
	_centered(done, Vector2(90, 180), Vector2(1100, 260))
	for i in range(_story_idx):
		done.add_child(_label(GameData.STORY_LINES[i], 22))
	_story_label = _label("", 22)
	done.add_child(_story_label)
	_next_btn()


func start_level() -> void:
	_remaining = GameData.LEVEL_TIME
	_hint_used = false
	_solved = [false, false, false, false]
	_active = -1
	_over = false
	_won = false
	_accum = 0.0
	show_room()


func _hud(parent_text: String) -> void:
	var bar := ColorRect.new()
	bar.color = Color(0.05, 0.05, 0.06, 0.9)
	bar.position = Vector2(0, 0)
	bar.size = Vector2(1280, 80)
	add_child(bar)
	var left := _label(parent_text, 24)
	left.position = Vector2(30, 12)
	add_child(left)
	_timer_label = _label("TIME " + time_str(), 24)
	_timer_label.position = Vector2(560, 8)
	add_child(_timer_label)
	_timer_bar = ProgressBar.new()
	_timer_bar.min_value = 0
	_timer_bar.max_value = 100
	_timer_bar.value = 100
	_timer_bar.show_percentage = false
	_timer_bar.position = Vector2(560, 48)
	_timer_bar.size = Vector2(220, 14)
	add_child(_timer_bar)
	_msg = _label("", 20)
	_msg.position = Vector2(30, 660)
	_msg.size = Vector2(1220, 30)
	add_child(_msg)


func show_room() -> void:
	_scene = "ROOM"
	_clear()
	var tex: Texture2D = load("res://assets/rooms/room01_server.png")
	if tex != null:
		var tr := TextureRect.new()
		tr.texture = tex
		tr.set_anchors_preset(Control.PRESET_FULL_RECT)
		tr.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		tr.stretch_mode = TextureRect.STRETCH_SCALE
		add_child(tr)
	var shade := ColorRect.new()
	shade.color = Color(0.02, 0.02, 0.05, 0.45)
	shade.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(shade)
	_hud("ROOM 01 | LEVEL 01")
	var names := ["Puzzle 01: Main Terminal", "Puzzle 02: Server Rack", "Puzzle 03: Abandoned Desk", "Puzzle 04: System Logs"]
	var pos := [Vector2(180, 260), Vector2(680, 260), Vector2(180, 400), Vector2(680, 400)]
	for i in range(4):
		var t: String = names[i] + ("  [SOLVED]" if _solved[i] else "")
		var b := _btn(t)
		_centered(b, pos[i], Vector2(420, 90))
		var idx := i
		b.pressed.connect(func() -> void: open_puzzle(idx))
	var hint := _btn("LANTERN HINT (-60s)" if not _hint_used else "LANTERN: EMPTY")
	_centered(hint, Vector2(30, 100), Vector2(260, 45))
	hint.pressed.connect(use_hint)
	if _won:
		var w := _label("LEVEL 01 CLEARED - BADGE: SILVER", 28)
		w.add_theme_color_override("font_color", Color(0.3, 0.8, 0.45))
		w.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		_centered(w, Vector2(340, 560), Vector2(600, 50))
	if _over:
		var o := _label("TIME'S UP - SYSTEM LOCKED", 28)
		o.add_theme_color_override("font_color", Color(1, 0.35, 0.35))
		o.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		_centered(o, Vector2(340, 560), Vector2(600, 50))


func open_puzzle(idx: int) -> void:
	_active = idx
	_scene = "PUZZLE"
	_clear()
	var p: Dictionary = GameData.PUZZLES[idx]
	var shade := ColorRect.new()
	shade.color = Color(0, 0, 0, 0.55)
	shade.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(shade)
	var panel := _panel()
	_centered(panel, Vector2(80, 110), Vector2(1120, 500))
	var vb := VBoxContainer.new()
	vb.add_theme_constant_override("separation", 10)
	panel.add_child(vb)
	vb.add_child(_title(p["title"], 34))
	for line in p["prompt"]:
		vb.add_child(_label(line, 22))
	vb.add_child(_label("Code:", 22))
	for c in p["code"]:
		var code_l := _label("   " + c, 22)
		code_l.add_theme_color_override("font_color", Color(0.65, 0.65, 0.7))
		vb.add_child(code_l)
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 16)
	vb.add_child(row)
	var ans := LineEdit.new()
	ans.custom_minimum_size = Vector2(520, 48)
	ans.placeholder_text = "type answer + ENTER"
	if _font_body != null:
		ans.add_theme_font_override("font", _font_body)
	ans.add_theme_font_size_override("font_size", 24)
	row.add_child(ans)
	ans.text_submitted.connect(func(_t: String) -> void: submit(ans.text))
	var sub := _btn("SUBMIT")
	sub.custom_minimum_size = Vector2(200, 48)
	row.add_child(sub)
	sub.pressed.connect(func() -> void: submit(ans.text))
	var back := _btn("BACK (ESC)")
	back.custom_minimum_size = Vector2(200, 48)
	row.add_child(back)
	back.pressed.connect(func() -> void: show_room())
	_msg = _label("", 20)
	vb.add_child(_msg)
	ans.grab_focus()


func use_hint() -> void:
	if _hint_used:
		say("LANTERN ALREADY USED", Color(0.9, 0.75, 0.35))
		return
	for i in range(4):
		if not _solved[i]:
			_hint_used = true
			_remaining = maxi(0, _remaining - GameData.HINT_PENALTY)
			say("HINT P%d: %s" % [i + 1, GameData.PUZZLES[i]["hint"]], Color(0.9, 0.75, 0.35))
			if _scene == "ROOM":
				show_room()
				say("HINT P%d: %s" % [i + 1, GameData.PUZZLES[i]["hint"]], Color(0.9, 0.75, 0.35))
			return


func submit(raw: String) -> void:
	if _active < 0 or _over or _won:
		return
	var p: Dictionary = GameData.PUZZLES[_active]
	var ans: String = raw.strip_edges()
	var ok: bool = (ans == p["answer"]) if bool(p["exact"]) else (ans.to_upper() == String(p["answer"]).to_upper())
	if ok:
		_solved[_active] = true
		var all := true
		for s in _solved:
			all = all and bool(s)
		if all:
			_won = true
			SaveSystem.set_badge(PLAYER, 1, "SILVER")
			level_cleared()
		else:
			say("PUZZLE %02d SOLVED!" % int(p["id"]), Color(0.3, 0.8, 0.45))
			open_puzzle(_active)
			say("PUZZLE %02d SOLVED!" % int(p["id"]), Color(0.3, 0.8, 0.45))
	else:
		_remaining = maxi(0, _remaining - GameData.WRONG_PENALTY)
		say("WRONG! -%ds penalty" % GameData.WRONG_PENALTY, Color(1, 0.35, 0.35))
		if _remaining == 0:
			_over = true
			show_room()


func level_cleared() -> void:
	_scene = "WIN"
	_clear()
	var panel := _panel()
	_centered(panel, Vector2(340, 200), Vector2(600, 320))
	var vb := VBoxContainer.new()
	vb.add_theme_constant_override("separation", 16)
	vb.alignment = BoxContainer.ALIGNMENT_CENTER
	panel.add_child(vb)
	var t := _title("LEVEL 01 CLEARED", 44)
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vb.add_child(t)
	var b := _label("BADGE: SILVER  (saved to users.csv)", 24)
	b.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	vb.add_child(b)
	var menu := _btn("MAIN MENU")
	vb.add_child(menu)
	menu.pressed.connect(func() -> void: show_menu())
	var again := _btn("PLAY AGAIN")
	vb.add_child(again)
	again.pressed.connect(func() -> void: start_level())


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		var k := (event as InputEventKey).keycode
		if _scene == "STORY" and (k == KEY_ENTER or k == KEY_KP_ENTER or k == KEY_SPACE):
			advance_story()
		elif _scene == "PUZZLE" and k == KEY_ESCAPE:
			show_room()
		elif _scene == "ROOM" and k == KEY_ESCAPE:
			show_menu()
