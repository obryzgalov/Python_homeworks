from random import randint

with open('newfile5.txt', 'w', encoding='UTF-8') as f:
    r_list = [randint(1, 50) for i in range(75)]
    f.write(' '.join(map(str, r_list)))

with open('newfile5.txt', 'r', encoding='UTF-8') as f1:
    n = [int(j) for j in f1.read().split()]
    print(sum(n))
