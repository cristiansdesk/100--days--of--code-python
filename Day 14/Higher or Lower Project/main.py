from art import logo, vs
from game_data import data
import random

def account_t(account):
    account_n = account["name"]
    account_d = account["description"]
    account_c = account["country"]
    return f"{account_n}, a {account_d}, from {account_c}"
account_1 = random.choice(data)
print(f"Compare A: {account_t(account_1)}")


def check_answer(guess, count_1, count_2):
    if count_1['follower_count'] > count_2['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
account_2 = random.choice(data)
game_on = True
score = 0
while game_on:

    account_1 = account_2
    account_2 = random.choice(data)

    if account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}")
    print(vs)
    print(f"Compare B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}")
    guess = input("Guess 'a' or 'b': ").lower()
    result = check_answer(guess, account_1, account_2)

    if result:
        score += 1
        print(f"Correct! Score: {score}")

    else:
        print(f"That's incorrect, You Lose. Final score: {score}")
        game_on = False
print(score)


















#print logo
# I need a random.choice(data) for compare A
# print compare A: {name} a {profession}, for {country}
# print Vs logo
# I need a random.choice(data) for compare B
# print compare B: {name} a {profession}, for {country}
# compare followers of A and B
# guess = input, who has the most followers? A or B?
# if guess is correct, compare_a = compare_b-------
# compare_b = random.choice(data)
# print, you're correct, your current score:
# if guess not in or == to answer
# print, that's incorrect, final score