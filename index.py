import story
from Character import Character
from SceneBuilder import SceneBuilder

# TODO: REMOVE DEBUG PRINT STATEMENTS
# TODO: FINISH STORY.PY REQUIRED TEXT
# TODO: CLEAN UP STORY.PY TEXT, FORMAT!!

# Stretch goal: implement having different weapons

sheriff = Character("Sheriff")
enemy = Character("Robber")

# SceneBuilder creates each room, each room has variables we can access by getting the room from Scenebuilder.
sceneInit = SceneBuilder()
jail_room = sceneInit.jail_room
bank_room = sceneInit.bank_room
saloon_room = sceneInit.saloon_room
store_room = sceneInit.store

# This method makes it easy to have each door connected to room by strings. Each room has a list of room id's (strings)
# it's connected to. We use that as a key to get the actual room using this dictionary

room_mapping = {
    jail_room.room_id: jail_room,
    bank_room.room_id: bank_room,
    saloon_room.room_id: saloon_room,
    store_room.room_id: store_room,
}


def start_game():
    # TODO: Replace these prints with JSON
    print("Welcome to the Wild West adventure!\n")
    print("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    # Set the first scene
    sheriff.room = jail_room
    jail_scene()

    # Basic gameplay loop
    while sheriff.has_ended is not True:
        command_loop()

    # TODO: Replace end game prints with JSON text
    if sheriff.hasWon is True:
        if sheriff.room.room_id == "Bank":
            sheriff.honor = -50
        if "Whiskey" not in saloon_room.items:
            sheriff.honor = -10
        print("CONGRATS, your honor was: {}.".format(sheriff.honor))
    else:
        print("U SUCK!!")


# The command loop that drives the game. You could call this method in a while loop until an external condition is
# satisfied (game completion, etc.).
def command_loop():
    user_input = input("Enter your command: ")
    user_input_list = user_input.split()

    # A big if statement is the easiest way to implement this. Could be split up into independent functions
    # and called through another method, but this is easier.
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
        print(sceneInit.help_menu_content["commands"])
    else:
        print("Invalid command! Please try again")


def jail_scene():
    print(jail_room.story_content['description'])
    has_finished = False
    # Run the command loop until the sheriff's inventory contains the required items
    while has_finished is not True:
        command_loop()
        if sheriff.items.__contains__("Gun") and sheriff.items.__contains__("Badge"):
            has_finished = True
            # Only create the door AFTER condition has been met
            jail_room.create_door("Bank")
    sheriff.room.has_visited = True
    print("You can move to the \'Bank\' now. Do this using the command: \"Move to Bank\"")
    print("DEBUG: END JAIL SCENE")
    return 0


def bank_scene():
    print("DEBUG: START BANK SCENE")

    print("\n" + bank_room.story_content['description'])
    print("\n" + bank_room.story_content['dialogue'])

    # Run gameplay loop until completion, use has_visited to avoid extra variable.
    while sheriff.room.has_visited is False:
        user_input = input("Do you Fight? Saying no will deescalate (Y/N)")
        if user_input == "Y":
            print("\n" + bank_room.story_content['dialogue_violent'])
            # Starts a battle with poor odds for the sheriff
            if sheriff.battle(enemy, .4, 1) == sheriff:
                print("WON HERE")
                sheriff.hasWon = True
                sheriff.has_ended = True
            else:
                print("LOST HERE")
                sheriff.has_ended = True
            sheriff.room.has_visited = True
        elif user_input == "N":
            # Increase sheriff's honor
            sheriff.honor += 30
            print("\n" + bank_room.story_content['dialogue_peaceful'])

            bank_room.create_door("Saloon")

            print("You can move to the \'Saloon\' now.")

            sheriff.room.has_visited = True

    print("DEBUG: END BANK SCENE")


def saloon_scene():
    print("DEBUG: START SALOON SCENE")

    has_guessed = False

    # You get a shot at guessing after the descriptions are displayed. If you enter a number out of range,
    # the description is displayed again, and you get another chance
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
    sheriff.room.create_door('Store')
    sheriff.room.has_visited = True
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

    # If you got a correct guess back at the saloon, increase your likelihood of winning.
    # TODO: Switch this to use experience instead of creating additional modifier variable
    if sceneInit.correct_saloon_guess is True:
        sheriff_modifier += 5

    if sheriff.battle(enemy, sheriff_modifier, 1) == sheriff:
        print("WON HERE")
        sheriff.hasWon = True
        sheriff.has_ended = True
    else:
        print("LOST HERE")
        sheriff.has_ended = True

    sheriff.room.has_visited = True

    print("DEBUG: END STORE SCENE")


def main():
    start_game()


if __name__ == "__main__":
    main()
