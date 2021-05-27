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

x = items["Potion"].get("hp_healed")

print(x)

with open("items.json", "w") as items_file:
    json.dump(items, items_file)

with open("items.json", "r") as items_read_file:
    items_from_json = json.load(items_read_file)

print(items_from_json)

y = items_from_json["Potion"].get("hp_healed")

print(y)
