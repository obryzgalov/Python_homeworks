import json

res = dict()
av_profit = 0
n = 0
with open('file7.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        name, type, inc, cost =line.split()
        profit = int(inc) - int(cost)
        if profit >= 0:
            av_profit += profit
            n += 1
        res[name] = profit
av_profit /= n
with open('json7.json', 'w', encoding='UTF-8') as f:
    json.dump([res, {'av_profit': av_profit}], f, ensure_ascii=False)
