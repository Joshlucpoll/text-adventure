from objects import *
import time

class Manager():

    def __init__(self):
        self.current_room = None
        self.current_subroom = None
        self.health = 5#self.set_difficulty()
        self.inventory = []
        self.rooms = {}
        self.characters = {}
        self.enemies = {}

    # health functions
    
    def set_difficulty(self):
        #set up difficult
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

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    # room functions
    
    def add_room(self, room, room_name):
        self.rooms.update({room_name:room})
    
    def get_current_room(self):
        return self.current_room
    
    def set_current_room(self, room):
        if room in self.rooms.values():
            self.current_room = room

    # character functions
    
    def add_character(self, char, char_name):
        if  type(char).__name__ == "Character":
            self.characters.update({char_name:char})
        else:
            self.enemies.update({char_name:char})


    # command functions
    
    def _help(self):
        print("Commands:")
        print("\t* go          |    move to different room with a direction (go north)")
        print("\t* inspect     |    explore section of room by choosing number (inspect 3)")
        print("\t* return      |    go back to the room from inspecting an area (return)")
        print("\t* take        |    pick up an item you find in the world (take sword)")
        
        input("\nPress ENTER to continue")

    def input_command(self, command):
        self.command = command

        self._commandWord = self.command.split(' ', 1)[0]
        self._command_word_process()

    def _command_word_process(self):
        command = self._commandWord.lower()

        if command == "go":
            if self.current_subroom == None:
                self._move_room()
            else:
                print("You must step back into the room.")
        elif command == "inspect":
            self._inspect_subroom()
        elif command == "return":
            if self.current_subroom != None:
                self._return()
            else:
                print("You can't go back at the moment.")
        elif command == "help":
            self._help()
        else:
            print("Invalid command: \nType 'help' to get a list of possible commands")
            time.sleep(1)

    def _move_room(self):
        direction = (self.command.split(' ' , 1)[1]).lower()
        self.current_room = self.current_room._move(direction)
        
    def _inspect_subroom(self):
        subroom = int(self.command.split(' ' , 1)[1].lower()) - 1
        if subroom <= len(self.current_room.subrooms):
            time.sleep(0.5)
            self.current_room.subrooms[subroom][1].describe()
            self.current_subroom = self.current_room.subrooms[subroom][0]
    
    def _return(self):
        print("You step back from the " + self.current_subroom)
        self.current_subroom = None
        time.sleep(0.5)


    def mainloop(self):
        while True:		         
            time.sleep(1)
            if self.current_subroom == None:
                current_room = self.get_current_room()
                current_room.get_details()

            command = input("> ")
            self.input_command(command)

