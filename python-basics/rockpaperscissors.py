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


options = [rock, paper, scissors]

player_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
player_choice = ""

print("\n")

if player_selection >= 3 or player_selection < 0:
    print("Wrong selection!\n")
else:
    player_choice = options[player_selection]
    print(f"You chose: {player_choice}")

computer_choice = options[random.randint(0, len(options) - 1)]

print("Computer chose:")
print(computer_choice)

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == rock and computer_choice == scissors \
        or player_choice == paper and computer_choice == rock \
        or player_choice == scissors and computer_choice == paper:
    print("You won!")
else:
    print("You lost!")




