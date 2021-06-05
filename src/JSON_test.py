# Simple file for trying out things for JSON and accessing dictionaries

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
items.update({
    "Grenade": {
        "damage_dealt": 100,
        "price": 250
    }
})

print(x)

with open("items.json", "w") as items_file:
    json.dump(items, items_file)

with open("items.json", "r") as items_read_file:
    items_from_json = json.load(items_read_file)

print(items_from_json)

y = items_from_json["Potion"].get("hp_healed")
z = items_from_json.get("Potion").get("hp_healed")
a = items_from_json.get("Potion")

print(y)
print(z)
print(a)
print(items.keys())
print(list(items)[2])
