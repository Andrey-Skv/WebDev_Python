""" Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. """

def nums_request(hidden_num, attempts_num):

    def guess_num():
        for _ in range(attempts_num):
            user_num = int(input('Введите своё число: '))
            if user_num == hidden_num:
                return 'Вы угадали!'
        return 'Попытки закончились, вы не угадали!'

    return guess_num

# hidden_num = int(input('Задайте число от 1 до 100: '))
# attempts_num = int(input('Установите число попыток от 1 до 10: '))
user_game = nums_request(15, 5)
print(user_game())

#

def guessing_game(low, high, attempts):
    import random  # Импортируем модуль random для генерации случайных чисел

    secret_number = random.randint(low, high)  # Генерируем случайное число и сохраняем его

    def make_guess():
        for _ in range(attempts):  # Перебираем количество попыток
            guess = int(input(f'Введите число от {low} до {high}: '))  # Просим пользователя ввести угадываемое число

            if guess < secret_number:
                print('Загаданное число больше, чем ваше предположение.')
            elif guess > secret_number:
                print('Загаданное число меньше, чем ваше предположение.')
            else:
                print('Поздравляем! Вы угадали число!')
                return
        print(
            f'Вы проиграли. Загаданное число было: {secret_number}')  # Выводим загаданное число, если пользователь не угадал

    return make_guess  # Возвращаем функцию для угадывания числа


# Пример использования функции-замыкания для загадывания чисел от 1 до 100 с 5 попытками
game = guessing_game(1, 100, 5)
game()

#

def guess_num(tries: int = 5, num: int = 50):
    def prompt():
        nonlocal tries, num
        while tries > 0:
            print(f'Осталось {tries} попыток.')
            attempt = int(input('Введите число:\n'))
            if attempt == num:
                print('Вы угадали.')
                return True
            else:
                print('Вы не угадали.')
                tries -= 1
                if tries == 0:
                    print('Попытки закончились.')
                    return False

    return prompt


game = guess_num(5, 75)
game()

#

from random import randint as ri

MIN_LIMIT = 1
MAX_LIMIT = 100
MIN_COUNT = 1
MAX_COUNT = 10


def guess_rules(func):
    def inner(number, count):
        user_number = number if MIN_LIMIT <= number <= MAX_LIMIT else ri(MIN_LIMIT, MAX_LIMIT)
        user_count = count if MIN_COUNT <= count <= MAX_COUNT else ri(MIN_COUNT, MAX_COUNT)
        func(user_number, user_count)

    return inner


@guess_rules
def guess_game(user_number, user_count):
    while user_count:
        guess_num = int(input(f'Угадайте число от {MIN_LIMIT} до {MAX_LIMIT}: '))
        if guess_num == user_number:
            print(f'Ура, ты победил! Это число {user_number}')
            return
        elif guess_num < user_number:
            print('Загаданное число больше!')
        else:
            print('Загаданное число меньше!')
        user_count -= 1
    print(f'Увы! Ты проиграл! Это было число {user_number}!')


if __name__ == '__main__':
    game = guess_rules(169, 7)
    game()

20:22
def nums_request(hidden_num, attempts_num):

    def guess_num():
        for _ in range(attempts_num):
            user_num = int(input('Введите своё число: '))
            if user_num == hidden_num:
                return 'Вы угадали!'
        return 'Попытки закончились, вы не угадали!'

    return guess_num

# hidden_num = int(input('Задайте число от 1 до 100: '))
# attempts_num = int(input('Установите число попыток от 1 до 10: '))
user_game = nums_request(15, 5)
print(user_game())