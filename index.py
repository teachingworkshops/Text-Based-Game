from Character import Character
from Room import Room
from Color import Color

def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    sheriff = Character("Sheriff")
    enemy = Character("Robber")

    sheriff.display_weapons()
    sheriff.display_items()
    

    """while sheriff.has_ended is not True:
        user_input = input("Enter your command: ")
        user_input_list = user_input.split()
        if user_input_list[0] == "Move":
            if sheriff.set_room(user_input_list[3]).room_id == user_input_list[3]:
            #new_room()
        if user_input == "Inventory":
            sheriff.display_items()
        if user_input == "List items in Room":
            sheriff.room.display_items()
        if user_input_list[0] == "Pick" and user_input_list[1] == "up" and user_input_list[2] in sheriff.room.items:
            sheriff.add_item(user_input_list[2])
            sheriff.room.remove_item(user_input_list[2])
        """
    jail_room = Room("Jail")
    jail_room.add_item("Badge")

    sheriff.set_room(jail_room)

    jail_room.display_items()



def main():
    start_game()


if __name__ == "__main__":
    main()
