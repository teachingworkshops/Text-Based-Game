class Player:
    def __init__(self):
        self.weapon = "None"
        self.health = 100
        self.experience = 0
        self.points = 0
        self.weapons = {
            "Pistol": {"damage": 5, "accuracy": 40, "xp_needed": 0},
            "Shotgun": {"damage": 20, "accuracy": 60, "xp_needed": 30},
            "Rifle": {"damage": 30, "accuracy": 70, "xp_needed": 50}
        }

    # changes the player's weapon. Example: sheriff.set_weapon("Pistol")
    def set_weapon(self, weapon_name):
        self.weapon = weapon_name

    # Subtracts user's health
    # If you need to add health -damage_taken
    def update_health(self, damage_taken):
        self.health -= damage_taken
        if self.health <= 0:
            self.health = 0

    # Ads exp
    def gain_experience(self, exp):
        self.experience += exp

    # Prints out all weapons in the game
    def display_weapons(self):
        print("\033[1mWeapon: \033[0m")

        for weapon_name in self.weapons:
            weapon = self.weapons[weapon_name]
            print(f"{weapon_name}: Damage: {weapon['damage']}, Accuracy: {weapon['accuracy']}, Experience needed: {weapon['xp_needed']}")
        print("\n")

    # prints user's stats
    def display_stats(self):
        print("\033[1mStats: \033[0m")
        print("Weapon: " + self.weapon )
        print("Health: {}".format(self.health))
        print("Experience: {}".format(self.experience))
        print("Points: {}".format(self.points))
        print("\n")