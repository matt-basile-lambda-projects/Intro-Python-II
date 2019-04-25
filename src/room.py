# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, name, description, contains=[]):
        self.name = name
        self.description = description
        self.contains = contains
        self.linked_rooms = []
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
    def __str__(self):
        return self.description
    def describe_room(self):
        return f'{self.description}'
    def move_rooms(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def add_item(self,item):
        self.contains.append(item)
    def remove_item(self,item):
        self.contains.remove(item)
    def show_items(self):
        for i in self.contains:
            print(i.name)
    # def link_rooms(self, room_to_link, direction):
    #     self.linked_rooms.append({direction: room_to_link})
    #     #print(self.name + ' linked Rooms' + repr(self.linked_rooms))
