import tkinter as tk
from tkinter import ttk
from tomatime.core.timer import tick
from tomatime.ui.styles import add_background

class PomodoroFrame(ttk.Frame):
    def __init__(self, master, config: Config):
        super().__init__(master)

        self.config = config
        self.time_data = config.load_config()
        self.time_ticking: bool = False
        self.focused: bool  = True

        self.bg_photo = add_background(self, "src/assets/images/tomato.jpg", (500, 500))

        self.frame = ttk.Frame(self, style="Tomato.TFrame")
        self.frame.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

        self.time_label = ttk.Label(self.frame, text=self.format_time(self.time_data["focus_time"]), style="Timer.TLabel")
        self.time_label.pack(pady=10)

        self.tomato = ttk.Button(self.frame, text="Tomato", command=lambda: self.time_tick())
        self.tomato.pack()

        # Botões de tomatime e break
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.place(relx=0.5, rely=1, anchor=tk.S)

        self.focus_button = ttk.Button(self.bottom_frame, text="Focus", command=self.focus_time)
        self.focus_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.break_button = ttk.Button(self.bottom_frame, text="Break", command= self.break_time)
        self.break_button.pack(side=tk.LEFT, padx=10, pady=10)

    def time_tick(self) -> None:
        if self.time_ticking:
            self.time_ticking = False
            return
        self.time_ticking = True
        self.update()

    def update(self) -> None:
        if self.time_ticking:
            time_left = tick(self.time_label.cget("text"), self.time_label, self.focused)
            if time_left:
                self.time_label.after(1000, self.update)
            else:
                self.time_ticking = False

    def stop_time(self) -> None:
        self.time_ticking = False

    def break_time(self) -> None:
        self.stop_time()
        self.focused = False
        self.time_label.config(text=self.format_time(self.time_data["break_time"]))

    def focus_time(self) -> None:
        self.stop_time()
        self.focused = True
        self.time_label.config(text=self.format_time(self.time_data["focus_time"]))

    def format_time(self, time: int) -> str:
        return f"{time}:00"


