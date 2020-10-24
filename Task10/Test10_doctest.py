"""
Негативный тест
>>> Sqr.check_length_sides_of_triangle((2, 2, 4))
Traceback (most recent call last):
AssertionError: Сумма двух любых сторон треугольника должна быть больше третьей.

Негативный тест
>>> Sqr.check_sides_of_triangle("2, 2, 4, 5")
Traceback (most recent call last):
AssertionError: Треугольник должен иметь 3 стороны.

Позитивный тест
>>> Sqr.check_length_sides_of_triangle((11, 12, 13))
True

Позитивный тест
>>> Sqr.square_of_triangle((12, 13, 14))
72.30793524918272

Позитивный тест
>>> Sqr.square_of_triangle((3, 4, 8))
Traceback (most recent call last):
AssertionError: Сумма двух любых сторон треугольника должна быть больше третьей.
"""

import Test10 as Sqr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
