# Создать класс Matrix. Он хранит количество строк и столбцов, элементы целочисленной матрицы. Методы: сумма,
# разность, произведение двух матриц, умножение матрицы на скаляр, транспонирование матрицы, равны ли две матрицы,
# квадратная ли матрица, для квадратной матрицы – проверка симметричности относительно главной (побочной) диагонали.
import random
from tabulate import tabulate


# >>> a = Matrix(2, 2) # generate random matrix
# >>> b = Matrix([[1,2], [3, 4]]) # concreate matrix
# >>> c = a * b
# >>> c
# [[4, 5],
# [6, 7]]
# >>> c.is_squared()
# True

class Matrix(list):
    def __init__(self, *args):
        super().__init__()

        p = args
        """Прроверки самые примитивные. Легко можно завалить..."""
        if isinstance(p, tuple) and len(p) == 2 and type(p[0]) is int:
            random.seed(1)
            self.append([[random.randrange(0, 10) for _ in range(p[1])] for _ in range(p[0])])
        elif isinstance(p[0], list):
            self.append(p[0])
        else:
            raise TypeError('Не верный тип параметроов конструктора!')

        self.size_x = len(self[0][0])
        self.size_y = len(self[0])
        self.matrix = self[0]

    def __str__(self):
        return tabulate(self.matrix, tablefmt="grid")

    @property
    def is_squared(self):
        """Проверка на квадратая-ли мотрица?"""
        return self.size_x == self.size_y

    def transpose(self):
        """Транспонирование матрицы"""
        return Matrix([list(i) for i in list(zip(*self.matrix))])

    @property
    def is_symmetric(self):
        """Матрица симметричная?"""
        if not self.is_squared:
            raise TypeError("Матрица не квадратная!")

        return all(all([self.matrix[y][x] == self.matrix[x][y] for x in range(self.size_x)])
                   for y in range(self.size_y))

    def main_cycle(self, other, func):
        """Общий цикл операций с матрицами
        other: Матрица или скалярное значение
        func: Функция
        """
        return Matrix([[func(self.matrix[i][j], other[0][i][j] if isinstance(other, Matrix) else other)
                        for j in range(self.size_x)] for i in range(self.size_y)])

    def __add__(self, other):
        return self.main_cycle(other, lambda x, y: x + y)

    def __mul__(self, other):
        return self.main_cycle(other, lambda x, y: x * y)

    def __sub__(self, other):
        return self.main_cycle(other, lambda x, y: x - y)

    def __eq__(self, other):
        return all(all([self.matrix[x][y] == other[0][x][y] for x in range(self.size_x)]) for y in range(self.size_y))


def print_result(report_title, val):
    print(f"-------------------------------{report_title}-------------------------------")
    if isinstance(val, bool):
        print(f"Сравненеие матриц = {val}")
    elif isinstance(val, Matrix):
        print(val)


# Проверка на сложение, вычитание, умножение, сравнение
a = Matrix([[11, 71, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[11, 71, 3], [4, 5, 6], [7, 8, 9]])

print_result("Проверка на сложение, вычитание, умножение, сравнение", a - b)
print_result("Проверка на сравнение", a == b)

# Проверка на сложение, вычитание, умножение сo скаляром
print_result("Проверка на сложение, вычитание, умножение сo скаляром", a - 3)

# Проверка на транспонирование
a = Matrix(2, 4)
print_result("Проверка на транспонирование", a)
c = a.transpose()
print(c)
print(c.transpose())

# Проверка на симетричность
a = Matrix([[9, 9, 9], [9, 0, 9], [9, 9, 10]])
print_result("Проверка на симетричность", a.is_symmetric)
print(a)

a = Matrix([[0, 9, 9], [9, 0, 1], [9, 9, 1], [9, 9, 1]])
print_result("Проверка на квадратность", a.is_squared)
print(a)
