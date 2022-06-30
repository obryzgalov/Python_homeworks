"""
подсчет символов велся без учета символа переноса строки

"""

f = open('task2file.txt', 'w+', encoding='UTF-8')
ln = ''
while True:
    ln = input('enter data or '' for exit: ')
    if ln != '':
        f.write(f"{ln}\n")
    else:
        break
f.close()

f = open('task2file.txt', 'w+', encoding='UTF-8')
l_num = 0
for line in f:
    if '\n' in line:
        l_num += 1
        print(f"there are {(len(line) - 1)} symbols in line {l_num}")
print(f"there are {l_num} lines in the file")
f.close()
