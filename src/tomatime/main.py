from tomatime.ui.interface import App
from tomatime.core.config import Config

if __name__ == "__main__":
    config = Config()
    app = App(config)
    app.mainloop()