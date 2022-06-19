# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

seasons_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
                'Декабрь']
seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
                10: 'Осень', 11: 'Осень', 12: 'Зима'}
while True:
    i = (input("Enter month's number (Q for exit): "))
    if i == "Q":
        break
    elif i.isdigit() == False or int(i) <= 0 or int(i) > 12:
        print("Input incorrect! Try again.")
    else:
        i = int(i)
        print((seasons_list[i - 1]), "- это", (seasons_dict[i]))
