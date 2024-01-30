from story import content
import Room

class item:
    def __init__(self, name, location: Room):
        self.name = name
        self.description = content[name]
        self.location = location
        self.picked_up = False
        self.pickupable = True

    def info_item(self) -> str:
        return self.description

    def item_name(self) -> str:
        return self.name
