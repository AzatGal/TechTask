"""
Напишите на C# или Python библиотеку для поставки внешним клиентам,
которая умеет вычислять площадь круга по радиусу и треугольника по
трем сторонам. Дополнительно к работоспособности оценим:

- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным
"""
import math
import unittest


class Figure:
    def __init__(self, *args):
        self.figures = [False, Circle, False, Triangle]
        args_size = len(args)
        if args_size <= len(self.figures) and self.figures[args_size] != False:
            self.figure = self.figures[args_size](*args)
        else:
            print("Нет поддержки данной фигуры")

    def square(self):
        return self.figure.square()


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * (self.radius**2)


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        self.side1 = sides[0]
        self.side2 = sides[1]
        self.side3 = sides[2]
        self.exist = True
        if self.side1 + self.side2 < self.side3:
            self.exist = False

    def square(self):
        if not self.exist:
            return "Такого треугольника не существует"
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        return math.isclose(self.side1**2 + self.side2**2, self.side3**2)

# Unit тесты
class FigureTests(unittest.TestCase):
    def test_circle_square(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.square(), math.pi * 5**2)

    def test_triangle_square(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.square(), 6.0)

    def test_triangle_not_exist(self):
        triangle = Triangle(1, 1, 10)
        self.assertEqual(triangle.exist, False)

    def test_triangle_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_figure(self):
        unknown_fig_1 = Figure(3)
        circle = Circle(3)
        self.assertAlmostEqual(unknown_fig_1.square(), circle.square())

        unknown_fig_2 = Figure(3, 2, 4)
        triangle = Triangle(3, 2, 4)
        self.assertAlmostEqual(unknown_fig_2.square(), triangle.square())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)