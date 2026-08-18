from timer import text_to_seconds, seconds_to_text
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

def test_seconds_to_text():
    result = seconds_to_text(600)
    assert result == "10:00"

def test_many_seconds_to_text():
    result = seconds_to_text(40982)
    assert result == "683:02"

def test_zero_seconds_to_text():
    result = seconds_to_text(0)
    assert result == "00:00"

def test_negative_seconds_to_text():
    with raises(ValueError, match="Time cannot be negative"):
        seconds_to_text(-12)

#def test_float_seconds_to_text():
#    result = seconds_to_text(4982.5)
#    assert result == "83:02"

def test_character_seconds_to_text():
    with raises(Exception, match="Time must be an number"):
        seconds_to_text("abcd")

def test_empty_seconds_to_text():
    with raises(Exception, match="Time must be an number"):
        seconds_to_text("")