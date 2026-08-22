import tkinter as tk
from tomatime.timer import tick


class PomodoroFrame(tk.Frame):
    def __init__(self, master, config: Config):
        super().__init__(master)

        self.config = config
        self.time_data = config.load_config()
        self.time_ticking: bool = False

        self.frame = tk.Frame(self)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.time_label = tk.Label(self.frame, text=self.time_data["focus_time"])
        self.time_label.pack(pady=10)

        self.tomato = tk.Button(self.frame, text="Tomato", command=lambda: self.time_tick())
        self.tomato.pack()

        self.start = tk.Label(self.frame, text="Pomodoro")
        self.start.pack(pady=10)

        # Botões de tomatime e break
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.place(relx=0.5, rely=1, anchor=tk.S)

        self.focus_button = tk.Button(self.bottom_frame, text="Focus", command=self.focus_time)
        self.focus_button.pack(side=tk.LEFT)

        self.break_button = tk.Button(self.bottom_frame, text="Break", command= self.break_time)
        self.break_button.pack(side=tk.LEFT)

    def time_tick(self) -> None:
        if self.time_ticking:
            self.time_ticking = False
            return
        self.time_ticking = True
        self.update()

    def update(self) -> None:
        if self.time_ticking:
            time_left = tick(self.time_label.cget("text"), self.time_label)
            if time_left:
                self.time_label.after(1000, self.update)

    def stop_time(self) -> None:
        self.time_ticking = False

    def break_time(self) -> None:
        self.stop_time()
        self.time_label.config(text=self.time_data["break_time"])

    def focus_time(self) -> None:
        self.stop_time()
        self.time_label.config(text=self.time_data["focus_time"])


