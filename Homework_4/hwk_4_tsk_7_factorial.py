"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом:
for el in fact(n). Она отвечает за получение факториала числа.
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""


def f_gen(n):
    f_number = 1
    if n == 0:
        yield f'{n}! = 1'
    for i in range(1, n + 1):
        f_number *= i
        yield f'{i}! = {f_number}'


for el in f_gen(int(input('factotrial number '))):
    print(el)