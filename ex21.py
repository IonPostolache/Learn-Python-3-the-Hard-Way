def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print(f"DIVIDING {a} \ {b}")
    return a / b

print("Let's do some math with just functions!")

age=add(3, 5)
height=subtract(10, 4)
weight=multiply(9, 2)
iq=divide(12, 6)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the xtra credit, type it in anyway.
print("Here is a puzzle.")

what=add(age, subtract(height, multiply(weight, divide(iq,2))))

what2=age+(height-(weight*(iq/2)))

print("That becomes: ", what, "Can you do it by hand?")
print("That becomes: ", what2, "Can you do it by hand?")
