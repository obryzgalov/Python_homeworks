def sum_list():
    s = 0
    while True:
        inp_list = input('Введите числа через пробел (q- выход): ').split()
        if 'q' in inp_list:
            inp_list.remove('q')
            try:
                for i in inp_list:
                    y = 0
                    if i.isdigit():
                        y += i
                    s += y
            except ValueError:
                print('Вводите целые числа!')
            break
        else:
            number_list = list(map(int, inp_list))
            s += sum(number_list)
            print('Сумма равна:', s)
    print('Итоговая сумма:', s)


print(sum_list())
