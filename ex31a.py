print("""You're going into the garden
 to pick something to cook
What vegetable do you pick?
1. Onions.
2. Potatoes.
3. Garlic""")

vegetable=input("> ")

if vegetable=="1":
    print("Great, you picked onions.")
    print("What type of onion did you pick?")
    print("1. Spring onions.")
    print("2. Normal onions.")

    onions=input("> ")

    if onions=="1":
        print("You picked spring onions, so you can make a salad.")
        print("Did you pick only the leaves or entire plant?")
        print("1. Leaves only.")
        print("2. Entire plant.")

        leaves=input("> ")
        if leaves=="1":
            print("Great, so you'll have something left for autumn.")

        else:
            print("So you'll have some white pieces as well.")

    else:
        print("""You picked normal onions,
        so you can make some ceapa prajita cu peste.""")

elif vegetable=="2":
    print("You picked potatoes, so you can make tocanita de cartofi.")

else:
    print("""You picked garlic, so you can
     make some cartofi pai cu mamaliga si usturoi verde""")
