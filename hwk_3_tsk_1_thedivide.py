# Реализовать функцию деления с учетом ошибки деления на 0.

# Возвращает частное от деления
# x -  делимое,
# y - делитель по умолчанию

def my_div(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:  # исключение с делением на 0
        return "Zero division Error!"
    except ValueError:  # исключение с типом данных
        return "Wrong Data! Enter the numbers!"


x = input("Enter x ")
y = input("Enter y ")
print(my_div(x, y))
