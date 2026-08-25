# https://education.yandex.ru/ege/inf/task/5e1d8be3-465b-4e31-a70d-78cbc1ee8e60
print('u | w | x | y | F')
for u in range(2):
    for w in range(2):
        for x in range(2):
            for y in range(2):
                f = (x <= w) <= (u <= y)
                if not f:
                    print(u, w, x, y, f, sep=' | ')
# xuwy