''' Practice using if, elif and else statements in Python. 
Date: 2024-06-01
Author: Kevin'''


water_lever = 50
if water_lever > 80:
    print("Drain Water")
elif water_lever < 20:
    print("Add Water")
else:
    print("Water level is good")
# Output: Water level is good

print("welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:    
    print("Sorry, you have to grow taller before you can ride.")
# Output: You can ride the rollercoaster! (if height is 120 or more)

print ("Welcome to the rollercoaster!")

number_to_check = int(input("Enter Number: "))
print(number_to_check % 2)



# Nested : if conition: if anoter condition: do this else: do this else: do this

print("Test of nested")

height = int(input("Enter height: "))

if height >= 120:
    print("You can ride the rollercoaster")

age = int(input("What is your age: "))
if age <= 12:
    print("Please pay 7$")
elif age <= 18:
    print("Please pay 7$")
if age > 18:
    print("Please pay 10$")