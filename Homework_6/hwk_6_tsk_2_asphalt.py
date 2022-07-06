std_mass = 25  # константа массы 1 кв. м. толщиной 1 см.


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_req(self):
        thickness = int(input('Введите толщину полотна в см: '))
        print(f"Необходимо {self._length * self._width * std_mass * thickness} кг"
              f" асфальта")


l = int(input('Введите длинну полотна: '))
w = int(input('Введите ширину полотна: '))

road_1 = Road(l, w)
road_1.asphalt_req()
# кажется работает
