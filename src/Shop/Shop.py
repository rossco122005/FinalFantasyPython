import json
with open("src/Shop/items.json", "r") as items_read_file:
    items_from_json = json.load(items_read_file)


class Shop:
    def __init__(self):
        self.items = items_from_json

    def open_shop(self):
        print()
        print("----------Shop----------")
        print("Items for sale:")
        print()
        for item in self.items:
            print(item + "\t" + "Price: ", self.items[item].get("price"))

        print()
