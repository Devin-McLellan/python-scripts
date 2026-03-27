from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Oavgjort"

    elif computer_score == 0:
        return "Datorn har blackjack, du förlorade!"
    elif user_score == 0:
        return "Grattis du har blackjack, du vann!"

    elif user_score > 21:
        return "Du förlorade"
    elif computer_score > 21:
        return "Du vinner!"

    elif user_score > computer_score:
        return "Du har högst poäng, du vinner!"
    else:
        return "Datorn har högst poäng, du förlorar"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []

    # Dealing cards
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    play = True

    while play:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)

        print(f"[User score]: {user_score}")
        print(f"[computer score]: {computer_cards[0]}")

        if user_score == 0:
            print("Blackjack")
            play = False
        elif computer_score == 0:
            print("Blackjack")
            play = False
        elif user_score > 21:
            print("Bust")
            play = False

        else:
            play_again = input("Spela igen?: [y/n]: ").upper().strip()
            if play_again == 'Y':
                user_cards.append(deal_card())
            else:
                play = False

    while computer_score < 17 and not computer_score == 0:
       computer_cards.append(deal_card())
       computer_score = calculate_score(computer_cards)

    print(f"[Spelare]: [Kort]: {user_cards}, [Poäng]: {user_score}")

    print(f"[Dator]: [Kort]: {computer_cards}, [Poäng]: {computer_score}")

    print(compare(user_score, computer_score))

while input("Vill du spela Blackjack? [y/n]: ").lower() == 'y':
    play_game()