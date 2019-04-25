from room import Room
from player import Player
from items import Item, Banjo
# Declare all the rooms

room = {
    'bedroom':  Room("Bedroom", "Your room is so awesome! You've got a poster of Earl Scruggs on the wall, YeHaw!"),
    'living_room':    Room("Living Room", """Your living room is know for two things: Grandpa Willy's Banjo and your Dog Yeller's nose shattering farts!"""),
    'kitchen':    Room("Kitchen", """Is mom making her famous chicken for the fair tonight? Smellsssssss D-Licious"""),
    'road': Room("The Road", """It's a long a lonesome Road to the top of Rock and Roll... but should only be 5 minutes to get to town!"""),
    'city_center': Room("City Center", """Look's like they're setting up for the Harvest festival tonight! Should be quite the show :)"""),
    'main_stage':   Room("Main Stage", """The main stage where Banjo legend Earl Scruggs played. Boy... it's a little chilly isn't it?"""),
    'food_stand':   Room("Food Stand", """Your old friend is working the Twinkie stand! Go say hey to your ole pal!"""), 
}
items ={
    'poster': Item("Earl Scruggs Poster", "Your Grandpa Willy gave you this poster for your 5th Birthday. It's a beaut!" ),
    'chicken': Item("Mom's Chicken", "This might be helpful when we're hungry later!" ),
    'banjo': Banjo()
}


# Link rooms together
room['bedroom'].e_to = room["living_room"]
room['bedroom'].w_to = room["kitchen"]
room['bedroom'].add_item(items['poster'])
room['living_room'].add_item(items['banjo'])
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

def change_rooms(player):
    print(player.current_room.name)
    valid_directions = ["n", "w", "s", "e"]
    direction = input(f"You are currently located at {player.current_room.name}. {player.describe_current_room()}. Type n,s,e or w to move North, South, East or West\n")
    if(direction in valid_directions):
        player.change_rooms(direction)
        moved = True
    else:
        moved = False

def show_items(searching, room): 
    room.show_items()
    item = input("Try picking one up! Just type that Items name or type Q to return to the game.")
    if item == 'Q':
        searching = False
    else:
        for i in room.contains:
            if i.name == item:
                player.pick_up(i)
                room.remove_item(i)
                print(f"You've added an {i.name} to your itembag. It's {i.description}")
                searching = False
            else:
                print("Sorry that item doesn't exist. Try searching again")
                searching = False
            
            


# Write a loop that:

while active == True:
    name = input("Howdy there stranger! What's your name?\n")
    if name == 'q':
        print("Thanks for playing!")
        active == False
    # Make a new player object that is currently in the 'outside' room. That's Home in my game
    player = Player(name, room['bedroom'])
    # welcome = input(f"Welcome {player.name}, are you ready to become a Banjo Legend? Press y to continue or n to exit\n")
    # if welcome == 'y':
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    cmd = input(f'{player.name} you are currently located in your {player.current_room.name}. {player.describe_current_room()}\n. If you want to start moving type move or if you want to look around your room type search.')
    if cmd == "move":
        change_rooms(player)
    if cmd == "search":
        searching = True
        show_items(searching, player.current_room)
    # Waits for user input and decides what to do.
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    while moved == False:
        print('Sorry that moves Unavailable please try again. ')
        change_rooms(player)
    print(player.current_room)

    # elif welcome == 'n':
    #     print("Thanks for playing!")
    #     active = False

#
# If the user enters "q", quit the game.