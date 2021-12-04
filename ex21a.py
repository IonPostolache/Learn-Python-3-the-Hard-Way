formula=24+34/100-1023
print(formula)

def add(a, b):
    print(f"adding {a} +{b}")
    return a+b

def subt(a, b):
    print(f"subtrac {a} - {b}")
    return a-b

def div(a, b):
    print(f"divide {a} / {b}")
    return a / b


print("This is after defining the functions.")
print("Now we'll start calling the functions.\n")

apple=add(20, 4)
pear=subt(3069, 1023)
grape=div(3400, 100)

print("Now we'll start calculating the result using functions:\n")

#result=add(apple, div(grape, subt(pear,1023)))
result2=add(apple, subt(div(grape, 100), 1023))

#print("The result calculated by using functions is: ", result, "correct?")
print("The result calculated by using functions is: ", result2, "correct?")
