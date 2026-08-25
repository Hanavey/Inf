# https://education.yandex.ru/ege/inf/task/af4e8a95-d5b5-4698-be21-428478bda513
from itertools import permutations


ls = list(permutations([i for i in range(999, 99, -1)], 2))
print(ls)

def f(l):
    k = str(l[0] % 10 + l[1] % 10) + str(l[0] // 100 + l[1] // 100) + str(l[0] // 10 % 10 + l[1] // 10 % 10)
    d = int(k)
    return str(d // 1000 % 10) + str(d // 100 % 10) + str(d // 10 % 10), k

for i in ls:
    if f(i)[0] == '002':
        print(i, f(i), end='\n')
