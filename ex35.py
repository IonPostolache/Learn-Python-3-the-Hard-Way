from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice=input("> ")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much<50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("""There si a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?""")
    bear_moved=False

    while True:
        choice=input("> ")

        if choice=="take honey":
            dead("The bear looks at you then slaps your face.")
        elif choice=="taunt bear" and not bear_moved:
            print("THe bear has moved from the door.")
            print("You can go throug it now.")
            bear_moved=True
        elif choice=="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs.")
        elif choice=="open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("""Here you see the great evil cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for yuor life or eat your head? """)

    choice=input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was nasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("""You are in a dark room.
    There is a door to your right and left.
    Which one do you take?""")

    choice=input("> ")

    if choice=="left":
        bear_room()
    elif choice=="right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
