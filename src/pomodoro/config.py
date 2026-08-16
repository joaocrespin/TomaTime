import json
from pathlib import Path


class Config:
    def __init__(self, file_path: Path = Path("config/config.json")) -> None:
        self.file_path = file_path

    def load_config(self) -> dict:
        if self.file_path.exists():
            json_data = json.load(open(self.file_path))
            return json_data
        else:
            time_data = {
                "focus_time": "25:00",
                "break_time": "5:00",
            }
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            self.set_config(time_data["focus_time"], time_data["break_time"])
            return time_data

    def set_config(self, new_focus_time: str, new_break_time: str) -> None:
        time_data = {
                     "focus_time": new_focus_time,
                     "break_time": new_break_time,
                     }
        with open(self.file_path, "w") as f:
            json.dump(time_data, f)
