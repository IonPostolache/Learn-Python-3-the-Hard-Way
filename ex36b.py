from sys import exit

list_wagons=['first_wagon', 'second wagon', 'third wagon', 'fourth wagon', 'fifth wagon']

def start():
    start_position=3
    print(f"You are in the {list_wagons[start_position]} now.")

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
    current_wagonl1=start_position+(move_int*sign)

    if current_wagonl1>4:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif current_wagonl1<0:
        print("Not possible, not enough wagons to do that.")
        print("Choose a different number!")

    elif move_int>=1:
        print(f"You are in the {list_wagons[current_wagonl1]} now.")
        print("Where do you want to go next? 'front' or 'back' ?")


        #startl2()
        start_positionl2=current_wagonl1
        directionl2=input("> ")
        if "back" in directionl2:
            signl2=+1

        elif "front" in directionl2:
            signl2=-1

        else:
            print("You have to choose 'front' or 'back'!")
            exit()

        print("How many wagons do you want to move? ")
        movel2=input(">")
        movel2_int=int(movel2)
        current_wagonl2=start_positionl2+(movel2_int*signl2)

        if current_wagonl2>4:
            print("Not possible, not enough wagons to do that.")
            print("Choose a different number!")

        elif current_wagonl2<0:
            print("Not possible, not enough wagons to do that.")
            print("Choose a different number!")

        elif move_int>=1:
            print(f"You are in the {list_wagons[current_wagonl2]} now.")
            print("Where do you want to go next? 'front' or 'back' ?")


            #startl3()
            start_positionl3=current_wagonl2
            directionl3=input("> ")
            if "back" in directionl3:
                signl3=+1

            elif "front" in directionl3:
                signl3=-1

            else:
                print("You have to choose 'front' or 'back'!")
                exit()

            print("How many wagons do you want to move? ")
            movel3=input(">")
            movel3_int=int(movel3)
            current_wagonl3=start_positionl3+(movel3_int*signl3)

            if current_wagonl3>4:
                print("Not possible, not enough wagons to do that.")
                print("Choose a different number!")

            elif current_wagonl3<0:
                print("Not possible, not enough wagons to do that.")
                print("Choose a different number!")

            elif move_int>=1:
                print(f"You are in the {list_wagons[current_wagonl3]} now.")
                print("Where do you want to go next? 'front' or 'back' ?")



        else:
            print("You have to type a number >0!")
            exit()

    else:
        print("You have to type a number >0!")
        exit()


start()
