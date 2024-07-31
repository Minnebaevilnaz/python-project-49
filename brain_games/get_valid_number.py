import prompt


def get_valid_number():
    while True:
        player_answer = prompt.string('Your answer: ')
        try:
            # Попытка преобразовать введенное значение в целое число
            number = int(player_answer)
            return number
        except ValueError:
            # Обработка ошибки, если введенное значение не является числом
            print("Invalid input. Please enter a valid integer.")
