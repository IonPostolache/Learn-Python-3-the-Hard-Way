the_count=[1,2,3,4,5]
fruits=['apples', 'oranges', 'pears', 'apricots']
change=[1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")


IP_list=[1,3,5]
for d in range(9, 20):
    IP_list.append(d)
    print(f"my list becomes a {d}")


for d in IP_list:
    print(f"my lis becomes: {d}")

list("corona")
print(f"{list}")
