# Норма сна человека
name = input ("Введите Ваше имя: ")
print("желательное время сна составляет от 6 до 9 часов в сутки")
minsleep = 6
maxsleep = 9
sleeptime = int(input("Введите время сна фактически: "))

if minsleep <= sleeptime <= maxsleep :
    print ('{}, Вы высыпаетесь'. format(name))

elif sleeptime < minsleep :
    print ('{}, Вы спите мало'. format(name))

else :
    print ('{}, Вы спите слишком много'. format(name))

print('\n')
a = input('put a: ')
b = input('put b: ')
c = a+b
print ('%s ...surprise!, m.....r!, this is string!,' % c)

print('\n\nАнализ парка техники')
trucksnum = int(input('\nВведите количество тяжелых грузовиков: '))
lcvnum = int(input('Введите количество LCV: '))
carnum = int(input('Введите количество легковых а/м: '))

totalnum = trucksnum + lcvnum + carnum
lcv4ht = round(((lcvnum*100)/trucksnum), 2)
car4total = round(((carnum*100)/totalnum), 2)

print ('\nОбщий штат составляет {} ед.' .format(totalnum))
print ('Соотношение LCV к грузовикам составляет {} %.' .format(lcv4ht))
print ('Соотношение легковых к штату составляет {} %.' .format(car4total))
