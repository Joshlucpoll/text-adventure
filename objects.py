import time

class Room():
    
    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.linked_rooms = {}
        self.subrooms = []
    
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
        self.subrooms[subroom_name] = Subroom(subroom_name, subroom_description)

    def get_details(self):
        #displays current room, description; linked rooms the player can travel to and subrooms inside current room
        print("\n----------------\n" + self.name + "\n----------------")
        time.sleep(0.5)
        print("Description:\n" + self.description + "\n")
        
        if len(self.subrooms) != 0:
            time.sleep(0.5)
            print("\n'Inspect':")
            count = 1
            for key, value in self.subrooms.items():
                print("(" + str(count) + ")  " + key)
                count += 1
        
        time.sleep(0.5)
        print("\n'Go':")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("\t(" + str(direction).capitalize() + ")\t" + room.get_name())

    def _move(self, direction):
        
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            time.sleep(1)
            return self
    
    def _inspectSubroom(self, sunroom):
        return

class Subroom(Room):

    def __init__(self, room_name, description):
        super().__init__(room_name, description)
        self.linked_subrooms = None
    

class Character():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

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