class Room:
    # Door class to manage doors in a room
    class Door:
        def __init__(self, door_id):
            self.door_id = door_id
            self.is_locked = False

        # Set a door to lock or unlocked (True/False)
        def set_lock_door(self, lock_val):
            self.is_locked = lock_val

    def __init__(self, room_id):
        self.room_id = room_id
        self.items = []
        self.doors = []
        self.number_Visits = 0

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

    # Add a door to a room
    def add_door(self, door):
        self.doors.append(door)

    # Check if there is at least one shared door between the two rooms, and both are unlocked
    def is_connected(self, other_room):
        for door1 in self.doors:
            for door2 in other_room.doors:
                if door1 is door2 and door1.is_locked is False and door2.is_locked is False:
                    return True
        return False
