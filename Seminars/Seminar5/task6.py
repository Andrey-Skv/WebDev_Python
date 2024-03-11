"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

def num_prime(num):          # реализуем функцию проверки числа на простоту
    for i in range(2, num):
        if not num % i:
            return False
    return True


def my_gen(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if num_prime(num):
            yield num
            count += 1


print(*my_gen(15))