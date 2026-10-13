def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 3)
        j //= 3
    return s[::-1]


def f(n: int):
    s = h(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s += h((n % 3) * 4)
    return int(s, 3)

l = []
for i in range(10000):
    if f(i) < 200:
        l.append(i)
print(max(l))