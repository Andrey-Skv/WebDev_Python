"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
Числа в каждом списке не повторяются.
"""

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
count = 0
for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            count += 1
print('Количество совпадающих чисел: ', count)
