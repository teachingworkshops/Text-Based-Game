from bank import bank_scene
from Player import Player
from Room import Room


def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    sheriff = Player("Sheriff")
    enemy = Player("Robber")

    jail_room = Room("Jail")
    jail_room.add_item("Badge")

    sheriff.set_room(jail_room)

    jail_room.display_items()

    # Testing player class
    sheriff.set_weapon("Pistol")
    sheriff.display_stats()
    sheriff.display_weapons()

    enemy.display_stats()

    bank_scene()


def main():
    start_game()


if __name__ == "__main__":
    main()
