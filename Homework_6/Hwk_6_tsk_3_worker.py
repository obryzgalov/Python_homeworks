class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        # значения из словаря отображаются в скобках выше? дошел опытным путем. интересно...


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}, \n{self.position}')

    def get_total_income(self):
        print(sum(self._income.values()), '\nBurn the Heretic!')


man = Position('Horus', 'Lupercal', 'gallera slave', 10, 2)
man.get_full_name()
man.get_total_income()
