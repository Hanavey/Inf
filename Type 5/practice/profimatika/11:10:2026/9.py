def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 3)
        j //= 3
    return s[::-1]


def f(n: int):
    s = h(n)
    if n % 3 == 0:
        s += s[-2::1]
    else:
        k = 0
        for i in s:
            k += int(i)
        s += h(k)
    return int(s, 3)

l = []
for i in range(1, 10000):
    if f(i) > 300 and f(i) % 2 == 0:
        l.append(f(i))
print(min(l))
