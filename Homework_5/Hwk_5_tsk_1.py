f = open('task1file.dat', 'w+', encoding='UTF-8')
line = ''
while True:
    line = input('enter data or '' for exit: ')
    if line != '':
        f.write(f"{line}\n")
    else:
        break

f.close()
