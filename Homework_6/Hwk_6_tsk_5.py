class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('А теперь рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('А теперь штрихуем маркером')


parent = Stationery('title')
parent.draw()
print('-----------')
pen = Pen('pen')
pen.draw()
print('-----------')
pencil = Pencil('Pencil')
pencil.draw()
print('-----------')
handle = Handle('handle')
handle.draw()

"""
На мой взгляд, никакой вызов super или нового инициализатора в подклассах не нужен:
это лишь увеличит число строк.

"""
