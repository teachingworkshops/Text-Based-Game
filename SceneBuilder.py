from Room import Room


class SceneBuilder:
    def __init__(self):
        self.jail_room = self.init_jail()
        self.bank_room = self.init_bank()

    def init_jail(self):
        jail_room = Room("Jail")
        jail_room.create_door("Bank")
        jail_room.add_item("Gun")
        jail_room.add_item("Badge")
        return jail_room

    def init_bank(self):
        bank_room = Room("Bank")
        bank_room.create_door("Jail")
        bank_room.create_door("Saloon")
        bank_room.add_item("Whiskey")
        return bank_room

    def init_saloon(self):
        saloon_room = Room("Saloon")
        saloon_room.add_door("Bank")
        saloon_room.add_door("Bank")
        saloon_room.add_item("Whiskey")
        return saloon_room

    def init_gs(self):
        gs_room = Room("General Store")
        gs_room
        return gs_room





