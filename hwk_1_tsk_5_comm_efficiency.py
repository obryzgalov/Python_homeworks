# sales - выручка
# costs - издержки
# revenue - прибыль
# employees - штат сотрудников
# profit - рентабельность
# revper1 - прибыль в расчете на одного сотрудника

sales = float(input('введите выручку с продаж в тыс. руб.:'))
costs = float(input('введите издержки в тыс. руб.:'))
revenue = sales - costs
if revenue < 0:
    print ('Фирма работает с убытком: ', (revenue), 'руб.', 'Увольте Васю!')
else:
    print ('Фирма работает с прибылью: ', (revenue), 'руб.')
    profit = (revenue/sales) * 100
    print ('Рентабельность составляет {:.2f} %'.format(profit))
    employees = int(input('Сколько человек у Вас работает?: '))
    revper1 = revenue/employees
    print ('Прибыль в расчете на одного сотрудника составляет {:.2f}'.format(revper1), 'руб')
