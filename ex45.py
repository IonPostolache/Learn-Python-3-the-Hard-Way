from sys import exit
from random import randint
from textwrap import dedent
from ex45virus import Virus

gas_guess=randint(0, 1)
temp_guess=randint(2, 3)


class Ship(object):

    def enter(self):
        print("This ship is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__ (self, ship_map):
        self.ship_map=ship_map

    def play(self):
        current_ship=self.ship_map.opening_ship()
        last_ship=self.ship_map.next_ship('samples_room')

        while current_ship!=last_ship:
            next_ship_name=current_ship.enter()
            current_ship=self.ship_map.next_ship(next_ship_name)

        current_ship.enter()

class Death(Ship):

    def enter(self):
        print("The virus woke up and killed you.")
        print("It's over now.")
        exit(1)

class CentralCommandRoom(Ship):

    if gas_guess==0:
        gas_guess1='Oxygen'
    elif gas_guess==1:
        gas_guess1='Hydrogen'
    else:
        print("Not possible.")

    if temp_guess==2:
        temp_guess1='warm'
    elif temp_guess==3:
        temp_guess1='cold'
    else:
        print("Not possible.")

    oc=Virus(gas_guess1, temp_guess1)
    oc.virus_needs()


    def enter(self):
        print(dedent("""
            But let's suppose you don't know anything about the virus.
            You are in the Central Command Room now.
            You've just picked a virus sample from the Mars soil.
            """))
        print("Where do you want to go next?")

        action=input("> ")

        if action=="bedroom":
            return 'bedroom'

        elif action=="lab":
            return 'lab_room'

        elif action=="food_room":
            return 'food_room'

        elif action=="samples_room":
            return 'samples_room'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_command_room'

class LabRoom(Ship):

    def enter(self):
        print(dedent("""
            You are in the Lab Room now.
            """))

        if gas_guess==1 and temp_guess==3:
            print("Because of the Hydrogen and cold temperature,")
            return 'death'

        else:
            print(dedent("""
                Where do you want to go next?
                """))

            action=input("> ")

            if action=="central_command_room":
                return 'central_command_room'

            elif action=="food_room":
                return 'food_room'

            elif action=="bedroom":
                return 'bedroom'

            elif action=="lab":
                return 'lab_room'

            elif action=="samples_room":
                return 'samples_room'

            else:
                print("DOES NOT COMPUTE!")
                return "lab_room"

class Bedroom(Ship):

    def enter(self):
        print(dedent("""
            You are in the Bedroom now.
            """))

        if gas_guess==0 and temp_guess==2:
            print("Because of the Oxygen and warm temperature,")
            return 'death'

        else:
            print(dedent("""
                Where do you want to go next?
                """))

            action=input("> ")

            if action==" central_command_room":
                return 'central_command_room'

            elif action=="food_room":
                return 'food_room'

            elif action=="bedroom":
                return 'bedroom'

            elif action=="lab":
                return 'lab_room'

            elif action=="samples_room":
                return 'samples_room'

            else:
                print("DOES NOT COMPUTE!")
                return "bedroom"

class FoodRoom(Ship):

    def enter(self):
        print(dedent("""
            You are in the Food Room now.
            """))

        if gas_guess==0 and temp_guess==2:
            print("Because of the Oxygen and warm temperature,")
            return 'death'

        else:
            print(dedent("""
                Where do you want to go next?
                """))

            action=input("> ")

            if action==" central_command_room":
                return 'central_command_room'

            elif action=="food_room":
                return 'food_room'

            elif action=="bedroom":
                return 'bedroom'

            elif action=="lab":
                return 'lab_room'

            elif action=="samples_room":
                return 'samples_room'

            else:
                print("DOES NOT COMPUTE!")
                return "food_room"


class SamplesRoom(Ship):

    def enter(self):
        print("The virus samples are safe now. You won!. Good job!")
        return 'samples_room'

class Map(object):

    ships= {
        'central_command_room': CentralCommandRoom(),
        'lab_room': LabRoom(),
        'bedroom': Bedroom(),
        'food_room': FoodRoom(),
        'death': Death(),
        'samples_room': SamplesRoom(),
    }

    def __init__(self, start_ship):
        self.start_ship=start_ship

    def next_ship(self, ship_name):
        val=Map.ships.get(ship_name)
        return val

    def opening_ship(self):
        return self.next_ship(self.start_ship)

a_map=Map('central_command_room')
a_game=Engine(a_map)
a_game.play()
