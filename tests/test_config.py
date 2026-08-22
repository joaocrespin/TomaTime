import json
import pytest
from pathlib import Path
from tomatime.core.config import Config

@pytest.fixture
def config_path(tmp_path: Path) -> Path:
    return tmp_path / "config" / "config.json"

def test_missing_file_load_config(config_path: Path) -> None:
    config = Config(config_path)
    result = config.load_config()
    assert result == {"focus_time": "25:00","break_time": "5:00",}
    assert config_path.exists()

def test_existing_file_load_config(config_path: Path) -> None:
    config_path.parent.mkdir(parents=True)
    config_path.write_text(json.dumps({"focus_time": "50:00", "break_time": "10:00"}))
    config = Config(file_path=config_path)
    result = config.load_config()
    assert result == {"focus_time": "50:00", "break_time": "10:00"}

def test_set_config(config_path: Path) -> None:
    config = Config(file_path=config_path)
    config.load_config()
    config.set_config("30:00", "7:00")
    result = config.load_config()
    assert result == {"focus_time": "30:00", "break_time": "7:00"}
