# https://education.yandex.ru/ege/inf/task/a679736e-0112-4e42-8ff1-59a7c47ca583
from itertools import permutations


tab = "4 46 47 123567 47 24 345".split()
pic = "cd cb db eb ef fb fg gb ab".split()

print(*range(1, 8), sep=' | ')

for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in tab[i.index(y)] for x, y in pic):
        print(*i, sep=' | ')

# 20 + 22 = 42