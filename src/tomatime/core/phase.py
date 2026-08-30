class Phase():
    def __init__(self):
        self.focused: bool = True

    def change_phase(self, focused: bool) -> None:
        self.focused = focused