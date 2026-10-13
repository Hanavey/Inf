def f(n: int):
    s = bin(n)[2:]
    if s[-1] == '0':
        s = '10' + s
    else:
        s = '1' + s + '01'
    return int(s, 2)

l = []
for i in range(15):
    l.append(f(i))

print(max(l))