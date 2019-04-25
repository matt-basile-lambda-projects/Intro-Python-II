# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.itembag = []
    def pick_up(self, item):
        self.itembag.append(item)
    # Add a method that will print all the contents the Player contains
    def print_contents(self):
      for i in self.itembag: 
        print(i.name)
    def change_rooms(self, direction):
        if direction in ["n", "s","w","e"]:
            new_room = self.current_room.move_rooms(direction)
            if new_room is not None:
                self.current_room = new_room
                print(f"You've moved to {self.current_room.name}")
                return True
            else: 
                return False
    def describe_current_room(self):
        return self.current_room.describe_room()
    def bio_description(self):
        return f'Name: {self.name}. Items: {self.itembag}, Current Room: {self.current_room}'
    def show_itembag(self):
        for i in self.itembag:
            return i.name
    def remove_item(self,item):
        self.itembag.remove(item)