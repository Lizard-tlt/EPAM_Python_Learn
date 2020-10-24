# Тема 2 Задание 3
# Вычисление формулы


def print_result(x, b):
    result = (12 * x + 25 * b) / (1 + x ** 2 ** b)
    print(f'Result is {result}')


def input_data():
    x = input("Введите число x: ")
    b = input("Введите число b: ")
    return float(x), float(b)


x, b = input_data()
print_result(x, b)


