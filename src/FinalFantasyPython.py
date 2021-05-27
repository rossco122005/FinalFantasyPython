from src.Characters.BaseCharacter import BaseCharacter
from src.Characters.Hero import Hero
from src.Items.Potion import Potion
from src.Shop.Shop import Shop


def main_game():
    print("----------Final Fantasy Python!----------")
    hero = Hero("Hero")
    monster = BaseCharacter("Goblin")
    shop = Shop()

    choice = "99"
    while choice != "0":
        print(hero.get_name() + " ", hero.get_hp())
        print(monster.get_name() + " ", monster.get_hp())

        # potion_1 = Potion()
        # potion_1.increase_item()
        # hero.add_item(potion_1)

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
            # for potion in hero.item_list:
                # print(potion.get_item_name() + "\t" + "Amount:", potion.get_amount())
            hero.display_items()
            print()
        elif choice == "3":
            shop.open_shop()
            item_choice = "99"
            print("Please choose one of the following:")
            print("1. To buy a Potion")
            print("2. To buy an Ether")
            print("0. To leave the shop")
            choice = input("Please choose: ")
            if choice == "1":
                hero.add_item(shop.items["Potion"])
            elif choice == "2":
                hero.add_item(shop.items["Ether"])
            elif choice == "0":
                print("Leaving shop...")
        elif choice == "0":
            print("Quitting")
        else:
            print("Incorrect input, please try again")


main_game()
