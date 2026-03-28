print("Welcome to the tip calculator")

try:
    bill = float(input("What was the total bill?: "))
except ValueError:
    print("Invalid input. Please enter a number for the bill.")
    exit()
try:
    tip = int(input("How much tip would you like to give? 10, 12, or 15: "))
except ValueError:
    print("Invalid input. Please enter 10, 12, or 15.")
    exit()

if tip not in [10, 12, 15]:
    print("Invalid tip percentage. Please choose 10, 12, or 15.")
    exit()

try:
    splitBill = int(input("How many people to split the bill?: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if splitBill < 1:
    print("Number of people must be at least 1.")
    exit()

total = round(bill * (1 + tip / 100) / splitBill, 2)

print(f"Each person should pay: ${total:.2f}")