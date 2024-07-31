import random
from brain_games.messages import lose_message, win_message, welcome_message
from brain_games.answer_checker import is_correct_answer
import prompt


def is_even(num: int):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def play_game(player_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0

    while correct_answers_count < 3:
        random_number = random.randint(0, 1000)
        print(f'Question: {random_number}')
        player_answer = prompt.string('Your answer: ')
        correct_answer = is_even(random_number)

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
