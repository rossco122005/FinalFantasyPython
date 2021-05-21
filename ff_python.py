import sys
sys.path.append(".")
from BaseCharacter import BaseCharacter
from Hero import Hero
from Potion import Potion


def main_game():
    print("----------Final Fantasy Python!----------")
    hero = Hero("Hero")
    monster = BaseCharacter("Goblin")
    choice = "99"
    while choice != "0":
        print(hero.get_name() + " ", hero.get_hp())
        print(monster.get_name() + " ", monster.get_hp())

        potion_1 = Potion()
        potion_1.add_potion()
        hero.add_item(potion_1)

        print("Please choose one of the following:")
        print("1. Attack")
        print("2. Items")
        print("0. Quit")
        choice = input("Please choose: ")

        if choice == "1":
            monster.be_attacked(hero.attack_with_weapon())
        if choice == "2":
            print("----------Items----------")
            hero.display_items()
        elif choice == "0":
            print("Quitting")
        else:
            print("Incorrect input, please try again")


main_game()
