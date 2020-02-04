from objects import Room, Character, Enemy, Item
from manager import Manager
import time


#set up manager 
mgr = Manager()


kitchen = Room("Kitchen", "A dank and dirty room buzzing with flies.", mgr)
dining_room = Room("Dining Room", "a room for eating", mgr)
ballroom = Room("Ballroom", "a room for dancing", mgr)

kitchen.link_room(dining_room, "south")

dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")

ballroom.link_room(dining_room, "east")

mgr.set_current_room(kitchen)

#create characters
dave = Enemy("Dave", "A smelly zombie", mgr)
dave.set_conversation("Rahh, I what to eat you!")
dave.set_weakness("cheese")

mgr.mainloop()


