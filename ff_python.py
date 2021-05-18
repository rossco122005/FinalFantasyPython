import random


class BaseCharacter:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 0
        self.attack = 5
        self.defense = 0

    def attack(self):
        return self.attack

    def be_attacked(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp


class Hero(BaseCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = Weapon()

    def attack_with_weapon(self):
        damage = BaseCharacter.attack(self)
        damage = damage + self.weapon.get_damage()
        return damage


class Weapon:
    def __init__(self):
        self.name = ""
        self.damage = 3

    def get_damage(self):
        return self.damage


def main_game():
    print("----------Final Fantasy Python!----------")
    hero = Hero("Hero")
    monster = BaseCharacter("Goblin")
    choice = "99"
    while choice != "0":
        print(hero.get_name() + " ", hero.get_hp())
        print(monster.get_name() + " ", monster.get_hp())

        print("Please choose one of the following:")
        print("1. Attack")
        print("0. Quit")
        choice = input("Please choose: ")

        if choice == "1":
            monster.be_attacked(hero.attack_with_weapon())
        elif choice == "0":
            print("Quitting")


main_game()
