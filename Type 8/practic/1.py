# https://education.yandex.ru/ege/inf/task/c6167029-d804-421e-865f-aa96e4c98ecd
from itertools import product


k = 0
for i in product('АВОРТ', repeat=6):
    k += 1
    if ''.join(i) == 'ВОРОТА':
        print(k)
        break
