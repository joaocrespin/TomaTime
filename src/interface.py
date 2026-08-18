import tkinter as tk
from pomodoro import PomodoroFrame

class App(tk.Tk):
    def __init__(self, time_data: dict):
        super().__init__()

        self.title("TomaTime")
        self.geometry("500x500")

        self.pomodoro_frame = PomodoroFrame(self, time_data)
        self.pomodoro_frame.pack(fill=tk.BOTH, expand=True)