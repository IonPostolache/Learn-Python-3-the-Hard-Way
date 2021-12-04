"""i=0
numbers=[]

d=[1,3,5,7,9,11]"""

def function(d, e):
    numbers=[]
    i=0
    while i<d:
        numbers.append(i)
        i+=e
        print(f"At the top i is {i}")
        print(f"Numbers now: {numbers}")
        print(f"At the bottom i is {i}")
        print("The numbers: ")
        for num in numbers:
            print(num)
"""
    return numbers

    for num in numbers:
        print(num)"""

#nooo=[1,2,3]
function(10, 3)
#print(r)

"""r=list(map(function, nooo))
print(r)

print(f" this is the function: {function}")
print(f" this is the second type of disaplying the function: {r}")"""
