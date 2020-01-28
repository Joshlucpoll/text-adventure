from objects import *
import time

class Manager():

    def __init__(self, health):
        self.current_room = None
        self.health = health
        self.inventory = []
        self.rooms = {}

    def create_room(self, room_name, description):
        self.rooms.update( {str(room_name) : (Room(room_name, description))} )
    
    def create_room_link(self, room_from, room_to, direction):
        if str(room_from) in self.rooms and str(room_to) in self.rooms:
            self.rooms[room_from].link_room(self.rooms[room_to], direction)


    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def set_current_room(self, room_name):
        if room_name in self.rooms:
            self.current_room = self.rooms.get(room_name,"")
    
    def get_current_room(self):
        return self.current_room

    def _help(self):
        print("Commands:")
        print("\t* go          |    move to different room with a direction (go north)")
        print("\t* inspect     |    explore section of room by choosing number (inspect 3)")
        print("\t* take        |    pick up an item you find in the world (take sword)")
        
        input("\nPress ENTER to continue")

    def input_command(self, command):
        self.command = command

        self._commandWord = self.command.split(' ', 1)[0]
        self._command_word_process()

    def _command_word_process(self):
        command = self._commandWord.lower()

        if command == "go":
            self._move_room()
        elif command == "inspect":
            self._s
        elif command == "help":
            self._help()
        else:
            print("Invalid command: \nType 'help' to get a list of possible commands")
            time.sleep(2)

    def _move_room(self):
        direction = (self.command.split(' ' , 1)[1]).lower()
        self.current_room = self.current_room._move(direction)
        
    def _inspect_subroom(self):
        subroom = self.command.split(' ' , 1)[1]