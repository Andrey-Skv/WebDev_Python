"""
Задание №6
📌 На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
📌 Напишите 3-7 тестов pytest для данного проекта.
📌 Используйте фикстуры.
"""

import json

import pytest


class BasedExep(Exception):
    pass


class NameErr(BasedExep):
    def __str__(self):
        return f"Ошибка имени"


class LevelErr(BasedExep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня"


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level


class CheckUserLogin:
    users = []

    @staticmethod
    def create_user(name, id, level):
        try:
            if level > 3:
                raise LevelErr(level)
        except LevelErr as e:
            print(e)
        else:
            obj = User(name, id, level)
            CheckUserLogin.users.append(obj)

    @staticmethod
    def load_users():
        with open('task13_4.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
            for level, user_list in user_dict.items():
                for id, name in user_list.items():
                    CheckUserLogin.users.append(User(name, id, level))

    @staticmethod
    def get_login_level(name):

        for el in CheckUserLogin.users:
            if name == el.name:
                return 'Пользователь найден'
            raise NameErr()


@pytest.fixture
def func():
    obj = CheckUserLogin()
    obj.load_users()
    return obj


def test_access(func):
    assert func.get_login_level('Новиков') == 'Пользователь найден'


def test_except(func):
    with pytest.raises(NameErr):
        func.get_login_level('Федоров')


if __name__ == '__main__':
    pytest.main(['-v'])
