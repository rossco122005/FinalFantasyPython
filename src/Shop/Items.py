import json

items = {
    "Potion": {
        "hp_healed": 100,
        "price": 50
    },

    "Ether": {
        "mp_healed": 20,
        "price": 150
    }
}

with open("items.json", "w") as items_file:
    json.dump(items, items_file)
