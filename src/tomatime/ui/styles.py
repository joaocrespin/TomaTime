from tkinter import Tk, ttk


COLORS = {
    "bg": "#a8c94a",
    "fg": "#fefaf0",
    "accent": "#c0392b",
    "accent_dark": "#7a1f1a",
    "circle": "#6b8e23",
    "text_dark": "#2d2a1f",
}

def apply_theme(root: Tk):
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("TFrame", background=COLORS["bg"])
    style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["fg"], font=("", 18, "bold"))
    style.configure("TButton", background=COLORS["accent"], foreground=COLORS["fg"], bordercolor=COLORS["accent_dark"],
        lightcolor=COLORS["accent"], darkcolor=COLORS["accent_dark"], borderwidth=1, focuscolor=COLORS["bg"])
    style.map("TButton", background=[("active", COLORS["accent_dark"])])
    style.configure("Timer.TLabel", background=COLORS["bg"], foreground=COLORS["fg"], font=("", 24, "bold"))