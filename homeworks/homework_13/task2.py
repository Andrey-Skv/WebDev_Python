""" Допишите в вашу задачу Archive обработку исключений.
Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является 
строкой или является пустой строкой.
Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом 
с плавающей запятой.
Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.' """

from typing import Union

class InvalidTextError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidNumberError(Exception):
    def __init__(self, message):
        self.message = message


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or text == '':
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        self.text = text
        if not isinstance(number, (int, float)) or number < 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not isinstance(text, str) or text == '':
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        self._text = text
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, (int, float)) or number < 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        self._number = number


if __name__ == '__main__':
    start = Archive(' ', 1)
    two = Archive('two', 2)
    three = Archive('three', 3)
    three.number = 4
    print(start)
