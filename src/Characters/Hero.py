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

    def add_item(self, item):
        self.item_dict.update(item)

    def display_items(self):
        print(self.item_dict)
        # for item in self.item_dict:
            # print(item)

