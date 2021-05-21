import sys
sys.path.append(".")
from BaseCharacter import BaseCharacter
from Weapon import Weapon


class Hero(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = Weapon()
        self.item_list = []

    def attack_with_weapon(self):
        damage = BaseCharacter.attack(self)
        damage = damage + self.weapon.get_damage()
        return damage

    def add_item(self, item):
        self.item_list.append(item)

    def display_items(self):
        print(self.item_list)
