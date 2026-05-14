import random
from art import logo

def set_difficulty(level):
    if level == 'e':
        return easy
    else:
        return hard

def check_guess(choice,  result):
    if choice not in range(1, 101):
        return "That's not a number."
    elif choice > result:
        return "Too High."
    elif choice < result:
        return "Too Low."

def lives_remaining(attempts):
    attempts -= 1
    if attempts == 0:
        print(f"You have {attempts} attempts remaining, You Lose.")
    return attempts


easy = 10
hard = 5
used_numbers = []

print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100.\n")
answer = random.randint(1, 100)
difficulty_level = input("Chose difficulty level, 'e' or 'h': ").lower()
lives = set_difficulty(difficulty_level)

guess_on = True
while guess_on:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Guess a number: "))
    if guess in used_numbers:
        print("You already guess that")
    else:
        print(check_guess(guess, answer))
        used_numbers.append(guess)

        if guess == answer:
            print("You Win.")
            guess_on = False
        else:
            lives =  lives_remaining(lives)
            if lives == 0:
                guess_on = False




