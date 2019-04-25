from room import Room
from player import Player
from items import Item, Banjo
# Declare all the rooms

room = {
    'bedroom':  Room("Bedroom", "Your room is so awesome! You've got a poster of Earl Scruggs on the wall, YeHaw!"),
    'living_room':    Room("Living Room", "Your living room is know for two things: Grandpa Willy's Banjo and your Dog Yeller's nose shattering farts!"),
    'kitchen':    Room("Kitchen", "Is mom making her famous chicken for the fair tonight? Smellsssssss D-Licious"),
    'road': Room("The Road", "It's a long a lonesome Road to the top of Rock and Roll... but should only be 5 minutes to get to town!"),
    'city_center': Room("City Center", "Look's like they're setting up for the Harvest festival tonight! Should be quite the show :)"),
    'main_stage':   Room("Main Stage", "The main stage where Banjo legend Earl Scruggs played. Boy... it's a little chilly isn't it?"),
    'food_stand':   Room("Food Stand", "Your old friend is working the Twinkie stand! Go say hey to your ole pal!"), 
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
    valid_directions = ["n", "w", "s", "e"]
    direction = input(f"You are currently located at {player.current_room.name}. {player.describe_current_room()}. Type n,s,e or w to move North, South, East or West\n")
    if(direction in valid_directions):
        new = player.change_rooms(direction)
        if new == False:
            print(f'Sorry the direction is unavailable please try again. ')
            change_rooms(player)
        elif new == True:
            moved = True
        else:
            print(f'Sorry the direction is unavailable please try again. ')
            change_rooms(player)
    else:
        print(f'Sorry the direction is unavailable please try again. ')
        change_rooms(player)

def show_items(searching, room): 
    room.show_items()
    item = input("Try looking or picking an item up! Just type that view object or pickup object name or type q to return to the game.")
    if item == 'q':
        searching = False
        return searching
    else:
        search = item.split(' ')
        if(search[0] == "view"):
            for i in room.contains:
                if i.name == search[1]:
                    print(f"Name:{i.name}, Description: {i.description}")
                    searching = True
                    return searching
        elif(search[0] == "pickup"):
            for i in room.contains:
                if i.name.upper() == search[1].upper():
                    player.pick_up(i)
                    room.remove_item(i)
                    print(f"You've added an {i.name} to your itembag. It's {i.description}")
                    searching = False
                    return searching
        else:
            print("Sorry that item doesn't exist. Try searching again")
            searching = False
            return searching
            
player = None
while active == True:
    if player == None: 
        print("Welcome to Banjo Quest Let's Start your journey!")
        cmd = input("Type one of these Commands: Bio | Quit\n")
        if cmd == "Quit":
            active = False
        elif cmd == "Bio":
            if player is not None:
                print(player.bio_description())
            else:
                name = input("Your Bio is empty! Let's create it! Please enter your name: \n")
                player = Player(name, room['bedroom'])  
    else:
        cmd = input("Type one of these Commands: Bio | Action | Items | Quit\n")
        if cmd == "Quit":
            active = False
        elif cmd == "Bio":
            if player is not None:
                print(player.bio_description())
            else:
                name = input("Your Bio is empty! Let's create it! Please enter your name: \n")
                player = Player(name, room['bedroom'])  
        elif cmd == "Action":
            action = input("Type one of these Actions: Move | Search | Quit")
            if action == "Quit":
                break
            elif action == "Move":
                change_rooms(player)
            elif action == "Search":
                searching = True
                while searching == True:
                    searching = show_items(searching, player.current_room)
        elif cmd == "Items":
            parsing = True
            while parsing == True: 
                new_items = player.show_itembag()
                if len(items) == 0:
                    new_items = 0
                item = input(f"Here are your current Items: {new_items}. Type one out to learn more about it or q to quit.")
                if item == "q":
                    parsing = False
                else:
                    for i in player.itembag:
                        if i.name == item:
                            print(f"Item: {i.name}, Description: {i.description}, Methods: {i}")
            
