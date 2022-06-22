"""
    Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя,
фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
именованные аргументы.
    Осуществить вывод данных о пользователе одной строкой.

"""


def user_data(**kwargs):
    return ' | '.join(kwargs.values()) #вывод строки с присоединением через пробел

print(user_data(name=input('Name: '), surname=input('S/name: '), birthyear=input('birthyear: '),
              city=input('city: '), email=input('email: '), tel=input('tel: ')))


