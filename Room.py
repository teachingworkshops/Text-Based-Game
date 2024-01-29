class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.items = []

    # Add an item to the room
    def add_item(self, item):
        self.items.append(item)

    # Remove an item from the room
    def remove_item(self, item):
        self.items.remove(item)

    # Print all items in the room
    def display_items(self):
        for item in self.items:
            print(item + " is in \'" + self.room_id + "\'")
