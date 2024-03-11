""" Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
 На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
  которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) 
в зависимости от результата проверки.
Пример использования На входе:

date_to_prove = 15.4.2023
На выходе:

True
На входе:

date_to_prove = 31.6.2022
На выходе:

False
 """

date_to_prove = "28.2.2023"

def _year_funk(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def true_data(data):
    day, month, year = [int(el) for el in data.split('.')]
    if year > 9999 or month > 12 or month <= 0 or day <= 0 or year <= 0:
        return False
    month_30 = {4, 6, 9, 11}
    month_31 = {1, 3, 5, 7, 8, 10, 12}
    if month in month_30 and day <= 30:
        return True
    elif month in month_31 and day <= 31:
        return True
    elif month == 2:
        if _year_funk(year) and day <= 29:
            return True
        elif day <= 28:
            return True
    return False


print(true_data(date_to_prove))


#

from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))
