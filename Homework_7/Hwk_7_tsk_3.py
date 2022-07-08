class Cell:
    def __init__(self, mesh, order):
        self.order = order  # число ячеек в ряду
        self.mesh = mesh  # число ячеек

    def make_order(self):
        for _ in range(self.mesh // self.order):  # печать структуры клетки в диапазоне числа рядов
            print("* " * self.order)  # печатаем целые строки
        print("* " * (self.mesh % self.order))  # добавляем остаток
        print(f"Cell has {self.mesh} meshes --------------------------------------------------------------------")
        # красивость

    def __add__(self, other):
        return Cell(self.mesh + other.mesh, ((self.order + other.order) // 2))

    def __sub__(self, other):
        if self.mesh - other.mesh > 0:
            if self.order - other.order > 0:
                return Cell(self.mesh - other.mesh, self.order - other.order)
            else:
                return Cell(self.mesh - other.mesh, other.order - self.mesh)
        else:
            raise ValueError("Клетку пожрало. Помойте чашку Петри")
        # в вычитании зашита проверка на длину рядов: вычтется всегда из бОльшего.
        # главное, чтобы общее число ячеек было больше у первого аргумента (мне здесь так захотелось)))
        # очень криво, но по- другому пока не умею.

    def __mul__(self, other):
        return Cell(self.mesh * other.mesh, (self.order * other.order) // 2)

    def __truediv__(self, other):
        if self.order // other.order != 0:
            return Cell(self.mesh // other.mesh, self.order // other.order)
        else:
            raise ValueError("Клетку пожрало. Помойте чашку Петри")


cell_1 = Cell(55, 8)
cell_2 = Cell(70, 19)
cell_1.make_order()
cell_2.make_order()
(cell_1 + cell_2).make_order()
(cell_2 - cell_1).make_order()
(cell_1 * cell_2).make_order()
(cell_2 / cell_1).make_order()

#  ВООБЩЕ- ВООБЩЕ САМ РЕШИЛ. ОТ 1 ДО 44 СТРОКИ. МОЗГИ КИПЯТ))
