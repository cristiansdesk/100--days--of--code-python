print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go 'L' for Left or 'R' for right? ").upper()

if choice1 == 'L':
    choice2 = input("You've come to a lake, there's an island on that lake.\n"
                    "Type 'W' to Wait or 'S' to Swim? ").upper()
    if choice2 == 'W':
        choice3 = input("You arrive at the island unharmed, there's\n"
                        " a house with 3 doors. Choose 'B' for\n"
                        "Blue, 'Y' for Yellow or 'R' for Red: ").upper()
        if choice3 == 'Y':
            print("You found the treasure, You Win.")
        elif choice3 == 'B':
            print("You enter a room of beasts, Game Over.")
        else:
            print("You walked into a room of fire, Game Over.")
    else:
         print("You get attacked by trout, Game Over.")
else:
    print("You fall into a whole, Game Over.")