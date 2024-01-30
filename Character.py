from Room import Room
import random


class Character:
    def __init__(self, name):
        self.name = name
        self.weapon = "None"
        self.health = 100
        self.experience = 0
        self.points = 0
        self.room = Room("Jail")
        self.items = []
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
        if isinstance(new_room, Room) and (self.room.is_connected(new_room)):
            self.room = new_room
        else:
            print("Invalid room, keeping the player in: " + self.room.room_id)
        return self.room

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
        print("\033[1mWeapon: \033[0m")

        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            print(
                f"{weapon_name}: Damage: {weapon['damage']}, Accuracy: {weapon['accuracy']}, "
                f"Experience needed: {weapon['xp_needed']}")
        print("\n")

    # Add an item to the player's item list
    def add_item(self, item):
        self.items.append(item)

    # Remove an item from the player's item list
    def remove_item(self, item):
        self.items.remove(item)

    # Print all items in the player's item list
    def display_items(self):
        for item in self.items:
            print(item + " is in your inventory")

    # Gets the winner of a fight and returns that Character
    def battle(self, other_character, self_modifier, enemy_modifier):
        # if(self.room.room_id ==)
        enemy_val = (random.randint(1, 10) + self.experience) * enemy_modifier
        self_val = (random.randint(1, 10) + self.experience) * self_modifier
        if enemy_val > self_val:
            return other_character
        else:
            return self

    # prints user's stats
    def display_stats(self):
        print("\033[1mStats: \033[0m")
        print("Weapon: " + self.weapon)
        print("Health: {}".format(self.health))
        print("Experience: {}".format(self.experience))
        print("Points: {}".format(self.points))
        print("\n")
