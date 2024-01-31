import story
from Room import Room


class SceneBuilder:
    def __init__(self):
        self.correct_saloon_guess = False
        self.help_menu_content = story.content["Help"]
        self.jail_room = self.init_jail()
        self.bank_room = self.init_bank()
        self.saloon_room = self.init_saloon()
        self.store = self.init_store()

    def init_jail(self):
        jail_room = Room("Jail")
        # jail_room.create_door("Bank")
        jail_room.add_item("Gun")
        jail_room.add_item("Badge")
        jail_room.story_content = story.content["Jail"]
        return jail_room

    def init_bank(self):
        bank_room = Room("Bank")
        bank_room.create_door("Jail")
        bank_room.create_door("Saloon")
        bank_room.add_item("Whiskey")
        bank_room.story_content = story.content["Bank"]
        return bank_room

    def init_saloon(self):
        saloon_room = Room("Saloon")
        saloon_room.create_door("Bank")
        saloon_room.create_door("Store")
        saloon_room.add_item("Whiskey")
        saloon_room.story_content = story.content["Saloon"]
        return saloon_room

    def init_store(self):
        gs_room = Room("Store")
        gs_room.create_door("Saloon")
        gs_room.story_content = story.content["General Store"]
        return gs_room





