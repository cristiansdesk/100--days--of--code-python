import random
from art import logo

def deal_cards():
    """Start of game dealing cards in random choice."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def check_blackjack(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "You have Blackjack, You Win."

    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def check_cards(u_score, c_score):
    if u_score == c_score:
        return "It's a draw."
    elif u_score > 21:
        return "You went over 21, YoU Lose."
    elif c_score > 21:
        return "You Win"
    elif u_score > c_score:
        return "You Win."
    else:
        return "You Lose."


def play_blackjack():
    print(logo)
    user_cards = []
    comp_cards = []
    user_score = 0
    comp_score = 0

    for card in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    user_score += sum(user_cards)
    comp_score += sum(comp_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {comp_cards[0]}")

    game_on = True
    while game_on:
        hit_me = input("Do you want another card? 'y' or 'n': ").lower()
        if hit_me == 'y':
            user_score = check_blackjack(user_cards)
            user_cards.append(deal_cards())
        else:
            if comp_score < 17:
                comp_score = check_blackjack(comp_cards)
                comp_cards.append(deal_cards())
            else:
                game_on = False
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {comp_cards}, final score: {comp_score}")
            print(f"{check_cards(user_score, comp_score)}")

play_blackjack()