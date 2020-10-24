# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти —слово Buzz.
# Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz

def get_wold(num):
    result = ""
    if num % 15 == 0:
        result = "FizzBuzz"
    elif num % 5 == 0:
        result = "Buzz"
    elif num % 3 == 0:
        result = "Fizz"
    return f"{num} {result}"


def print_result():
    print('\n'.join(map(str, [get_wold(i) for i in range(1, 101)])))


print_result()
