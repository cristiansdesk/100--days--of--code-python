import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

choice = int(input("What do you choose, '0' for Rock, '1' for paper or '2' for scissor: "))
if choice >= 0 and choice <= 2:
    print(game_images[choice])

print("Computer chooses:")

comp_choice = random.randint(0, 2)
print(game_images[comp_choice])

if choice < 0 or choice >= 3:
    print("Please type a number, try again.")
elif choice == 0 and comp_choice == 2:
    print("You Win.")
elif comp_choice == 0 and choice == 2:
    print("You Lose.")
elif choice > comp_choice:
    print("You Win.")
elif comp_choice > choice:
    print("You Lose.")
elif choice == comp_choice:
    print("Its a Draw.")
