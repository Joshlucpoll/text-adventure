from objects import *
from manager import Manager
import time


def set_difficulty():
    #set up difficulty and manager
    print("\n\nWelcome to the text adventure game!\nPlease select a difficulty (effects health):\n⁂ Meh!(1)\n⁂ Okay(2)\n⁂ Oh(3)\n⁂ What!?!(4)\n⁂ #!@#?!(5)")

    #select difficulty
    while True:
        try:
            difficulty = int(input())
            if difficulty > 0 and difficulty < 6:
                break
            else:
                print("Please select a number between 1-5")
        except (RuntimeError, TypeError, NameError, ValueError):
                print("Please select a number between 1-5")

    if difficulty == 1:
        health = 5
        print("Difficulty set to Meh!")
    if difficulty == 2:
        health = 4
        print("Difficulty set to Okay")
    if difficulty == 3:
        health = 3
        print("Difficulty set to Oh")
    if difficulty == 4:
        health = 2
        print("Difficulty set to What!?!")
    if difficulty == 5:
        health = 1
        print("Difficulty set to #!@#?!")

    time.sleep(1)
    print("\nCurrent health: " + str(health))
    return health

#set up manager 
mgr = Manager(set_difficulty())

mgr.create_room("Kitchen", "A dank and dirty room buzzing with flies.")
mgr.create_room("Dining Room", "a room for eating")
mgr.create_room("Ballroom", "a room for dancing")


mgr.create_room_link("Kitchen", "Dining Room", "south")

mgr.create_room_link("Dining Room", "Kitchen", "north")
mgr.create_room_link("Dining Room", "Ballroom", "west")

mgr.create_room_link("Ballroom", "Dining Room", "east")


mgr.set_current_room("Kitchen")


while True:		         
    time.sleep(1)
    current_room = mgr.get_current_room()       
    current_room.get_details()
    command = input("> ")
    mgr.input_command(command)

