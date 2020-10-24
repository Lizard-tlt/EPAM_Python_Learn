"""
Написать функцию расчёта площади тереугольника по формуле Герона и тесты к ней
"""


def query_sides_of_triangle() -> str:
    """
    Запрос сторон тереугольника

    return str
    """

    abc = input("Введите через запятую сторону A, B, C=")
    return abc


def check_sides_of_triangle(sides_of_triangle: str) -> tuple:
    result = tuple([int(i) for i in sides_of_triangle.split(',')])
    assert len(result) == 3, "Треугольник должен иметь 3 стороны."
    return result


def check_length_sides_of_triangle(sides_of_triangle: tuple):
    """
    Проверка длин введённых сторон треугольника
    Сумма двух любых сторон треугольника всегда больше третьей.
    """

    a, b, c = sides_of_triangle
    assert a + b > c, "Сумма двух любых сторон треугольника должна быть больше третьей."
    return True


def square_of_triangle(sides_of_triangle: tuple) -> float:
    """
    Вычисление площади треугольника
    result float Площадь тереугольника
    """

    check_length_sides_of_triangle(sides_of_triangle)

    a, b, c = sides_of_triangle
    # Вычисление полупериметра
    p = (a + b + c) / 2
    square = pow((p * (p - a) * (p - b) * (p - c)), 1 / 2)
    return square


def calc_square_of_triangle() -> float:
    """
    Вычисление площади треугольнока с запросом и проверкой входящих параметров
    result float Площадь тереугольника
    """
    sides_str = query_sides_of_triangle()
    sides = check_sides_of_triangle(sides_str)
    return square_of_triangle(sides)


if __name__ == '__main__':
    print(calc_square_of_triangle())
