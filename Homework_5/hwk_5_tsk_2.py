# не думаю, что нужен комментарий
with open ('task2file.txt', 'w+', encoding='UTF-8') as f:
    ln = ''
    while True:
        ln = input('enter data or '' for exit: ')
        if ln != '':
            f.write(f"{ln}\n")
        else:
            break

with open ('task2file.txt', 'r', encoding='UTF-8') as f:
    l_num = 0
    for line in f:
        l_num += 1
        print(f"there are {(len(line) - 1)} symbols in line {l_num}")
    print(f"there are {l_num} lines in the file")
