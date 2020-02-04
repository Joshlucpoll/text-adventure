import time

class Room():
    
    def __init__(self, room_name, description, manager):
        self.name = room_name
        self.description = description
        self.linked_rooms = {}
        self.subrooms = []
        self.mgr = manager
        
        self.mgr.add_room(self, self.name)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def set_subroom(self, subroom_name, subroom_description):
        self.subrooms.append( [subroom_name, Subroom(subroom_name, subroom_description)] )

    def get_details(self):
        #displays current room, description; linked rooms the player can travel to and subrooms inside current room
        print("\n----------------\n" + self.name + "\n----------------")
        print("Description:\n" + self.description + "\n")
        
        if len(self.subrooms) != 0:
            print("\n'Inspect':")
            for i in range(len(self.subrooms)):
                print("(" + str(i+1) + ")  " + self.subrooms[i][0])
            count = 1
        
        print("\n'Go':")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("\t(" + str(direction).capitalize() + ")\t" + room.get_name())
        

class Subroom():
    
    def __init__(self, subroom_name, description):
        self.subroom_name = subroom_name
        self.description = description
    
    def describe(self):
        print("\n" + self.subroom_name + "\n----------------")
        print(self.description)
        print("----------------\n")

class Character():

    def __init__(self, char_name, char_description, manager):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.mgr = manager

        self.mgr.add_character(self, self.name)

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):

    def __init__(self, char_name, char_description, manager):
        super().__init__(char_name, char_description, manager)
        self.weakness = None

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, weakness):
        self.weakness = weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

class Item():
    
    def __init__(self, item_name):
        self.name = name
        self.description = None
    
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, item):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def location(self, room):
        self.location = room