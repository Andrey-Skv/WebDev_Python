""" Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.

 """

from datetime import date
import logging

logging.basicConfig(filename='example.log.', filemode='w', encoding='utf-8', level=logging.ERROR)


def user_date(data_text):
    dict_month = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                  'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    dict_days = {'понедельник': 1, 'вторник': 2, 'среда': 3, 'четверг': 4,
                 'пятница': 5, 'суббота': 6, 'воскресенье': 7}
    try:
        data_text = data_text.split()
        num_week, day, month = int(data_text[0][0]), int(dict_days[data_text[1]]), \
            int(dict_month[data_text[2]])
    except ValueError:
        logging.error('Некорректный формат данных')
        return 'Некорректный формат данных'

    # получаем параметры заданной даты
    data_month = month  # месяц заданной даты
    data_year = date.today().year  # текущий год - год заданной даты

    first_day_data_month = date(data_year, data_month, 1).weekday()  # номер дня недели первого числа месяца
    # определяем день заданной даты
    if first_day_data_month >= day:
        data_day = (7 - first_day_data_month) + (
                num_week - 1) * 7 + day  # если в первой неделе месяца нет такого дня недели
    else:
        data_day = (7 - first_day_data_month) + (
                num_week - 2) * 7 + day  # если в первой неделе месяца есть такой день недели
    try:
        data = date(data_year, data_month, data_day)
    except ValueError:
        logging.error('Нет такого дня в этом месяце')
        return 'Нет такого дня в этом месяце'

    return data


dates = ['1-й вторник марта', '1-й четверг ноября', 'опять вторник в марте', '3-я среда мая', '5-й четверг апреля']
for el in dates:
    print(user_date(el))