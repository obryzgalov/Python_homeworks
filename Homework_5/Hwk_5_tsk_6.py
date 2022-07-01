import re

name = []
timing = []
with open('task6file.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        name.append(line.split(" ")[0])
        timing.append(sum(map(int, (re.findall('\d+', line)))))
    d = {}
    for i in range(0, len(name)):
        d[name[i]] = timing[i]
print(d)
