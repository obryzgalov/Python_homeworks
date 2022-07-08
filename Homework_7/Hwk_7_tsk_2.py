# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    total_cons = 0  # суммарный расход ткани

    @abstractmethod
    def sewing(self):
        """
        подставить формулу
        """
        pass


class Suit(Clothes):
    s_count = 0

    def __init__(self, height):
        self.height = height
        Suit.s_count += 1  # Просто счетчик. Крсивое

    @property
    def sewing(self):
        suit_cons = self.height * 2 + 0.3
        Clothes.total_cons += suit_cons
        return float(suit_cons)

    def __str__(self):
        return f"Расход ткани на костюм № {Suit.s_count} размером {self.height} равен {self.sewing}"


class Coat(Clothes):
    c_count = 0

    def __init__(self, size):
        self.size = size
        Coat.c_count += 1

    @property
    def sewing(self):
        coat_cons = self.size / 6.5 + 0.5
        Clothes.total_cons += coat_cons
        return float(coat_cons)

    def __str__(self):
        return f"Расход ткани на пальто № {Coat.c_count} размером {self.size} равен {self.sewing}"


suit_1 = Suit(7)
print(suit_1)
coat_1 = Coat(46)
print(coat_1)
print("Cуммарный расход ткани", '{:4.2f}'.format(Clothes.total_cons))

#  Я прикрутил ABC, но не понял сути: задача прекрасно решается без них. Просто МЕНЬШЕ ИМЕН МЕТОДОВ?
