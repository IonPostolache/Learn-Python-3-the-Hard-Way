#The total number of cars
cars=100.0
#Seats in a car except the driver
space_in_a_car=4.0
#How many drivers?
drivers=30.0
#How many passengers today?
passengers=90
#Automatic calculations:
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("There are",cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "people to carpoool today.")
print("We need to put about", average_passengers_per_car, "passengers in each car.")
