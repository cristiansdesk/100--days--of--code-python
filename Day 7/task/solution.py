import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = ["_"] * word_length
print(placeholder)
lives = 6
used_letters = []
game_on = True

while game_on:
    guess = input("Guess a letter: ").upper()
    if guess in used_letters:
        print(f"You already chose {guess}, try again.")
        continue
    used_letters.append(guess)
    if guess not in chosen_word:
        lives -= 1
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            placeholder[position] = letter
    print(f"Current word: " + "".join(placeholder))
    print(lives)
    if "_" not in placeholder:
        game_on = False
        print("you win")
    if lives == 0:
        game_on = False
        print("you lose")