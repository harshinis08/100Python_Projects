import random

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

user_cards = []
computer_cards = []

if user_input == 'y':
    print("Ok...")

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J']

    card1 = random.choice(cards)
    card2 = random.choice(cards)

    user_cards.append(card1)
    user_cards.append(card2)

    print(f"Your cards [{card1}, {card2}]")

    computer_card1 = random.choice(cards)
    computer_cards.append(computer_card1)

    print(f"Computer's first card {computer_card1}")

    another_card_request = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card_request == 'y':
        card3 = random.choice(cards)
    else:
        print(f"Your final hand : [{card1}, {card2}")
        computer_card2 = random.choice(cards)

        computer_cards.append(computer_card2)

        print(f"Computer's final hand: [{card1}, {card2}")

