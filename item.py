from story import content
import Room


# NOTE: Items are currently being stored as strings, nothing more. This would provide more depth and allow for some cool
# things if time permits

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
