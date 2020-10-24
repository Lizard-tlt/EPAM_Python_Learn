# Задание 6.1 - Prop descriptor

# Написать генератор, сходный по функционалу со встроенной функцией zip.
# Он обходит по кругу переданные ему в аргументах итерируемые объекты, выдавая за один проход по одному элементу с каждого.
# • Число принимаемых аргументов может быть произвольным
# • При реализации нельзя использовать zip или itertools
# • Отработавшие итераторы должны исключаться из цикла
# обхода (в этом будет заключаться отличие от zip)
# Пример использования:?
#
# ```python
# def myzip(*args):
#     pass # TODO: your code here
#
# >>> list(myzip(['A', 'B', 'C'], [1, 2, 3]))
# ['A', 1, 'B', 2, 'C', 3]
# >>> list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3)))
# ['!', 'A', 1, 'B', 2, 'C', 'D']


def myzip(*args):
    for i in range(max([len(i) for i in args])):
        for arr_num in range(len(args)):
            if len(args[arr_num]) > i:
                yield args[arr_num][i]


print(list(myzip(['A', 'B', 'C'], [1, 2, 3])))

print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3))))
