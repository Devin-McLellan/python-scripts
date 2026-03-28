import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock/Paper/Scissor game")

userInput = input("Rock/Paper/Scissor?: ").lower()

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

# Print result
if userInput == "rock":
    print(rock)
elif userInput == "paper":
    print(paper)
elif userInput == "scissor":
    print(scissors)
else:
    print("Invalid Choice.")

# Check results
print(f"You chose: {userInput}")
print(f"Computer chose: {computer}")

if userInput == computer:
    print("It's a tie!")
elif (userInput == "rock" and computer == "scissor") or \
     (userInput == "paper" and computer == "rock") or \
     (userInput == "scissor" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")