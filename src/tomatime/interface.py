import tkinter as tk
from tomatime.pomodoro import PomodoroFrame
from tomatime.settings import SettingsFrame


class App(tk.Tk):
    def __init__(self, config: Config):
        super().__init__()

        self.title("TomaTime")
        self.geometry("500x500")

        self.config = config

        self.pomodoro_frame = PomodoroFrame(self, config)
        self.pomodoro_frame.pack(fill=tk.BOTH, expand=True)

        self.settings_frame = SettingsFrame(self, config)

        # Config
        self.top_frame = tk.Frame(self)
        self.top_frame.place(relx=0.8, rely=0, anchor=tk.NW)
        self.settings_button = tk.Button(self.top_frame, text="Settings", command=self.open_settings)
        self.settings_button.pack()


    def hide_all_frames(self)-> None:
        self.pomodoro_frame.pack_forget()
        self.settings_frame.place_forget()

    def open_settings(self) -> None:
        self.hide_all_frames()
        self.settings_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.settings_button["text"] = "Return"
        self.settings_button["command"] = self.return_pomodoro

    def return_pomodoro(self) -> None:
        self.hide_all_frames()
        self.pomodoro_frame.time_data = self.config.load_config()
        self.pomodoro_frame.pack(fill=tk.BOTH, expand=True)
        self.settings_button["text"] = "Settings"
        self.settings_button["command"] = self.open_settings
