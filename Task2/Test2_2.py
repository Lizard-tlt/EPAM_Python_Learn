# Тема 2 Задание 2
# Написать программу, ожидающую ввод числа,
# возводящую его в 13 степень и выводящую на консоль

def print_result(val):
    result = float(val) ** 13
    print(f'Result is {result}')


def input_data():
    return input("Введите число: ")


value = input_data()
print_result(value)
