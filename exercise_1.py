# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


from random import randint


class Matrix:                               # может складывать матрицы любого порядка,
    def __init__(self, lines, columns):     # но нет проверки на совпадение порядков
        self.lines = lines
        self.columns = columns
        self.matrix = []
        i = 1
        while i <= self.lines:
            self.matrix.append(input(f'Введите {i} строку через пробел: ').split())
            if len(self.matrix[i - 1]) == self.columns:
                i += 1
            else:
                self.matrix.pop()
                print(f'В строке должно быть {self.columns} элемента!')

    def __str__(self):
        return '\n'.join(['\t'.join([j for j in i]) for i in self.matrix])

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        result_matrix = [[randint(-1, 1) for j in range(self.columns)] for i in range(self.lines)]
        for i in range(self.lines):
            for j in range(self.columns):
                result_matrix[i][j] = int(self.matrix[i][j]) + int(other[i][j])
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in result_matrix])


a = Matrix(2, 2)
z = Matrix(2, 2)
q = a + z
print(q)
