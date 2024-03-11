"""
Задание №5
📌 На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.
"""

import unittest


class Rectangle:
    """
    Класс "Прямоугольник" для выполнения действий с прямоугольниками,
    позволяет сравнивать прямоугольники по площади,
    получить площадь и периметр прямоугольников
    складывать и вычитать прямоугольники
    """

    # __slots__ = ('_width', '_length')

    def __init__(self, side_a, side_b=0):
        self._width = side_a
        if side_b == 0:
            side_b = side_a
        self._length = side_b

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise ValueError("Длина должна быть больше 0")
        self._length = new_len

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("Ширина должна быть больше 0")
        self._width = new_width

    def get_perimeter(self):
        return 2 * (self._width + self._length)

    def get_area(self):
        return self._width * self._length

    def __add__(self, other):
        """
        сложение прямоугольников, складываются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после сложения периметров
        """
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """
        вычитание прямоугольников, вычитаются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после вычитания периметров
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        res = f'Прямоугольник со сторонами {self._width} и {self._length}'
        return res


class TestRectangle(unittest.TestCase):

    def test_1_area(self):
        self.assertEqual(Rectangle.get_area(Rectangle(7, 11)), 77)

    def test_2_perimeter(self):
        self.assertEqual(Rectangle.get_perimeter(Rectangle(5, 10)), 30)

    def test_sub(self):
        self.assertEqual(str(Rectangle(7, 11) - Rectangle(5, 10)),
                         'Прямоугольник со сторонами 6 и 6')

    def test_sum(self):
        self.assertEqual(str(Rectangle(7, 11) + Rectangle(5, 10)),
                         'Прямоугольник со сторонами 66 и 66')

    def test_gt(self):
        self.assertEqual((Rectangle(7, 11) > Rectangle(5, 10)), True)

    def test_lt(self):
        self.assertEqual((Rectangle(7, 11) < Rectangle(5, 10)), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
