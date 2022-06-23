"""
Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень (pow())

вариант решения только циклами (без pow() и **)
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
        y =-1*y # перевод обратно в + значение (иначе for range не запустится)
        for s in range(y):
            s = 1/(x * x)
            return s

while True:
    print ('enter values (q for exit)')
    x = (input('enter float x >=0: '))
    y = (input('enter int y < 0: '))
    if x == 'q' or y == 'q':
        break
    else:
        print(my_pow(x, y))
