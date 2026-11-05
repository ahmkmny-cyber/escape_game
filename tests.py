import pytest
import player_data

@pytest.mark.parametrize("room_number, badge",[(1, "SILVER"),(2, "GOLD"),(3, "SILVER")])
def test_update_room_badge(room_number, badge):
    player_data.update_room_badge("jana",room_number,badge)
    player = player_data.get_player_data("jana")
    assert player is not None
    assert player[f"room{room_number}_badge"] == badge
    
def test_unknown_player_returns_none():
    player = player_data.get_player_data("UnknownPlayer")
    assert player is None
    
def test_missing_csv_file():
    with pytest.raises(FileNotFoundError):
        player_data.get_player_data("TestPlayer")