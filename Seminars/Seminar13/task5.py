""" Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа. """

from json import load, dump
import secrets
from task4 import User


class NameError(Exception):
    pass


class LevelError(Exception):
    pass


class Repo:
    users = set()

    @staticmethod
    def load_users(path):
        with open(path, encoding='utf-8') as f:
            data = load(f)
        for level, value in data.items():
            for id, name in value.items():
                Repo.users.add(User(name, id, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f"{name} Пользователь найден!"
            raise NameError
        except NameError:
            return 'Пользователь не найден'


    @staticmethod
    def create_user(name, id_user, level):
        try:
            if level > 3:
                raise LevelError
            else:
                Repo.users.add(User(name, id_user, level))
        except LevelError:
            return 'Ошибка уровня'


if __name__ == '__main__':
    repo = Repo()
    # repo.load_users('task13_4.json')
    # print(repo.check_login('Новиков'))
    repo.create_user('Семенов', '8', 3)
    repo.load_users('task13_4.json')
    print(*repo.users, sep='\n')