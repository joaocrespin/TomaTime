from pomodoro.timer import text_to_seconds
from pytest import raises

def test_text_to_seconds():
    result = text_to_seconds("10:00")
    assert result == 600

def test_negative_text_to_seconds():
    with raises(ValueError, match="Time cannot be negative"):
        text_to_seconds("-12:00")

def test_character_text_to_seconds():
    with raises(ValueError, match="Invalid time format"):
        text_to_seconds("ab:cd")

def test_with_hours_text_to_seconds():
    with raises(ValueError, match="Expected 'MM:SS' format"):
        text_to_seconds("10:00:00")

def test_number_text_to_seconds():
    with raises(ValueError, match="Expected 'MM:SS' format"):
        text_to_seconds("999")

def test_empty_text_to_seconds():
    with raises(ValueError, match="Expected 'MM:SS' format"):
        text_to_seconds("")