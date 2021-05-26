from src.Items.Potion import Potion
from src.Items.Ether import Ether


class Shop:
    def __init__(self):
        self.potion_for_sale = Potion()
        self.ether_for_sale = Ether()

    def open_shop(self):
        print("----------Shop----------")
        print("Items for sale:")
        print()
        print(self.potion_for_sale.get_item_name() + "\t50G")
        print(self.ether_for_sale.get_item_name() + "\t150G")
        print()
        choice = "99"
        #3if choice ==
