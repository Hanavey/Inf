# https://education.yandex.ru/ege/inf/task/71166ece-bd5d-48a1-93a5-cbef298bcff7
print('w | x | y | z | F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not (w == y)) and (z <= w) and (not x)
                if f:
                    print(w, x, y, z, f, sep=' | ')
# zxwy