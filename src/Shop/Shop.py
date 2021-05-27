from src.Items.Potion import Potion
from src.Items.Ether import Ether


class Shop:
    def __init__(self):
        self.items = {
            "Potion": {
                "hp_healed": 100,
                "price": 50
            },

            "Ether": {
                "mp_healed": 20,
                "price": 150
            }
        }

    def open_shop(self):
        print()
        print("----------Shop----------")
        print("Items for sale:")
        print()
        for item in self.items:
            print(item + "\t" + "Price: ", self.items[item].get("price"))

        print()
