import os

import story
from Character import Character
from SceneBuilder import SceneBuilder
from random import randrange
from Color import Color

# DONE: REMOVE DEBUG PRINT STATEMENTS
# DONE: FINISH STORY.PY REQUIRED TEXT
# DONE: CLEAN UP STORY.PY TEXT, FORMAT!!

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


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    # TODO: Replace these prints with JSON
    Color.blue("Welcome to the Wild West adventure!\n")
    Color.green("You are the sheriff in a small town, and trouble is brewing at the bank.\n")

    # Set the first scene
    sheriff.room = jail_room
    jail_scene()

    # Basic gameplay loop
    while sheriff.has_ended is not True:
        command_loop()

    # TODO: Replace end game prints with JSON text
    if sheriff.hasWon is True:
        Color.blue("Congrats, your honor was: {}.".format(sheriff.honor))
        if sheriff.honor >= 60:
            Color.blue("You are the best sheriff there ever was!")
        elif 60 >= sheriff.honor >= 0:
            Color.yellow("You got the job done! that's all that matters")
        elif sheriff.honor < 0:
            Color.red("You got the job done... but at the cost of the respect of the citizens.")
        end_game()
    else:
        Color.red("You have been killed! This town is now a lawless hellscape that no man, woman or child could ever\n"
              "dream of living in. The sheriff was truly an awful justice enforcer")
        Color.red("A dead sheriff doesn't know his honor...")
        end_game()


# The command loop that drives the game. You could call this method in a while loop until an external condition is
# satisfied (game completion, etc.).
def command_loop():
    user_input = input("Enter your command: ")
    # Format so case doesn't matter
    user_input = user_input.lower()
    user_input_list = user_input.split()
    user_input_list = [x.capitalize() for x in user_input_list]
    # A big if statement is the easiest way to implement this. Could be split up into independent functions
    # and called through another method, but this is easier.
    if user_input_list[0] == "Move" and len(user_input_list) > 2 and user_input_list[2] in room_mapping \
            and user_input_list[2] != sheriff.room.room_id:
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
                    Color.red("Congrats, you broke it.")
    elif user_input == "inventory":
        sheriff.display_items()
    elif user_input == "list items in room":
        sheriff.room.display_items()
    elif user_input == "list connections":
        sheriff.room.display_connections()
    elif user_input_list[0] == "Info":
        if user_input_list[1] == "Random-patron":
            if sceneInit.correct_saloon_guess:
                Color.green((story.content["Items"]["correct-patron" + str(randrange(1, 13))]))
            else:
                Color.red((story.content["Items"]["incorrect-patron" + str(randrange(1, 13))]))
            return
        if user_input_list[1] in sheriff.room.items or user_input_list[1] in sheriff.items:
            Color.blue(story.content["Items"][user_input_list[1].lower()])
        else:
            Color.red("\"" + user_input_list[1] + "\" is not a valid item. Check again using \"List items in Room\""
                                              " or \"Inventory\" \nto see the available items.")
    elif user_input_list[0] == "Pick" and user_input_list[1] == "Up":
        if user_input_list[2] in sheriff.room.items:
            return_str = sheriff.add_item(user_input_list[2])
            if return_str == user_input_list[2]:
                sheriff.room.remove_item(user_input_list[2])
                Color.yellow(return_str + " has been picked up!")
            else:
                Color.red("\"" + user_input_list[2] + "\" couldn't be picked up. Check again using \"List items in Room\"")
        else:
            Color.red("\"" + user_input_list[2] + "\" is not a valid item. Check again using \"List items in Room\"")

    elif user_input == "where am i?":
        Color.green("You are in: " + sheriff.room.room_id)
    elif user_input == "help":
        Color.blue(sceneInit.help_menu_content["commands"])
    else:
        Color.red("Invalid command! Please try again")


def jail_scene():
    Color.blue(jail_room.story_content['description'])
    has_finished = False
    # Run the command loop until the sheriff's inventory contains the required items
    while has_finished is not True:
        command_loop()
        if sheriff.items.__contains__("Revolver") and sheriff.items.__contains__("Badge"):
            has_finished = True
            # Only create the door AFTER condition has been met
            jail_room.create_door("Bank")
    sheriff.room.has_visited = True

    clear_terminal()
    Color.red("Cleared Jail!")
    Color.yellow("You can move to the \'Bank\' now. Do this using the command: \"Move to Bank\"")
    return 0


