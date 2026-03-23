import random
from word_list import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for _ in chosen_word:
    display.append("_")

print(display)

lives = 6
game_over = False

while not game_over:
    guess = input("Gissa en bokstav: ").lower()
    print(stages[6 - lives])

    if guess not in chosen_word:
        lives -= 1
        print(f"Fel! '{guess}' finns inte i ordet. Du har {lives} liv kvar.")
        
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    
    print(" ".join(display))

    if "_" not in display:
        print("You won!")
        game_over = True

    if lives == 0:
        print(f"Game over! Ordet var '{chosen_word}'")
        game_over = True
        