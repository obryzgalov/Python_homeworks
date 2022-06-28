"""
Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень (pow())
функция самам проверяет тип введенных данных
"""


def my_pow(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return 'not supported type'
    if x < 0 or y >= 0:
        return 'wrong data'
    else:
        return x ** y


while True:
    print('enter values (q for exit)')
    x = (input('enter float x >=0: '))
    y = (input('enter int y < 0: '))
    if x == 'q' or y == 'q':
        break
    else:
        print(my_pow(x, y))
