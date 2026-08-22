import tkinter as tk
from tkinter import messagebox as mb


class SettingsFrame(tk.Frame):
    def __init__(self, master, config: Config):
        super().__init__(master)

        self.master = master;
        self.config = config
        self.time_data = config.load_config()

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.main_label = tk.Label(self.frame, text="Settings")
        self.main_label.grid(row=0, column=2)

        self.time_label = tk.Label(self.frame, text="Time (minutes)")
        self.time_label.grid(row=1, column=2)

        # Validate entry on write
        vcmd: tuple = (self.register(self.on_key_validate), '%P')

        # Focus time
        self.focus_label = tk.Label(self.frame, text="Focus Time")

        self.focus_label.grid(row=2, column=0)
        self.focus_time_entry = tk.Entry(self.frame, justify="center", validate="key", validatecommand=vcmd)
        self.focus_time_entry.insert(tk.END, self.time_data["focus_time"])
        self.focus_time_entry.grid(row=3, column=0)

        # Break time
        self.break_label = tk.Label(self.frame, text="Break Time")
        self.break_label.grid(row=2, column=3)
        self.break_time_entry = tk.Entry(self.frame, justify="center", validate="key", validatecommand=vcmd)
        self.break_time_entry.insert(tk.END, self.time_data["break_time"])
        self.break_time_entry.grid(row=3, column=3)

        # Save
        self.save_button = tk.Button(self.frame, text="Save", command=self.save_time)
        self.save_button.grid(row=4, column=2)

    def on_key_validate(self, value: str) -> bool:
        return value == "" or value.isdigit()

    def validate_number(self, value: str) -> int:
        try:
            number = int(value)
        except ValueError:
            raise ValueError(f'"{value}" is not a number')
        if number <= 0:
            raise ValueError("Must be a positive integer")
        return number

    def save_time(self) -> None:
        try:
            focus_time = self.validate_number(self.focus_time_entry.get())
            break_time = self.validate_number(self.break_time_entry.get())
            self.config.set_config(str(focus_time), str(break_time))
        except Exception as e:
            print("Error saving time:", e)
            mb.showwarning("Warning", str(e))

