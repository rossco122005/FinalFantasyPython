class Item:
    def __init__(self):
        self.name = ""
        self.amount = 0

    def get_amount(self):
        return self.amount

    def get_item_name(self):
        return self.name

    def increase_item(self):
        self.amount = self.amount + 1
