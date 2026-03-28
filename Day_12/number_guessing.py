from art import logo
from colorama import Fore, Style
import random

def presentation():
    print(Fore.GREEN +

    """Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100. \n Chose a difficulty. 
    Type 'Easy' or 'Hard: """ + Style.RESET_ALL)

def random_num():
    random_number = random.randint(1,100)
    return random_number

def print_logo():
    print(Fore.LIGHTCYAN_EX + logo)

def hard(random_number):

    attempts = 5

    while attempts > 0:

        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ").lower().strip())

        if guess == random_number:
            return Fore.LIGHTCYAN_EX + "You win!" + Style.RESET_ALL

        elif guess < random_number:
            attempts -= 1
            print(Fore.RED + "Too low" + Style.RESET_ALL)

        elif guess > random_number:
            attempts -= 1
            print(Fore.RED + "Too high" + Style.RESET_ALL)
    return "Game over"

def easy(random_number):

    attempts = 10

    while attempts > 0:

        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ").lower().strip())

        if guess == random_number:
            return Fore.LIGHTCYAN_EX + "You win!" + Style.RESET_ALL

        elif guess < random_number:
            attempts -= 1
            print(Fore.RED + "Too low" + Style.RESET_ALL)

        elif guess > random_number:
            attempts -= 1
            print(Fore.RED + "Too high" + Style.RESET_ALL
)
    return "Game over"


def main():

    print_logo()

    presentation()

    random_number = random_num()

    user_choice = input().lower().strip()

    if user_choice == 'easy':
        print(easy(random_number))

    elif user_choice == "hard":
        print(hard(random_number))

    else:
        print(f"[{user_choice}]: Invalid")

main()