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
   
    def change_room(self, new_room):
        self.current_room = new_room