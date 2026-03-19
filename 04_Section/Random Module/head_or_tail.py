import random

print("Welcome to heads or tail")

user_input = input("Heads or tails? ").lower()

random_num = random.randint(0 , 1)
result = "tails" if random_num == 0 else "heads"

print(f"You choose: {user_input}")
print(f"We got: {result.capitalize()}")

if user_input == result:
    print("You win")
else:
    print("You lose!")
