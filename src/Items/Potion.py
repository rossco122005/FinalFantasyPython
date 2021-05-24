from src.Items.Item import Item


class Potion(Item):
    def __init__(self):
        super().__init__()
        self.name = "Potion"
        self.hp_healed = 100

    def heal(self):
        return self.hp_healed
