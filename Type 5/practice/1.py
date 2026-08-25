# https://education.yandex.ru/ege/inf/task/32e89d37-e49f-4eee-bc53-877209c7b4ce
from itertools import *


ls = list(map(lambda x: ''.join(x), product('123456789', repeat=4)))
print(ls)

def f(l):
    a = []
    b = []
    for i in l:
        if int(i) % 2 == 0:
            a.append(int(i))
        else:
            b.append(int(i))
    return len(a) == len(b), a, b

for i in ls:
    s = f(i)
    if not s[0]:
        continue
    if sum(s[1]) == 4 and sum(s[2]) == 6:
        print(i)
        break


