import time

class Room():
    
    mgr = None

    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.linked_rooms = {}
        self.subrooms = {}

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
        self.linked_rooms.update( {direction : room_to_link} )

    def set_subroom(self, subroom_name, subroom_description):
        self.subrooms.update({subroom_name : Subroom(subroom_name, subroom_description)})

    def get_details(self):
        #displays current room, description; linked rooms the player can travel to and subrooms inside current room
        print("\n----------------\n" + self.name + "\n----------------")
        print("Description:\n" + self.description + "\n")
        
        if len(self.subrooms) != 0:
            print("\n'Inspect':")
            
            count = 1
            for key, value in self.subrooms.items():
                print("(" + str(count) + ")  " + str(key))
                count += 1
        
        print("\n'Go':")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("\t(" + str(direction).capitalize() + ")\t" + room.get_name())

    def _move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            return self
        

class Subroom():
    
    def __init__(self, subroom_name, description):
        self.subroom_name = subroom_name
        self.description = description
    
    def describe(self):
        print("\n" + self.subroom_name + "\n----------------")
        print(self.description)
        print("----------------\n")

    def get_name(self):
        return self.subroom_name
class Character():

    mgr = None

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

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

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
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
    
    mgr = None

    def __init__(self, item_name, location, item_description):
        self.name = item_name
        self.description = item_description
        self.location = location
    
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, item):
        self.description = item_description

    def get_description(self):
        return self.description

    def location(self, room):
        self.location = room
    
    def get_location(self):
        return self.location

    def describe(self):
        print(self.description)

class Health_potion(Item):

    default_des = "Use it to restore your health."

    def __init__(self, item_name, location, item_description=None):
        if item_description == None:
            item_description = self.default_des
        super().__init__(item_name, location, item_description)

        self.health = 0

    def set_health(self, heath):
        self.health = health
    
    def get_health(self):
        return self.health