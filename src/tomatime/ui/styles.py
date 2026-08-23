import tkinter as tk
from tkinter import Tk, ttk
from PIL import Image, ImageTk

COLORS = {
    "bg": "#a8c94a",
    "fg": "#fefaf0",
    "accent": "#c0392b",
    "accent_dark": "#7a1f1a",
    "circle": "#6b8e23",
    "text_dark": "#2d2a1f",
    "tomato_bg": "#fb0200",
}

def apply_theme(root: Tk):
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("TFrame", background=COLORS["bg"])
    style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["fg"], font=("", 18, "bold"))
    style.configure("TButton", background=COLORS["accent"], foreground=COLORS["fg"], bordercolor=COLORS["accent_dark"],
        lightcolor=COLORS["accent"], darkcolor=COLORS["accent_dark"], borderwidth=1, focuscolor=COLORS["bg"])
    style.map("TButton", background=[("active", COLORS["accent_dark"])])
    style.configure("Tomato.TFrame", background=COLORS["tomato_bg"])
    style.configure("Timer.TLabel", background=COLORS["tomato_bg"], foreground=COLORS["fg"], font=("", 24, "bold"))

def add_background(frame: tk.Widget, image_path: str, size: tuple[int, int]) -> ImageTk.PhotoImage:
    img = Image.open(image_path).resize(size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    bg_label = tk.Label(frame, image=photo, borderwidth=0)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()
    return photo