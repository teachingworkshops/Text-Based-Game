class Room:

    def __init__(self, room_id):
        self.room_id = room_id
        self.items = []
        self.connection_list = []
        self.has_visited = False

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

    def create_door(self, other_room):
        self.connection_list.append(other_room)

    # Check if there is at least one shared door between the two rooms, and both are unlocked
    def is_connected(self, other_room):
        for connection in self.connection_list:
            if connection == other_room.room_id:
                return True
        return False
