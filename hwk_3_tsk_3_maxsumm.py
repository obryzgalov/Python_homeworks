"""

Функция принимает 3 позиц. аргумента и суммирует 2 наибольших

"""


def max_summ(*args):
        return sum(args) - min(args)

x = float(input('enter x '))
y = float(input('enter y '))
z = float(input('enter z '))

print(max_summ(x, y, z))
