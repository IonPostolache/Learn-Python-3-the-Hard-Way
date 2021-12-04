from sys import exit

list_wagons=['first_wagon', 'second wagon', 'third wagon', 'fourth wagon', 'fifth wagon']


def go_back():
    print("How many wagons do you want to go to the back? ")
    no_back=input(">")
    back_int=int(no_back)
    current_wagonb1=back_int+3

    if back_int==1:
        print(f"You are in the {list_wagons[current_wagonb1]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")

    elif back_int>1:
        print("Not possible, not enough wagons to do that.")
        print("Choose another number:")
        go_back()

    else:
        exit()



def go_front():
    print("How many wagons do you want to go to the front? ")
    no_front=input(">")
    front_int=int(no_front)
    current_wagonf1=3-front_int

    if front_int==1:
        print(f"You are in the {list_wagons[current_wagonf1]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")

    elif front_int==2:
        print(f"You are in the {list_wagons[current_wagonf1]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")

    elif front_int==3:
        print(f"You are in the {list_wagons[current_wagonf1]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")

    elif front_int>3:
        print("Not possible, not enough wagons to do that.")
        print("Choose another number:")
        go_front()

    else:
        exit()





def start():
    print("""You are in a train and you don't remember
    which wagon you are in and how many wagons are in total.
    The only way to find out is to walk in each of them.
    Which way do you want to go first?
    (you can choose between 'front' or 'back')""")

    direction=input("> ")
    if "back" in direction:
        go_back()


    elif "front" in direction:
        go_front()

    else:
        print("You have to choose 'front' or 'rear'!")
        start()


start()
