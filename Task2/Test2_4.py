# Напишите программу, принимающую 2 числа и выводящую НОД.

def print_result(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(a + b)


def input_data():
    print('Определение НОД')
    d1 = input("Введите число x: ")
    d2 = input("Введите число b: ")
    return int(d1), int(d2)


digit1, digit2 = input_data()
print_result(digit1, digit2)
