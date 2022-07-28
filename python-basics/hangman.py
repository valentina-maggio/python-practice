# Hangman game

import random
from hangmanart import stages, logo
from hangmanwords import word_list


chosen_word = random.choice(word_list)

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ["_"] * len(chosen_word)

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess in display:
        print(f"You have already guessed letter: {guess}. Try again!")

    if guess not in chosen_word:
        lives -= 1
        print(f"I'm sorry, but letter {guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lost!")

    print(f"{' '.join(display)}")
    print(stages[6 - lives])

    if "_" not in display:
        end_of_game = True
        print("You won!")

