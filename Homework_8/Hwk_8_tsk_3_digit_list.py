class MyError(Exception):
    def __inint__(self, num, num_lst):
        self.num = num
        self.num_lst = num_lst


num_lst = []
print('Список сформирован, для выхода и печати введите "stop"')

while True:
    num = input('Введите элемент списка (число): ')
    if num == 'stop':
        print(num_lst)
        break
    try:
        if not num.isdigit():
            raise MyError('"Это не число"')
    except MyError as merr:
        print(merr)
    else:
        num_lst.append(float(num))
