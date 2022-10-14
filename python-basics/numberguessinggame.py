from random import randint


logo = """
   ___                  _____ _          _  _            _             
  / __|_  _ ___ ______ |_   _| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-<   | | | ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/   |_| |_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|  
"""


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 4)
    print(f"psssss the answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


play_game()




