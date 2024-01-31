from Character import Character
from Room import Room
from Color import Color
from SceneBuilder import SceneBuilder

sheriff = Character("Sheriff")
enemy = Character("Robber")

sceneInit = SceneBuilder()
jail_room = sceneInit.jail_room
bank_room = sceneInit.bank_room

room_mapping = {
    jail_room.room_id: jail_room,
    bank_room.room_id: bank_room,
}


def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")
    # sheriff.set_room(jail_room)
    sheriff.room = jail_room

    # sheriff = Character("Sheriff")
    # enemy = Character("Robber")

    sheriff.display_weapons()
    sheriff.display_items()
    jail_scene()

    while sheriff.has_ended is not True:
        command_loop()

    if sheriff.hasWon is True:
        print("CONGRATS")
    else:
        print("U SUCK!!")


def command_loop():
    user_input = input("Enter your command: ")
    user_input_list = user_input.split()
    print("SETJIOSFJODIJSIOFJENSEIFJIOFES")
    if user_input_list[0] == "Move":
        if sheriff.set_room(room_mapping[user_input_list[2]]) == user_input_list[2]:
            if sheriff.room.has_visited is False:
                if sheriff.room.room_id == "Jail":
                    jail_scene()
                elif sheriff.room.room_id == "Bank":
                    bank_scene()
    if user_input == "Inventory":
        sheriff.display_items()
    if user_input == "List items in Room":
        print("ESTSTSSETSETESTETTEESTESETESTSTEST")
        sheriff.room.display_items()
    if user_input_list[0] == "Pick" and user_input_list[1] == "up" and user_input_list[2] in sheriff.room.items:
        return_str = sheriff.add_item(user_input_list[2])
        print(return_str + " has been picked up!")
        sheriff.room.remove_item(user_input_list[2])


def jail_scene():
    print("DEBUG: START JAIL SCENE")
    # DIALOGUE
    has_finished = False
    while has_finished is not True:
        command_loop()
        if sheriff.items.__contains__("Gun") and sheriff.items.__contains__("Badge"):
            has_finished = True
    sheriff.room.has_visited = True
    print("DEBUG: END JAIL SCENE")
    return 0


def bank_scene():
    # DIALOGUE
    print("DEBUG: START BANK SCENE")
    while sheriff.room.has_visited is False:
        user_input = input("Do you Fight? Saying no will deescalate (Y/N)")
        if user_input == "Y":
            # winning_character = sheriff.battle(enemy)
            if sheriff.battle(enemy) == sheriff:
                print("WON HERE")
                sheriff.hasWon = True
                sheriff.has_ended = True
            else:
                print("LOST HERE")
                sheriff.has_ended = True
            sheriff.room.has_visited = True
        elif user_input == "N":
            # Dialogue
            sheriff.room.has_visited = True
    print("DEBUG: END BANK SCENE")



def saloon_scene():
    return 0


def main():
    start_game()


if __name__ == "__main__":
    main()
