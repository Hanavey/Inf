def f(n: int):
    s = bin(n)[2:]
    if s[-1] == 1:
        s = '10' + s[:-2] + '01'
    else:
        s = '11' + s[2:] + '1'
    return int(s, 2)

l = []
for i in range(50, 100000):
    l.append(f(i))

print(min(l))
