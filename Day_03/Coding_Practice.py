# Prices
small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_price = 2
extra_cheese_price = 1

total = 0

print("Welcome to Python Pizza Deliveries!")

size = input("What size do you want? (L/M/S): ").upper()
if size == "L":
    total += large_pizza
elif size == "M":
    total += medium_pizza
elif size == "S":
    total += small_pizza
else:
    print("Invalid size entered, default small")
    total += small_pizza

pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
if pepperoni == "Y":
    total += pepperoni_price

extra_cheese = input("Do you want cheese? (Y/N): ").upper()
if extra_cheese == "Y":
    total += extra_cheese_price

print(f"Your total price is: {total}")

# With functions

def get_pizza_size():
    while True:
        size = input("What size do you want? (S/M/L): ").upper()
        prices = {"S":15, "M":20, "L":25}
        if size in prices:
            return prices[size]
        print("Invalid choice. Please enter S,M, or L")

