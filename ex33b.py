i=0
numbers=[]
"""
while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i=i+1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)"""


#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    numbers.append(i)
    """i=i+1
    #or
    i +=1
    #not needed anymore, because we have append()"""
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")
for num in numbers:
    print(num)
