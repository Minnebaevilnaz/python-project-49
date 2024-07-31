import random
from brain_games.messages import lose_message, win_message, welcome_message
from brain_games.answer_checker import is_correct_answer
from brain_games.get_valid_number import get_valid_number


def generate_arithmetic_progression():
    step = random.randint(1, 100)
    length = random.randint(5, 11)
    start = random.randint(0, 100)
    return [start + step * i for i in range(length)]


def generate_question_progression(progression, correct_answer):
    replacement = '..'
    question_progression = [str(
        replacement if x == correct_answer else x)
        for x in progression
    ]
    return ' '.join(question_progression)


def play_game(player_name):
    print('What number is missing in the progression?')
    correct_answers_count = 0
    while correct_answers_count < 3:
        progression = generate_arithmetic_progression()
        correct_answer = random.choice(progression)
        print(f'Question: '
              f'{generate_question_progression(progression, correct_answer)}')
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
