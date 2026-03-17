print("Welcome to the tip calculator")

try:
    bill = float(input("What was the total bill?: "))
except ValueError:
    print("Invalid input")
    exit()

try:
    tip = int(input("What was the total tip? 10, 12 or 15: "))
except ValueError:
    print("Invalid input")
    exit()

if tip not in (10, 12, 15):
    print("Invalid")
    exit()

try:
    split = int(input("Numbers of people splitting?: "))
except ValueError:
    print("Invalid input")
    exit()

if split < 1:
    print("Invalid")
    exit()

total = round(bill * (1 + tip / 100) / split, 2)

print(f"Each person should pay: ${total:.2f}")
