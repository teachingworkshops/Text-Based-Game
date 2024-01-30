from bank import bank_scene
from Character import Character
from Room import Room


def new_room(character):
    if character.room.number_Visits < 1:
        character.room.trigger_Event()


def initialize_jail():
    room_list = {Room("Jail"), Room("Main Street"), Room("Bank"), Room("Saloon"), Room("General Store")}
    return room_list


def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    sheriff = Character("Sheriff")
    enemy = Character("Robber")

    # while sheriff.has_ended is not True:
    user_input = input("Enter your command: ")
    user_input_list = user_input.split()
    if user_input_list[0] == "Move":
        if sheriff.set_room(user_input_list[3]).room_id == user_input_list[3]:
            new_room()
    if user_input == "Inventory":
        sheriff.display_items()
    if user_input == "List items in Room":
        sheriff.room.display_items()
    if user_input_list[0] == "Pick" and user_input_list[1] == "up" and user_input_list[2] in sheriff.room.items:
        sheriff.add_item(user_input_list[2])
        sheriff.room.remove_item(user_input_list[2])

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
