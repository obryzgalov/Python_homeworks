"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для
проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

"""

my_list = [12, 04.61, 'Gagarin', True, 'Help', 1111, 14, 45, 98]
print("'my_list' has", "0-", (len(my_list) - 1), "indices")
print(my_list)

while True:
    my_ind = input("Enter element's index (Q for quit): ")
    if my_ind == "Q":
        break
    else:
        my_ind = int(my_ind)
        print((my_ind), "|", (my_list[my_ind]), "|", type(my_list[my_ind]))
