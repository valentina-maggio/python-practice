from higherlowerart import logo, vs
from higherlowerdata import data
import random

print(logo)
print("Welcome to the Higher Lower Game!")


def check_answer(user_answer, celebs_to_compare, solution):
    if user_answer == 'A' and celebs_to_compare[0] == solution or user_answer == 'B' and celebs_to_compare[
            1] == solution:
        return True
    elif user_answer == 'A' and celebs_to_compare[1] == solution or user_answer == 'B' and celebs_to_compare[
            0] == solution:
        return False


def play_game():
    is_game_over = False
    score = 0

    while not is_game_over:
        celebs_to_compare = random.sample(data, 2)
        solution = max(celebs_to_compare, key=lambda x: x['follower_count'])

        print(
            f"Compare A: {celebs_to_compare[0]['name']}, a {celebs_to_compare[0]['description']}, "
            f"from {celebs_to_compare[0]['country']}")
        print(vs)
        print(
            f"Compare B: {celebs_to_compare[1]['name']}, a {celebs_to_compare[1]['description']}, "
            f"from {celebs_to_compare[1]['country']}")

        user_answer = input("Who has more followers? Type 'A' or 'B': ")

        if check_answer(user_answer, celebs_to_compare, solution):
            score += 1
            print(f"\nYou are right! Current score: {score}.\n")
        else:
            print(f"\nSorry, you are wrong. Current score: {score}.")
            is_game_over = True


play_game()
