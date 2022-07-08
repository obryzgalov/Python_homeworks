# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
class Clothes:
    total_cons = 0  # суммарный расход ткани


class Suit(Clothes):
    s_count = 0

    def __init__(self, height):
        self.height = height
        Suit.s_count += 1  # Просто счетчик. Крсивое

    def sewing_suit(self):
        suit_cons = self.height * 2 + 0.3
        Clothes.total_cons += suit_cons
        print(f"Расход ткани на костюм № {Suit.s_count} с ростом {self.height} равен {suit_cons}")


class Coat(Clothes):
    c_count = 0

    def __init__(self, size):
        self.size = size
        Coat.c_count += 1

    def sewing_coat(self):
        coat_cons = round((self.size / 6.5 + 0.5), 2)
        Clothes.total_cons += coat_cons
        print(f"Расход ткани на пальто № {Coat.c_count} размером {self.size} равен {coat_cons}")


suit_1 = Suit(7)
suit_1.sewing_suit()
suit_2 = Suit(11)
suit_2.sewing_suit()
coat_1 = Coat(46)
coat_1.sewing_coat()
coat_2 = Coat(52)
coat_2.sewing_coat()
coat_3 = Coat(27)
coat_3.sewing_coat()

print(f"Cуммарный расход ткани {Clothes.total_cons}")
