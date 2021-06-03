import json

with open("items.json", "r") as items_read:
    items = json.load(items_read)

print(items)
