from Room import Room
import story


class SceneBuilder:

    # Initialize all the rooms and store them in variables easy to access from elsewhere
    def __init__(self):
        self.jail_room = self.init_jail()
        self.bank_room = self.init_bank()
        self.saloon_room = self.init_saloon()
        self.store = self.init_store()
        self.correct_saloon_guess = False
        self.help_menu_content = story.content["Help"]

    # Each room can have items, doors, and story content. The story content comes from the story file, and the
    # doors should come from the previous room, and another door. This other door connecting to the next step in
    # the game should be added in the scene, so you can't progress until completing the previous room.
    def init_jail(self):
        jail_room = Room("Jail")
        # jail_room.create_door("Bank")
        jail_room.add_item("Revolver")
        jail_room.add_item("Badge")
        jail_room.add_item("Papers")
        jail_room.story_content = story.content["Jail"]
        return jail_room

    def init_bank(self):
        bank_room = Room("Bank")
        bank_room.create_door("Jail")
        # bank_room.create_door("Saloon")
        bank_room.story_content = story.content["Bank"]
        return bank_room

    def init_saloon(self):
        saloon_room = Room("Saloon")
        saloon_room.create_door("Bank")
        # saloon_room.create_door("Store")
        # saloon_room.add_item("Whiskey") DRINKING IS A SIN!
        saloon_room.story_content = story.content["Saloon"]
        return saloon_room

    # TODO: Replace all instances of General Store with Store, should keep to one word
    def init_store(self):
        store_room = Room("Store")
        store_room.create_door("Saloon")
        store_room.story_content = story.content["General Store"]
        return store_room
