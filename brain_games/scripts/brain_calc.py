import random
from brain_games.messages import lose_message, win_message, welcome_message
from brain_games.answer_checker import is_correct_answer
from brain_games.get_valid_number import get_valid_number


def play_game(player_name):
    operations = ["+", "-", "*"]

    correct_answers_count = 0
    while correct_answers_count < 3:
        random_number_one = random.randint(0, 1000)
        random_number_two = random.randint(0, 1000)
        operation = random.choice(operations)
        print('What is the result of the expression?')
        match operation:
            case "+":
                correct_answer = random_number_one + random_number_two
                print(f'Question: {random_number_one} + {random_number_two}')
            case "-":
                correct_answer = random_number_one - random_number_two
                print(f'Question: {random_number_one} - {random_number_two}')
            case "*":
                correct_answer = random_number_one * random_number_two
                print(f'Question: {random_number_one} * {random_number_two}')

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
