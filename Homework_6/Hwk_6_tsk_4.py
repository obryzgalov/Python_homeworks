class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        print(f"my {self.color} {self.name}")

    def go(self):
        print('go')

    def direction(self):
        dir = input('Where to go?...')
        if dir == 1:
            print('turning left')
        elif dir == 2:
            print('turning right')

    def stop(self):
        print('stop')

    def police_check(self):
        if self.is_police == True:
            print('Thats police, run!')
        else:
            print('chillout, bro')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'{self.speed} is too fast!')
        else:
            print(f"current speed is {self.speed}")


class SportCar(Car):
    """just car"""


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'{self.speed} is too fast!')
        else:
            print(f"current speed is {self.speed}")


class PoliceCar(Car):
    is_police = True


car_1 = TownCar(70, 'red', 'mini')
car_1.go()
car_1.show_speed()
car_1.direction()
car_1.stop()

car_2 = SportCar(200, 'black', 'maseratti')
car_2.go()
car_2.stop()
car_2.police_check()
print(f'{car_2.speed} km/h')

car_3 = PoliceCar(100, 'none', 'police')
car_3.police_check()
