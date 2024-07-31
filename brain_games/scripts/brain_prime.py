import random
from brain_games.messages import lose_message, win_message, welcome_message
from brain_games.answer_checker import is_correct_answer

import prompt


def is_prime(a):
    if a <= 1:
        return "no"
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return "no"
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return "no"
        i += 6
    return "yes"


def play_game(player_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_count = 0

    while correct_answers_count < 3:
        random_number = random.randint(0, 1000)
        print(f'Question: {random_number}')
        player_answer = prompt.string('Your answer: ')
        correct_answer = is_prime(random_number)

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
