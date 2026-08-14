import tkinter as tk
from timer import count_time, tick

root = tk.Tk()

root.title("Pomodoro")
root.geometry("500x500")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

time_label = tk.Label(frame, text="00:00")
time_label.pack(pady=10)

tomato = tk.Button(frame, text="Tomato", command=lambda: count_time(10, time_label))
tomato.pack()

start = tk.Label(frame, text="Pomodoro")
start.pack(pady=10)

root.mainloop()