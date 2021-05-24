from src.Items.Item import Item


class Ether(Item):
    def __init__(self):
        super().__init__()
        self.name = "Ether"
        self.mp_healed = 20

    def heal(self):
        return self.mp_healed
