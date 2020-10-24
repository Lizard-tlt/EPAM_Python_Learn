"""
Тестирование через unittest
"""

import builtins
import mock
from io import StringIO
import unittest

import Test10 as Sqr


class MyTestCase(unittest.TestCase):
    """
    Проверка на допустимую длину сторон теругольника
    """
    def test_check_length_sides_of_triangle_non_positive(self):
        with self.assertRaises(AssertionError) as raised_exception:
            Sqr.check_length_sides_of_triangle((2, 3, 13))
            self.assertEqual(raised_exception.exception.args[0], "Сумма двух любых сторон треугольника должна быть "
                                                                 "больше третьей.")
    """
    Проверка на количество введённых сторон треугольника
    """
    def test_check_count_sides_of_triangle_non_positive(self):
        with self.assertRaises(AssertionError) as raised_exception:
            Sqr.check_sides_of_triangle("2,3")
            self.assertEqual(raised_exception.exception.args[0], "Треугольник должен иметь 3 стороны.")

    """
    Проверка на тип сторон треугольника
    """
    def test_check_type_sides_of_triangle_non_positive(self):
        with self.assertRaises(ValueError) as raised_exception:
            Sqr.check_sides_of_triangle("2,3,w")
            self.assertEqual(raised_exception.exception.args[0], "invalid literal for int() with base 10: 'w'")

    def test_check_length_sides_of_triangle_positive(self):
        """
        Проверка на допустимую длину сторон теругольника
        """
        result = Sqr.check_length_sides_of_triangle((11, 12, 13))
        self.assertEqual(result, True)

    def test_square_of_triangle_positive(self):
        """
        Проверка на правильность расчёта площади треугольника
        """
        result = Sqr.square_of_triangle((12, 13, 14))
        self.assertEqual(result, 72.30793524918272)

    def test_square_of_triangle_non_positive(self):
        """
        Проверка на корректность ввода длинн сторон треугольника
        """
        with self.assertRaises(AssertionError) as raised_exception:
            Sqr.square_of_triangle((3, 4, 8))
            self.assertEqual(raised_exception.exception.args[0], "Сумма двух любых сторон треугольника должна быть "
                                                                 "больше третьей.")

    def test_input_positive(self):
        """
        Проверка на корректность пользовательского ввода
        """
        with mock.patch.object(builtins, 'input', lambda _: "1,2,3"):
            abc = Sqr.query_sides_of_triangle()
            self.assertEqual("1,2,3", abc)

    def test_check_sides_of_triangle_positive(self):
        """
        Проверка на тип введённых данных
        """
        self.assertTupleEqual((11, 12, 13), Sqr.check_sides_of_triangle("11, 12, 13"))

    def test_check_sides_of_triangle_non_positive(self):
        """
        Проверка на тип введённых данных
        """
        with self.assertRaises(ValueError) as raised_exception:
            self.assertEqual((11, 12, 13), Sqr.check_sides_of_triangle("11.1, 12, 13"))
            self.assertEqual(raised_exception.exception.args[0], "invalid literal for int() with base 10: '11.1'")

    def test_calc_square_of_triangle(self):
        """
        Проверка полного расчёта с вводом и промежуточными проверками
        """
        with mock.patch.object(builtins, 'input', lambda _: "22,23,34"):
            with mock.patch('sys.stdout', new=StringIO()) as fakeOutput:
                print(Sqr.calc_square_of_triangle())
                self.assertEqual(fakeOutput.getvalue().strip(), '250.46144912940196')


if __name__ == '__main__':
    unittest.main()
