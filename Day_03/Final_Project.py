logo = '''
*******************************************************************************
      |                   |                  |                     |
______|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
      |                `"=._o`"=._      _`"=._                     |
______|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
______|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______
*******************************************************************************
'''

print(logo)
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You're at a crossroad.\n")

direction = input("Where do you want to go? (Left/Right): ").upper()

if direction == "LEFT":
    swim_or_wait = input("\nYou reach a lake. There's a boat nearby. Swim or wait? (Swim/Wait): ").upper()

    if swim_or_wait == "WAIT":
        print("\nYou arrive at a house with three doors: Red, Blue, and Yellow.")
        door = input("Which door do you choose? (Red/Blue/Yellow): ").upper()

        if door == "YELLOW":
            print("\nYou found the treasure! Congratulations, you win!")
        elif door == "RED":
            print("\nYou walked into a fire. Game over!")
        elif door == "BLUE":
            print("\nYou were eaten by beasts. Game over!")
        else:
            print("\nInvalid choice. Game over!")

    elif swim_or_wait == "SWIM":
        print("\nYou got attacked by a trout. Game over!")
    else:
        print("\nInvalid choice. Game over!")

elif direction == "RIGHT":
    print("\nYou fell off a cliff. Game over!")
else:
    print("\nInvalid direction. Game over!")
