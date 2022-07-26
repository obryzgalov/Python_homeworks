class MyError(Exception):
    def __inint__(self, a, b):
        self.a = a
        self.b = b


a = int(input('Делимое: '))
b = int(input('Делитель: '))

try:
    if b == 0:
        raise MyError('Деление на 0')
except MyError as merr:
    print(merr)
else:
    print(a / b)
