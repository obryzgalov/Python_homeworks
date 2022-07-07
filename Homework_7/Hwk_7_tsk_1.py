# в Python ведь нет матриц как таковых (мат. объектов): все это просто списки и их представление ??

class Matrix:
    def __init__(self, mat_list):
        self.mat_list = mat_list
        for row in self.mat_list[:-1]:
            if len(row) == len(self.mat_list[self.mat_list.index(row) + 1]):
                print("Следуй за кроликом")
                print("----------------------")
            else:
                raise ValueError('Кривая бабка')

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.mat_list)
        # а я тут все равно хотел принтом: он понятнее, но на Stack нашел вот это:
        # "представить каждый эл. списка как ряд с новой строки, отделяя элементы рядов отступом"
        # красиво, но попробуй запомни

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(*x)] for x in zip(self.mat_list, other.mat_list)])
        #вариант с распаковкой списков из кортежа. думаю из-за этого неравная матрица просто считается по меньшей


mat_1 = Matrix([[2, 3, 5, 1], [4, 5, 6, 1], [1, 1, 1, 1]])
print(mat_1)
mat_2 = Matrix([[7, 8, 1], [9, 10, 7]])
print(mat_2)
print(mat_1 + mat_2)
