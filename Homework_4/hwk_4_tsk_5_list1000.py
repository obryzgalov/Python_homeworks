"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce
from operator import mul
import time
start_time = time.time()

result = reduce(mul, (n for n in range(100, 1001, 2) if n % 2 == 0))
print(result)
print("--- %s seconds ---" % (time.time() - start_time))

# использовано перемножение результатов фильтрации функцией mul
#я не списывал! stack overflow((

"""
def mul_list(n1, n2):
   return n1 * n2

list = [x for x in range (100, 1001, 2)]
print(reduce(mul_list, list))
"""

#Второй вариант в статистике запусков чуть более стабилен по времени, и, судя по порядку операций,
# будет лучше работать с большими объемами, но первый как-то красивее))
# ни один не занимает более 0,00025 сек.