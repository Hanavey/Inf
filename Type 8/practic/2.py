# https://education.yandex.ru/ege/inf/task/7bd50bb2-d36b-496b-b363-393b9ac6cb4b
from itertools import permutations


k = 0
for i in set(permutations('НОСОЧЕЧКИ')):
    s = ''.join(i)
    if all([s[i] in 'НСЧК' for i in (0, 2, 4, 6, 8)]) and all([s[i] in 'ОЕИ' for i in (1, 3, 5, 7)]):
        k += 1
print(k)