def bank_scene():
    Color.green("\n" + bank_room.story_content['description'])
    Color.yellow("\n" + bank_room.story_content['dialogue'])

    # Run gameplay loop until completion, use has_visited to avoid extra variable.
    while sheriff.room.has_visited is False:
        user_input = input("Do you Fight? Saying no will deescalate (Y/N)").capitalize()
        if user_input == "Y":
            # print("\n" + bank_room.story_content['dialogue_violent'])
            # Starts a battle with poor odds for the sheriff
            if sheriff.battle(enemy, .5, 6) == sheriff:
                Color.red(story.content["Battle"]["bandit-die"])
                sheriff.honor += 100
                sheriff.hasWon = True
                sheriff.has_ended = True
            else:
                Color.red(story.content["Battle"]["ouchie!"])
                sheriff.honor -= 50
                sheriff.experience += 2
            sheriff.room.has_visited = True
        elif user_input == "N":
            # Increase sheriff's honor
            sheriff.honor += 30
            Color.blue("\n" + bank_room.story_content['dialogue_peaceful'])

        bank_room.create_door("Saloon")
        bank_room.add_item("Banker")
        bank_room.add_item("Hostages")
        bank_room.add_item("Wanted-poster")

        Color.yellow("You can move to the \'Saloon\' now. But before you go, take a look around.")

        sheriff.room.has_visited = True


def saloon_scene():
    has_guessed = False
    # You get a shot at guessing after the descriptions are displayed. If you enter a number out of range,
    # the description is displayed again, and you get another chance

    clear_terminal()
    while has_guessed is not True:
        Color.green(saloon_room.story_content['description'])
        Color.yellow(saloon_room.story_content['character1'])
        Color.blue(saloon_room.story_content['character2'])
        Color.green(saloon_room.story_content['character3'])
        Color.yellow(saloon_room.story_content['character4'])
        Color.blue(saloon_room.story_content['character5'])
        Color.green(saloon_room.story_content['character6'])
        Color.yellow(saloon_room.story_content['character7'])
        Color.blue(saloon_room.story_content['character8'])
        print(saloon_room.story_content['prompt'])
        user_input = input()
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == 3:
                Color.green(saloon_room.story_content['correct_guess'])
                has_guessed = True
                sceneInit.correct_saloon_guess = True
                sheriff.honor += 30
                sheriff.experience += 4
                sheriff.add_item("Shotgun")
            elif user_input != 3 and 0 < user_input < 9:
                sheriff.honor -= 30
                sheriff.experience -= 3
                Color.red(saloon_room.story_content['incorrect_guess' + str(user_input)])
                has_guessed = True
            else:
                Color.red("Try that again partner, you didn't enter a number in range")
        else:
            Color.red("You didn't enter a number, try again!")

    sheriff.room.create_door('Store')
    saloon_room.add_item("Random-patron")
    saloon_room.add_item("Bartender")

    sheriff.room.has_visited = True
    if sceneInit.correct_saloon_guess:
        Color.yellow("You can move to the \'Store\' now. \n"
              "But before you go, take a look around.")

    if not sceneInit.correct_saloon_guess:
        Color.green("The bandit escaped!\n"
              "You should investigate the Saloon to see if anyone saw where he went.")


def store_scene():
    clear_terminal()
    Color.green(store_room.story_content['description'])
    user_input = 'PLACEHOLDER'
    while user_input != 'Y':
        user_input = input()
        if user_input != 'Y':
            Color.blue("There's nowhere else to go, you need to enter \'Y\'")

    # If you got a correct guess back at the saloon, increase your likelihood of winning.

    if sheriff.battle(enemy, 1.5, .7) == sheriff:
        Color.blue(story.content["Battle"]["bandit-die"])
        sheriff.hasWon = True
        sheriff.has_ended = True
    else:
        sheriff.has_ended = True

    sheriff.room.has_visited = True


def end_game():
    input("Enter any character to exit: ")


def main():
    start_game()


if __name__ == "__main__":
    main()
