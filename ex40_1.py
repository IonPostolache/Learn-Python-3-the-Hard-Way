class Robot:
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce_self(self):
        print("My name is " + self.name)
        print("My eyes are " + self.color)
        print(f"My weight is ")
        print(self.weight)



r1=Robot("Tom", "red", 30)
r2=Robot("Jerry", "blue", 40)
r3=Robot("Alladin", "green", 50)
#r1.name="Tom"
#r1.color="red"
#r1.weight=30

r1.introduce_self()
r2.introduce_self()
r3.introduce_self()
