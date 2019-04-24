from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms

items = (
    Item('Sword', 'Your pokey guy'),
    Item('Spatula', 'For making krabby patties'),
    Item('Dice', 'Rolls a number between 1-6'),
    Item('Guitar', 'A mythical creation said to produce musical notes'),
    Item('Gold coin', 'A small circle of gold used as currency'),
    Item('Mouse', 'Sqeaky little guy running around looking for cheese'),
    Item('Key', 'Who know what this could open'),
    Item('Apple juice', 'Old moldy box of apple juice'),
    Item('Pebble', 'Tiny little pebble'),
    Item('Skull', 'Some poor soul from the past'),
    Item('Hat', 'Looks like a wizard hat'),
    Item('Meat', 'Just your run of the mill chunk of meat probably fell off of somethething'),
    Item('Potion', 'Its red who knows what it does'),
    Item('Bug', 'A small black beetle'),
    Item('Water skin', 'A pouch used to carry water'),
    Item('Stick', 'Small crooked looking stick'),
    Item('Cardboard sword', 'Probably not very useful'),
    Item('Cheese', 'A perfect looking wedge of yellow cheese'),
)


def generate_items(num):
    room_items = []
    for i in range(num):
        room_items.append(items[random.randint(0, len(items)-1)])
    return room_items


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", generate_items(3)),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

room['outside'].show_items()

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


def move_direction(current_room, dir):
    attr = dir + '_to'
    if hasattr(current_room, attr):
        player.set_current_room(getattr(current_room, attr))
    else:
        print("Can't go there.")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    print(player.current_room)
    # player.current_room.show_items()
    user_input = input('> ').lower().split()
    if len(user_input) == 1:
        fi = user_input[0][0]
        if fi == 'q':
            break
        elif fi == 'n' or fi == 'e' or fi == 's' or fi == 'w':
            move_direction(player.current_room, fi)
