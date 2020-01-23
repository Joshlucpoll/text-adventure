from objects import *
from manager import Manager
import time


#set up all object in world

#set up rooms
kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Room", "a room for eating")
ballroom = Room("Ballroom", "a room for dancing")

#setup subrooms
ballroom.set_subroom("Wardrobe", "The wardrobe has many dresses")

#link rooms together
kitchen.link_room(dining_hall, "south")

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

ballroom.link_room(dining_hall, "east")


#create characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Rahh, I what to eat you!")
dave.set_weakness("cheese")

def set_difficulty():
    #set up difficulty and manager
    print("\n\nWelcome to the text adventure game!\nPlease select a difficulty (effects health):\n⁂ Meh!(1)\n⁂ Okay(2)\n⁂ Oh(3)\n⁂ What!?!(4)\n⁂ #!@#?!(5)")

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


mgr = Manager(set_difficulty(), current_room=kitchen)

while True:		         
    time.sleep(1)
    current_room = mgr.getCurrentRoom()       
    current_room.get_details()
    command = input("> ")
    mgr.inputCommand(command)

