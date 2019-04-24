# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.contains = []
        self.linked_rooms = []
    def __str__(self):
        return self.description
    def link_rooms(self, room_to_link, direction):
        self.linked_rooms.append({direction: room_to_link})
        #print(self.name + ' linked Rooms' + repr(self.linked_rooms))
