from room import Room
from player import Player
# Declare all the rooms

room = {
    'home':  Room("Your Childhood Home", "The sweet familiar smells and sounds of being home"),
    'living_room':    Room("Living Room", """Your living room is know for two things: Grandpa Willy's Banjo and your Dog Yeller's nose shattering farts!"""),
    'road': Room("The Road", """It's a long a lonesome Road to the top of Rock and Roll... but should only be 5 minutes to get to town!"""),
    'city_center': Room("City Center", """Look's like they're setting up for the Harvest festival tonight! Should be quite the show :)"""),
    'main_stage':   Room("Main Stage", """The main stage where Banjo legend Earl Scruggs played. Boy... it's a little chilly isn't it?"""),
    'food_stand':   Room("Food Stand", """Your old friend is working the Twinkie stand! Go say hey to your ole pal!"""), 
}


# Link rooms together
room['home'].link_rooms("living_room", "s")
room['home'].link_rooms("kitchen", "n")
# room['home'].s_to = room['living_room']
# room['living_room'].n_to = room['road']
# room['living_room'].s_to = room['home']
# room['road'].n_to = room['city_center']
# room['road'].s_to = room['living_room']
# room['city_center'].e_to = room['food_stand']
# room['city_center'].w_to = room['main_stage']
# room['city_center'].s_to = room['road']
# room['main_stage'].e_to = room['city_center']
# room['food_stand'].w_to = room['city_center']

#
# Main
# Constants
active = True
moved = False
# Make a new player object that is currently in the 'outside' room. That's Home in my game
def change_rooms(player):
    direction = input(f"You're currently located at {player.current_room}. {room[player.current_room].__str__()} surround you. Use n,s or e,w to move North, South, East or West\n")
    # print(room[player.current_room].linked_rooms)
    for dics in room[player.current_room].linked_rooms:
        for k,v in dics.items():
            if direction == k: 
                player.change_room(str(v))
                moved = True
            else:
                moved = False
# Write a loop that:

while active == True:
    name = input("Howdy there stranger! What's your name?\n")
    if name == 'q':
        print("Thanks for playing!")
        active == False
    player = Player(name, 'home')
    welcome = input(f"Welcome {player.name}, are you ready to become a Banjo Legend? Press y to continue or n to exit\n")
    if welcome == 'y':
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        change_rooms(player)
        while moved == False:
            print('Sorry that moves Unavailable please try again.')
            change_rooms(player)
        print(player.current_room)

    elif welcome == 'n':
        print("Thanks for playing!")
        active = False
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.