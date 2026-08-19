import tkinter as tk


class SettingsFrame(tk.Frame):
    def __init__(self, master, config: Config):
        super().__init__(master)

        self.master = master;
        self.config = config

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.main_label = tk.Label(self.frame, text="Settings")
        self.main_label.grid(row=0, column=2)

        self.time_label = tk.Label(self.frame, text="Time (minutes)")
        self.time_label.grid(row=1, column=2)

        # Focus time
        self.focus_label = tk.Label(self.frame, text="Focus Time")

        self.focus_label.grid(row=2, column=0)
        self.focus_time_entry = tk.Entry(self.frame, justify="center")
        self.focus_time_entry.insert(tk.END, "25")
        self.focus_time_entry.grid(row=3, column=0)

        # Break time
        self.break_label = tk.Label(self.frame, text="Break Time")
        self.break_label.grid(row=2, column=3)
        self.break_time_entry = tk.Entry(self.frame, justify="center")
        self.break_time_entry.insert(tk.END, "5")
        self.break_time_entry.grid(row=3, column=3)

        # Save
        self.save_button = tk.Button(self.frame, text="Save", command=self.save_time)
        self.save_button.grid(row=4, column=2)

    def save_time(self) -> None:
        focus_time = int(self.focus_time_entry.get())
        break_time = int(self.break_time_entry.get())
        self.config.set_config(str(focus_time) + ":00", str(break_time) + ":00")
