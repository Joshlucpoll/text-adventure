from objects import *
import time

class Manager():

    def __init__(self, health, current_room):
        self.current_room = current_room
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def setCurrentRoom(self, current_room):
        self.current_room = current_room
    
    def getCurrentRoom(self):
        return self.current_room

    def _help(self):
        print("Commands:")
        print("\t* go          |    move to different room with a direction (go north)")
        print("\t* inspect     |    explore section of room by choosing number (inspect 3)")
        
        input("\nPress ENTER to continue")

    def inputCommand(self, command):
        self.command = command

        self._commandWord = self.command.split(' ', 1)[0]
        self._commandWordProcess()

    def _commandWordProcess(self):
        command = self._commandWord.lower()

        if command == "go":
            self._moveRoom()
        elif command == "inspect":
            self._inspectSubroom
        elif command == "help":
            self._help()
        else:
            print("Invalid command: \nType 'help' to get a list of possible commands")
            time.sleep(2)

    def _moveRoom(self):
        direction = (self.command.split(' ' , 1)[1]).lower()
        self.current_room = self.current_room._move(direction)
        
    def _inspectSubroom(self):
        subroom = self.command.split(' ' , 1)[1]
        