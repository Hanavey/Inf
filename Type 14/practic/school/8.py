def f(x):
    d = 64**12 - 8**14 + x
    return oct(d)[2:].count('7') == 12 and oct(d)[2:].count('1') == 1

for x in range(10000):
    if f(x):
        print(x)
        break
