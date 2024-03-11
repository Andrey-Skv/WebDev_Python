""" В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) 
имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст 
(целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), 
который должен быть шестизначным положительным целым числом.
Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях 
(Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать 
исключения InvalidNameError и InvalidAgeError, если данные неверные.
Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный 
номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, 
если ID неверный.
Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы 
цифр в его ID (по остатку от деления на 7).
Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают 
корректно при передаче неверных данных. """

MIN_ID = 100000
MAX_ID = 1000000

class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message

class Person:
    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(middle_name, str) or len(middle_name.strip()) == 0:
            raise InvalidNameError(middle_name)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.middle_name = middle_name.title()
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name} {self.age}'

class Employee(Person):
    def __init__(self, first_name, last_name, middle_name, age, id):
        super().__init__(first_name, last_name, middle_name, age)
        if not isinstance(id, int) or id < MIN_ID or id > MAX_ID:
            raise InvalidIdError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.id = id

    def get_level(self):
        return sum(int(digit) for digit in str(self.id)) % 7

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name} {self.age} {self.id}'

if __name__ == '__main__':
    p1 = Person('Иванов', 'Иван', 'Иванович', 23)
    print(p1)

