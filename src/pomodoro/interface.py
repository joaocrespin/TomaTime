import tkinter as tk
from timer import tick
from threading import Thread

root = tk.Tk()

root.title("Pomodoro")
root.geometry("500x500")

time_ticking: bool = False

def update() -> None:
    tick(time_label.cget("text"), time_label)
    time_label.after(1000, update)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

time_label = tk.Label(frame, text="01:01")
time_label.pack(pady=10)

tomato = tk.Button(frame, text="Tomato", command=lambda: update())
tomato.pack()

start = tk.Label(frame, text="Pomodoro")
start.pack(pady=10)


root.mainloop()