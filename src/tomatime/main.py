from tomatime.interface import App
from tomatime.config import Config

if __name__ == "__main__":
    config = Config()
    app = App(config)
    app.mainloop()