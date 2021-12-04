name='Ion Postolache'
age=36 # not a lie
height=175 # centimeters
weight=83 #kg
eyes='Brown'
teeth='White'
hair='Brown'
#inch_height=(0.393701*height)
inch_height=(0.39*height)
pounds_weight=(2.2*weight)
pounds_weight_round=round(pounds_weight,2)

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"That means in inches {inch_height}")
print(f"He's {weight} kg heavy.")
#print(f"That means in pounds {pounds_weight}.")
print(f"That means in pounds {pounds_weight_round}).")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total=age+height+weight
print(f"If I add {age}, {height} and {weight} I get {total}.")
