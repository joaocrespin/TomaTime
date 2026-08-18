import tkinter as tk

class SettingsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master;

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.time_label = tk.Label(self.frame, text="01:01")
        self.time_label.pack(pady=10)