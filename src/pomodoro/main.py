from interface import App
from config import Config

if __name__ == "__main__":
    config = Config()
    time_data = config.load_config()
    app = App(time_data)
    app.mainloop()