from src.Characters.BaseCharacter import BaseCharacter
from src.Weapons.Weapon import Weapon


class Hero(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = Weapon()
        self.item_dict = {}

    def attack_with_weapon(self):
        damage = BaseCharacter.attack(self)
        damage = damage + self.weapon.get_damage()
        return damage

    def add_item(self, item_name, item_attribute_name, item_attribute_value):
        # Adds 1 to the current amount in the Hero's inventory if the item already exists
        # If it doesn't then it adds a new entry to the dictionary
        if item_name in self.item_dict:
            self.item_dict.update({
                item_name: {
                    item_attribute_name: item_attribute_value,
                    "amount": self.item_dict.get(item_name).get("amount") + 1
                }
            })
        else:
            self.item_dict.update({
                item_name: {
                    item_attribute_name: item_attribute_value,
                    "amount": 1
                }
            })

    def display_items(self):
        print(self.item_dict)
        print()
        for item in self.item_dict:
            print(item + "\t\t:", self.item_dict.get(item).get("amount"))
