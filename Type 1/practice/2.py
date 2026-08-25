# https://education.yandex.ru/ege/inf/task/9d2228f8-6ca3-4819-9708-af4bc8555701
from itertools import permutations


tab = '27 1579 67 68 29 3478 123689 467 257'.split()
pic = 'eh eb hb hd ab ad bd cd cg fd fg fi ig gd'.split()

print(*range(1, 10), sep=' | ')

for i in permutations('abcdefghi'):
    if all(str(i.index(x) + 1) in tab[i.index(y)] for x, y in pic):
        print(*i, sep=' | ')

# 45