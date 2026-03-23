# structure: def my_function():
# do this
# do this
# then do this
# call it word my_function()

# Functions without
def test_function():
    print("This is a function")

# Functions with input
def greet(name):
    print(f"Hello {name}")
    print("How do do you do?")

test_function()
greet("Kevin")

# argument vs parameter: parameter -> det du faktiskt skickar in -> argument -> variablen

def greetings(name, age):
    print(f"Hej {name}, du är {age} år!")

greetings("Kevin", 29)

# Weeks left
def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(29)