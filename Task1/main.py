from fractions import Fraction


def print_formula_result():
    """
    :return:
    """
    x = (2 ** 12 + 4 * 6) / (2 ** Fraction("3/8"))
    print(f'результат x = {x}')


if __name__ == '__main__':
    print_formula_result()
