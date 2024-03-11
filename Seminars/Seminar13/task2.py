""" Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений. """


def get_dict(dict, key, default_value=None):
    try:
        return dict[key]
    except KeyError:
        return default_value

dict={2:'qwe', 3:'ddf'}
key1=2
key2=1

print(get_dict(dict, key1))
print(get_dict(dict, key2))