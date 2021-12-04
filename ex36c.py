from sys import exit

list_wagons=['first_wagon', 'second wagon', 'third wagon', 'fourth wagon', 'fifth wagon']

i=3

def start():
    for i in list_wagons:
        print(f"You are in the {list_wagons[i]} now.")

    print("""You are in a train and you don't remember
    which wagon you are in and how many wagons are in total.
    The only way to find out is to walk in each of them.
    Which way do you want to go first?
    (you can choose between 'front' or 'back')""")

    direction=input("> ")
    if "back" in direction:
        sign=+1

    elif "front" in direction:
        sign=-1

    else:
        print("You have to choose 'front' or 'back'!")
        exit()

    print("How many wagons do you want to move? ")
    move=input(">")
    move_int=int(move)
    i=i+(move_int*sign)

    if i>4:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif i<0:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif move_int>=1:
        print(f"You are in the {list_wagons[i]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")
        startl2()


    else:
        print("You have to type a number >0!")
        exit()


"""
def startl2():
    #start_position=3
    print(f"You are in the {list_wagons[i]} now.")

    print(""You are in a train and you don't remember
    which wagon you are in and how many wagons are in total.
    The only way to find out is to walk in each of them.
    Which way do you want to go first?
    (you can choose between 'front' or 'back')"")

    direction=input("> ")
    if "back" in direction:
        sign=+1

    elif "front" in direction:
        sign=-1

    else:
        print("You have to choose 'front' or 'back'!")
        exit()

    print("How many wagons do you want to move? ")
    move=input(">")
    move_int=int(move)
    i=i+(move_int*sign)

    if current_wagonl1>4:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif current_wagonl1<0:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif move_int>=1:
        print(f"You are in the {list_wagons[i]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")
        startl2()

    else:
        print("You have to type a number >0!")
        exit()

"""

start()
