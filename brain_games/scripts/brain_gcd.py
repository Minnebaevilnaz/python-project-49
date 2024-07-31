
import random
from brain_games.messages import lose_message, win_message, welcome_message
from brain_games.answer_checker import is_correct_answer
from math import gcd
from brain_games.get_valid_number import get_valid_number


def play_game(player_name):
    correct_answers_count = 0

    while correct_answers_count < 3:
        random_number_one = random.randint(1, 100)
        random_number_two = random.randint(1, 100)
        correct_answer = gcd(random_number_one, random_number_two)
        print("Find the greatest common divisor of given numbers.")
        print(f'Question: {random_number_one}  {random_number_two}')
        player_answer = get_valid_number()

        if is_correct_answer(player_answer, correct_answer):
            correct_answers_count += 1
            print("Correct!")
        else:
            lose_message(player_answer, correct_answer, player_name)
            break

    else:
        win_message(player_name)


def main():
    player_name = welcome_message()
    play_game(player_name)


if __name__ == "__main":
    main()
