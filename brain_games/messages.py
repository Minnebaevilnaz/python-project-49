import prompt


def welcome_message():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    return player_name


def lose_message(player_answer, right_answer, player_name):
    print(f"'{player_answer}' is wrong answer ;(."
          f" Correct answer was '{right_answer}'.\n "
          f"Let's try again, {player_name}!")


def win_message(player_name):
    print(f"Congratulations, {player_name}!")
