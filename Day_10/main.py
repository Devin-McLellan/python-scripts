from calculator import Calculator
from art import logo
from colorama import Fore, Style, init
init()

def start_calculator():
    # TODO: Create an instance of the Calculator class

    print(Fore.CYAN + logo)
    calc = Calculator()

    operations = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide,
    }
    # TODO: Ask user for first number
    while True:
        try:
            first_number = float(input("Please enter first number: "))
            break
        except ValueError:
            print("Try again, invalid input")

    # TODO: Display operation symbols (e.g., +, -, *, /)
    print("=" * 10)
    print(Fore.GREEN + "Valid choices: '+', '-', '*', '/'")
    
    # TODO: Ask user to pick an operation symbol
    while True:
        operation = input("Pick a operation: ")
        if operation not in operations:
            print(Fore.RED + "Invalid operation!")
            continue
        break

    # TODO: Ask user for the next number
    while True:
        try:
            second_number = float(input("Please enter second number: "))
            break
        except ValueError:
            print("Try again, invalid input")
            continue

    # TODO: Use the calculator object to perform the calculation
    # Hint: answer = calc.add(num1, num2)

    try:
        result = operations[operation](first_number, second_number)
        print(Fore.LIGHTMAGENTA_EX + f"{first_number} {operation} {second_number} = {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

    print(Style.RESET_ALL)

if __name__ == "__main__":
    start_calculator()
    