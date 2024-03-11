# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию, выведите:
#
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
#
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов
# (от 0 до 100). В противном случае выведите:
#
# Оценка должна быть целым числом от 2 до 5
#
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
# следующая информация.
#
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по
# предметам. Класс должен иметь следующие методы:
# Атрибуты класса:
#
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
# качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.
#
# Магические методы (Dunder-методы):
#
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента
# и файл с предметами и их результатами. Инициализирует атрибуты name и subjects
# и вызывает метод load_subjects для загрузки предметов из файла.
#
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
# Убеждается, что name начинается с заглавной буквы и состоит только из букв.
#
# __getattr__(self, name): Позволяет получать значения атрибутов предметов
# (оценок и результатов тестов) по их именам.
#
# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
#
# Методы класса:
#
# load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль
# csv для чтения данных из файла и добавляет предметы в атрибут subjects.
#
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается,
# что оценка является целым числом от 2 до 5.
#
# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
# Убеждается, что результат теста является целым числом от 0 до 100.
#
# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
#
# get_average_grade(self): Возвращает средний балл по всем предметам.
#
# Пример
#
# На входе:
#
#
# student = Student("Иван Иванов", "subjects.csv")
#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
#
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
#
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
#
# print(student)
# На выходе:
#
#
# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История
import csv


class Verified:
    def __init__(self):
        self.param_name = None

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"You don't have permission to delete  {self.param_name}")

    def validate(self, value):
        if not value.istitle or not value.replace(" ", '').isalpha():
            print(f"ФИО должно состоять только из букв и начинаться с заглавной буквы")


class Student:

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        return self.name

    def __setattr__(self, name, value):
        if isinstance(value, str):
            if not value.istitle() or not value.replace(' ', '').isalpha():
                print(f"ФИО должно состоять только из букв и начинаться с заглавной буквы")
                exit(1)
        object.__setattr__(self, name, value)

    def __str__(self):
        res = f"Студент: {self.name}\nПредметы: "
        for name in self.subjects:
            if len(self.subjects[name]) > 0:
                res += name + ', '
        return res.rstrip(', ')

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                for item in row:
                    self.subjects[item] = {}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            print(f"Оценка должна быть целым числом от 2 до 5")
            exit(1)
        self.subjects[subject]['grade'] = grade

    def add_test_score(self, subject, test_score):
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            print(f"Результат теста должен быть целым числом от 0 до 100")
            exit()
        if not self.subjects[subject].get('test_score'):
            self.subjects[subject]['test_score'] = [test_score]
        else:
            self.subjects[subject]['test_score'].append(test_score)

    def get_average_grade(self):
        average_grd = 0
        count = 0
        for item in self.subjects:
            if self.subjects[item].get('grade'):
                average_grd += self.subjects[item]['grade']
                count += 1
        return average_grd / count if count else None

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not self.subjects[subject].get('test_score'):
            return None
        average_ts = 0
        for item in self.subjects[subject]['test_score']:
            average_ts += item
        return average_ts / len(self.subjects[subject]['test_score'])


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 10)

    student.add_grade("История", 5)
    student.add_test_score("Математика", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)