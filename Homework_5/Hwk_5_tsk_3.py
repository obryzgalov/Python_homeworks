import numpy

with open('task3file.txt', 'r', encoding='UTF-8') as f:
    s = []
    small_s = []
    l_num = 0
    for line in f:
        l_num += 1
        name, n = (i for i in line.split())
        n = float(n)
        try:
            s.append(float(n))
            if float(n) < 20000.00:
                small_s.append(name)
        except ValueError:
            pass
    print(f"Средний оклад сотрудников: {round((numpy.average(s)), 2)} руб.")
    print(f"Оклады меньше 20 тыс. руб. имеют {small_s}")
