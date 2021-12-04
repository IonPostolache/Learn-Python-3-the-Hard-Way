def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for  a party!")
    print("Get a blanket.\n")

#giving the vslues directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#giving the values by using variables
print("OR, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#giving the values of the function as a math inside
print("We can even do the maths inside too:")
cheese_and_crackers(10+20, 5+6)

# giving the values of the functions as a combination of variables and math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
