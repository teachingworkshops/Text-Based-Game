import story
from Character import Character
from SceneBuilder import SceneBuilder

sheriff = Character("Sheriff")
enemy = Character("Robber")

sceneInit = SceneBuilder()
jail_room = sceneInit.jail_room
bank_room = sceneInit.bank_room
saloon_room = sceneInit.saloon_room
store_room = sceneInit.store

room_mapping = {
    jail_room.room_id: jail_room,
    bank_room.room_id: bank_room,
    saloon_room.room_id: saloon_room,
    store_room.room_id: store_room,
}


def start_game():
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    sheriff.room = jail_room

    jail_scene()

    while sheriff.has_ended is not True:
        command_loop()

    if sheriff.hasWon is True:
        if sheriff.room.room_id == "Bank":
            sheriff.honor = -50
        if "Whiskey" not in saloon_room.items:
            sheriff.honor = -10
        print("CONGRATS, your honor was: {}.".format(sheriff.honor))
    else:
        print("U SUCK!!")


def command_loop():
    user_input = input("Enter your command: ")
    user_input_list = user_input.split()
    if user_input_list[0] == "Move" and len(user_input_list) > 2 and user_input_list[2] in room_mapping:
        if sheriff.set_room(room_mapping[user_input_list[2]]) == user_input_list[2]:
            print("You are now in: " + sheriff.room.room_id)
            if sheriff.room.has_visited is False:
                if sheriff.room.room_id == "Jail":
                    jail_scene()
                elif sheriff.room.room_id == "Bank":
                    bank_scene()
                elif sheriff.room.room_id == "Saloon":
                    saloon_scene()
                elif sheriff.room.room_id == "Store":
                    store_scene()
                else:
                    print("Congrats, you broke it.")
    elif user_input == "Inventory":
        sheriff.display_items()
    elif user_input == "List items in Room":
        sheriff.room.display_items()
    elif user_input == "List connections":
        sheriff.room.display_connections()
    elif user_input_list[0] == "Pick" and user_input_list[1] == "up":
        return_str = sheriff.add_item(user_input_list[2])
        if return_str == user_input_list[2]:
            sheriff.room.remove_item(user_input_list[2])
            print(return_str + " has been picked up!")
        else:
            print("\"" + user_input_list[2] + "\" couldn't be picked up. Check again using \"List items in Room\"")
    elif user_input == "Where am I?":
        print("You are in: " + sheriff.room.room_id)
    elif user_input == "Help":
        print(story)
    else:
        print("Invalid command! Please try again")


def jail_scene():
    print(jail_room.story_content['description'])
    # DIALOGUE
    has_finished = False
    while has_finished is not True:
        command_loop()
        if sheriff.items.__contains__("Gun") and sheriff.items.__contains__("Badge"):
            has_finished = True
            jail_room.create_door("Bank")
    sheriff.room.has_visited = True
    print("You can move to the \'Bank\' now. Do this using the command: \"Move to Bank\"")
    print("DEBUG: END JAIL SCENE")
    return 0


def bank_scene():
    print("\n" + bank_room.story_content['description'])
    print("\n" + bank_room.story_content['dialogue'])
    # DIALOGUE
    print("DEBUG: START BANK SCENE")
    while sheriff.room.has_visited is False:
        user_input = input("Do you Fight? Saying no will deescalate (Y/N)")
        if user_input == "Y":
            print("\n" + bank_room.story_content['dialogue_violent'])
            if sheriff.battle(enemy, .4, 1) == sheriff:
                print("WON HERE")
                sheriff.hasWon = True
                sheriff.has_ended = True
            else:
                print("LOST HERE")
                sheriff.has_ended = True
            sheriff.room.has_visited = True
        elif user_input == "N":
            # Dialogue
            sheriff.honor += 30
            print("\n" + bank_room.story_content['dialogue_peaceful'])
            sheriff.room.create_door(saloon_room)
            print("You can move to the \'Saloon\' now.")
            sheriff.room.has_visited = True
    print("DEBUG: END BANK SCENE")


def saloon_scene():
    print("DEBUG: START SALOON SCENE")
    has_guessed = False
    while has_guessed is not True:
        print(saloon_room.story_content['description'])
        user_input = int(input())
        if user_input == 3:
            print(saloon_room.story_content['correct_guess'])
            has_guessed = True
            sceneInit.correct_saloon_guess = True
        elif user_input != 3 and 0 < user_input < 9:
            print(saloon_room.story_content['incorrect_guess'])
            has_guessed = True
        else:
            print("Try that again partner, you didn't enter a number in range")
    sheriff.room.create_door(store_room)
    print("You can move to the \'Store\' now.")
    print("DEBUG: END SALOON SCENE")


def store_scene():
    print("DEBUG: START STORE SCENE")
    print(store_room.story_content['description'])
    user_input = 'PLACEHOLDER'
    sheriff_modifier = 2
    while user_input != 'Y':
        user_input = input()
        if user_input != 'Y':
            print("There's nowhere else to go, you need to enter \'Y\'")

    if sceneInit.correct_saloon_guess is True:
        sheriff_modifier += 5

    if sheriff.battle(enemy, sheriff_modifier, 1) == sheriff:
        print("WON HERE")
        sheriff.hasWon = True
        sheriff.has_ended = True
    else:
        print("LOST HERE")
        sheriff.has_ended = True

    print("DEBUG: END STORE SCENE")


def main():
    start_game()


if __name__ == "__main__":
    main()
