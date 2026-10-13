def f(n: int):
    s = bin(n)[2:]
    h = 0
    for i in s:
        h += int(i)
    s += str(h % 2)
    h = 0
    for i in s:
        h += int(i)
    s += str(h % 2)
    return int(s, 2)

for i in range(10000):
    if f(i) > 500:
        print(i)
        break
