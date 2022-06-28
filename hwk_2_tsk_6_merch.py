"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
 — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество,
единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.

"""

shop_price = []
cat_numr = len(shop_price) + 1
n = int(input("Сколько номеров заводим, шеф?: "))

for _ in range(n):
    name = input("Имя товара: ")
    price = input("Цена товара: ")
    qnty = input("Количество его: ")
    ummt = input("Единицы измерения: ")
    ftrs = {'Наименование': name, 'Цена': price, 'Кол-во': qnty, 'Ед-изм': ummt}
    shop_price.append((cat_numr, ftrs))
    cat_numr += 1

print('\n'.join(map(str, shop_price)))

shop_analytics = {'Наименование': [], 'Цена': [], 'Кол-во': [], 'Ед-изм': []}
for s in shop_price:
    shop_analytics['Наименование'].append(s[1]['Наименование'])
    shop_analytics['Цена'].append(s[1]['Цена'])
    shop_analytics['Кол-во'].append(s[1]['Кол-во'])
    if s[1]['Ед-изм'] not in shop_analytics['Ед-изм']:
        shop_analytics['Ед-изм'].append(s[1]['Ед-изм'])

print(shop_analytics)
