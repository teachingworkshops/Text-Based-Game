import story
from Room import Room
import random
from Color import Color
from time import sleep

class Character:

    # has_ended should really not live here but screw it, hasWon makes sense though
    def __init__(self, name):
        self.has_ended = 0
        self.name = name
        self.weapon = "None"
        self.health = 20
        self.experience = 0
        self.honor = 0
        self.room = Room("Jail")
        self.items = []
        self.hasWon = 0
        self.weapons = {
            "Pistol": {"damage": 5, "accuracy": 40, "xp_needed": 0},
            "Shotgun": {"damage": 20, "accuracy": 60, "xp_needed": 30},
            "Rifle": {"damage": 30, "accuracy": 70, "xp_needed": 50}
        }

    # changes the player's weapon. Example: sheriff.set_weapon("Pistol")
    def set_weapon(self, weapon_name):
        self.weapon = weapon_name

    # Changes the player's room. If an invalid argument is passed it keeps the player in the old room
    def set_room(self, new_room):
        # if isinstance(new_room, Room) and (self.room.is_connected(new_room)):
        if self.room.is_connected(new_room):
            self.room = new_room
        else:
            print("Invalid room, keeping the player in: " + self.room.room_id)
        return self.room.room_id

    # Subtracts user's health
    # If you need to add health -damage_taken
    def update_health(self, damage_taken):
        self.health -= damage_taken
        if self.health <= 0:
            self.health = 0

    # Adds or subtracts exp
    def update_experience(self, exp):
        self.experience += exp

    # Adds or subtracts points
    def update_points(self, points):
        self.points += points

    # Prints out all weapons in the game
    def display_weapons(self):
        Color.green("Weapon:")
        Color.yellow("y")
        Color.red("r")
        Color.blue("b")

        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            print(
                f"{weapon_name}: Damage: {weapon['damage']}, Accuracy: {weapon['accuracy']}, "
                f"Experience needed: {weapon['xp_needed']}")
        print("\n")

    # Add an item to the player's item list
    def add_item(self, item):
        self.items.append(item)
        if self.items[-1] == item:
            return item
        else:
            return "Nothing"

    # Remove an item from the player's item list
    def remove_item(self, item):
        self.items.remove(item)

    # Print all items in the player's item list
    def display_items(self):
        for item in self.items:
            print(item + " is in your inventory")

    # Gets the winner of a fight and returns that Character
    # TODO: ADD DEPTH AND MAKE IT A LITTLE COOLER, MAYBE WEAPON VARIETY FROM CHASE?
    def battle(self, other_character, self_modifier=1, enemy_modifier=1, is_final=False):
        while self.health > 0 and other_character.health > 0:
            enemy_val = (random.randint(1, 10) + self.experience) * enemy_modifier
            self_val = (random.randint(1, 10) + self.experience) * self_modifier
            if enemy_val > self_val:
                self.health -= enemy_val
            else:
                other_character.health -= self_val
        print(story.content["Battle"]["standoff"])
        # DRAMATIC STAND OFF   .   .   .
        sleep(7)
        print("\n  .  ")
        sleep(1)
        print("  .  ")
        sleep(1)
        print("  .  \n")
        sleep(1)
        print("BANG!!!\n")
        sleep(3)
        # Returns the winning character
        if self.health > 0 >= other_character.health or self.health == other_character.health:
            return self
        elif self.health <= 0 < other_character.health:
            return other_character

    # prints user's stats
    def display_stats(self):
        print("\033[1mStats: \033[0m")
        print("Weapon: " + self.weapon)
        print("Health: {}".format(self.health))
        print("Experience: {}".format(self.experience))
        print("Points: {}".format(self.points))
        print("\n")
