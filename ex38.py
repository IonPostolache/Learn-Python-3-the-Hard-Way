ten_things="Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it")

stuff=ten_things.split(' ')
print(f"this is the list after split: {stuff}")
more_stuff=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    next_one=more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(f"this is the list after pop {stuff}")
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!


list_ip="onions potatoes garlic"
list_s=list_ip.split(' ')
print(f"this is the list after split: {list_s}")

list_pop=list_s.pop()
print(f"this is list after pop: {list_pop}")
