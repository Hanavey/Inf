def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 9)
        j //= 9
    return s[::-1]

def f(x: int):
    d = 81**20 - 9**x + 50
    k = 0
    for i in str(h(d)):
        k += int(i)
    return k

for l in range(10000):
    if f(l) == 138:
        print(l)
        break
