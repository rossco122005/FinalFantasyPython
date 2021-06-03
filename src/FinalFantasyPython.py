from src.Characters.BaseCharacter import BaseCharacter
from src.Characters.Hero import Hero
from src.Shop.Shop import Shop


def main_game():
    print("----------Final Fantasy Python!----------")
    hero = Hero("Hero")
    monster = BaseCharacter("Goblin")
    shop = Shop()

    choice = "99"
    while choice != "0":
        print()
        print("Current Characters: ")
        print(hero.get_name() + " ", hero.get_hp())
        print(monster.get_name() + " ", monster.get_hp())
        print()

        print("Please choose one of the following:")
        print("1. Attack")
        print("2. Items")
        print("3. Shop")
        print("0. Quit")
        choice = input("Please choose: ")

        if choice == "1":
            monster.be_attacked(hero.attack_with_weapon())

        elif choice == "2":
            print("----------Items----------")
            hero.display_items()
            print()

        elif choice == "3":
            shop.open_shop()

            print("Please choose one of the following:")
            print("1. To buy a Potion")
            print("2. To buy an Ether")
            print("0. To leave the shop")
            choice = input("Please choose: ")
            if choice == "1":
                # hero.add_item(shop.items["Potion"])
                print(shop.items["Potion"])
                print(list(shop.items)[0])
                # hero.add_item(shop.items["Potion"]["hp_healed"])
            elif choice == "2":
                hero.add_item(shop.items["Ether"])
            elif choice == "0":
                print("Leaving shop...")

        elif choice == "0":
            print("Quitting")
        else:
            print("Incorrect input, please try again")


main_game()
