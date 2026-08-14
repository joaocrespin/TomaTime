import threading
from tkinter import Label

def count_time(time: int, label: Label) -> None:
    print("clicado")
    if time < 0:
        raise Exception("Time must be greater than or equal to 0")
    while time:
        print(time)
        label.after(time, count_time)
        threading.Event().wait(1)
        time-=1

def tick(time: int, label: Label) -> None:
    # Formata pra segundos
    seconds = text_to_seconds(time)
    # Diminui em um segundo o tempo
    #reformata pra devolver pra label
    pass

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
    minutes, seconds = divmod(time, 60)
    return f'{minutes:02d}:{seconds:02d}'