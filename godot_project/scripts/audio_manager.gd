class_name AudioManager
extends Node
## Two channels like the Pygame version: bg loop + voiceover once.

var _bg: AudioStreamPlayer
var _voice: AudioStreamPlayer


func _ready() -> void:
	_bg = AudioStreamPlayer.new()
	_bg.bus = "Master"
	add_child(_bg)
	_voice = AudioStreamPlayer.new()
	add_child(_voice)


func _stream(path: String, loop: bool) -> AudioStream:
	if not ResourceLoader.exists(path):
		return null
	var s: AudioStream = load(path)
	if s is AudioStreamMP3 and loop:
		(s as AudioStreamMP3).loop = true
	return s


func play_menu() -> void:
	var s := _stream("res://assets/audio/Game_Background.mp3", true)
	if s != null:
		_bg.stream = s
		_bg.play()


func play_room() -> void:
	var s := _stream("res://assets/audio/Kill_User_Background.mp3", true)
	if s != null:
		_bg.stream = s
		_bg.play()
	var v := _stream("res://assets/audio/Kill_User_voiceover.mp3", false)
	if v != null:
		_voice.stream = v
		_voice.play()


func stop_all() -> void:
	_bg.stop()
	_voice.stop()
