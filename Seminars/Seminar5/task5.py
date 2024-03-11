"""
Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
"""

matrix = [[f'{i:2} * {j:2} = {i * j:2}' for i in range(2, 10)] for j in range(2, 11)]
print(*matrix, sep='\n')

def print_table(data):
    count = 0
    for el in data:
        print(el, end='\t\t')
        count += 1
        if count % 4 == 0:
            print()
    print()


half_table_1 = (f'{j} * {i} = {j * i}' for i in range(2, 11) for j in range(2, 6))
half_table_2 = (f'{j} * {i} = {j * i}' for i in range(2, 11) for j in range(6, 10))

print_table(half_table_1)
print_table(half_table_2)