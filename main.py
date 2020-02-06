from objects import Room, Character, Enemy, Item, Health_potion
from manager import Manager
import time


#set up manager 
mgr = Manager()

#set up rooms
kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.")
dining_room = Room("Dining Room", "a room for eating")
ballroom = Room("Ballroom", "a room for dancing")

kitchen.link_room(dining_room, "south")

dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")

ballroom.link_room(dining_room, "east")

kitchen.set_subroom("Stove", "There is an old saucepan on the hob, it's greasy")

mgr.set_current_room(kitchen)


#create characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Rahh, I what to eat you!")
dave.set_weakness("cheese")

potion = Health_potion("potion", kitchen.subrooms.get("Stove"), "description")

mgr.mainloop()