"""

Функция принимает 3 позиц. аргумента и суммирует 2 наибольших

"""
def max_summ(*args):
    return sum(args) - min(args)

x = int(input('enter x '))
y = int(input('enter y '))
z = int(input('enter z '))

print(max_summ(x, y, z))
