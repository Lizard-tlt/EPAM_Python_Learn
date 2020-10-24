# Тема 2 Задание 1
# Написать программу, принимающую на вход 2 дроби (вида a/b)
# и выводящую результат сложения дробей“Result is XX/XX”

from fractions import Fraction


def print_formula_result(fr_operands):
    """
    Сумма дробей
    :param fr_operands: Кортеж операндов
    :return:
    """
    print(f'Result is {sum([Fraction(item) for item in fr_operands])}')



def input_data():
    fr_1 = input("Дробь 1: ")
    fr_2 = input("Дробь 2: ")
    return fr_1, fr_2


op = input_data()
print_formula_result(op)
