"""
Задание №3
📌 Добавьте к задачам 1 и 2 строки документации для классов.
"""

"""
MyStr - class, наследует все возможности класса str
также имеет дополнительные атрибуты
"""

# для def __new__(cls, value, author_name):
"""
Создает экземпляр класса с дополнительными атрибутами
value: Переданная строка
author_name: имя автора-создателя
creation_time = datetime.datetime.now() - время создания
"""

"""
класс Archive хранит свойства:
число и строку, а также list-архивы предыдущих экземпляров класса.
При нового экземпляра класса, старые данные из ранее созданных экземпляров 
сохраняются в два списковархивов
"""


class Archive:
    '''
    Класс Archive наследует функциональность класса
    '''
    last_num = None
    last_str = None
    str_archives = []
    num_archives = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        if Archive.last_num is not None:
            Archive.num_archives.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archives.append(Archive.last_str)
        Archive.last_num = number
        Archive.last_str = text


obj1 = Archive(1, '1')
print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
obj2 = Archive(2, '2')
print(obj2.number, obj2.text, obj2.num_archives, obj2.str_archives)
obj3 = Archive(3, '3')
print(obj3.number, obj3.text, obj3.num_archives, obj3.str_archives)
print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
print(obj1.num_archives)
print(obj1.__doc__)
print(obj1.__dict__)
print(Archive.__dict__)