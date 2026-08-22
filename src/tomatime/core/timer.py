from tkinter import Label
from tomatime.core.notification import notify

# TODO: Identify if it's break time or focus time (custom messages)

def tick(time: str, label: Label) -> bool:
    seconds = text_to_seconds(time)
    if seconds > 0:
        seconds  -= 1
        text = seconds_to_text(seconds)
        label.config(text=text)
        return True
    else:
        notify("Time's up!", "Time's up! Break or another round?")
    return False

def text_to_seconds(time: str) -> int:
    parts = time.split(':')
    if len(parts) != 2:
        raise ValueError("Expected 'MM:SS' format")
    try:
        minutes, seconds = int(parts[0]) * 60, int(parts[1])
    except ValueError:
        raise ValueError("Invalid time format")
    if minutes < 0 or seconds < 0:
        raise ValueError("Time cannot be negative")
    return minutes + seconds

def seconds_to_text(time: int) -> str:
    try:
        if time < 0:
            raise ValueError("Time cannot be negative")
        minutes, seconds = divmod(time, 60)
        #print(minutes, seconds)
    except TypeError:
        raise Exception("Time must be an number")
    return f'{minutes:02d}:{seconds:02d}'