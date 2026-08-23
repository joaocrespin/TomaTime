# TomaTime 🍅

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

A simple, local desktop Pomodoro timer with focus/break cycles, sound + system notifications and configurable durations. Built as a portfolio project to practice clean structure and dependency injection in a small Python desktop app.

---

## Features

- Focus and break countdown timer with start/pause control
- Desktop notifications (via `plyer`) and a notification sound (via `playsound3`) when a phase ends
- Different notification messages depending on whether focus or break just finished
- Configurable focus/break durations, persisted locally in a JSON config file
- Manual phase switching between Focus and Break
- Custom themed UI built with `tkinter`/`ttk`
- Unit tested timer and config logic with `pytest`

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Tkinter / ttk | Desktop UI |
| plyer | Cross-platform desktop notifications |
| playsound3 | Notification sound playback |
| JSON | Local persistence of timer settings |
| Pytest | Unit testing |
| uv | Project and dependency management |

---

## Project Structure

```
TomaTime/
├── src/
│   └── tomatime/
│       ├── core/
│       │   ├── config.py        # Load/save timer settings (JSON)
│       │   ├── notification.py  # Desktop notification + sound
│       │   └── timer.py         # Countdown logic (tick, time parsing)
│       ├── ui/
│       │   ├── interface.py     # Main App window
│       │   ├── pomodoro.py      # Pomodoro timer frame
│       │   ├── settings.py      # Settings frame
│       │   └── styles.py        # Theme and colors
│       └── main.py
├── tests/
│   ├── test_config.py
│   └── test_timer.py
├── pyproject.toml
└── README.md
```

---

## Running Locally

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) installed

### Setup

```bash
# Clone the repository
git clone https://github.com/joaocrespin/TomaTime.git
cd TomaTime

# Install dependencies
uv sync
```

### Start the app

```bash
uv run src/tomatime/main.py
```

On first run, TomaTime creates a `config/config.json` file with default durations (25 min focus / 5 min break), which you can adjust from the in-app Settings screen.

---

## Running Tests

```bash
uv run pytest
```

---

## How It Works

- **Focus** and **Break** are separate phases controlled from the main window; switching phases resets the timer to the configured duration for that phase.
- The **Tomato** button starts, pauses, and resumes the countdown.
- Durations are set in the **Settings** screen and saved to a local JSON file, so they persist between runs.

---

## TODO

- Automatic transition between focus and break phases
- Long break after every N focus sessions
- Session history / daily pomodoro count
- System tray support