def f(n: int):
    s = bin(n)[2:]
    if s[0] == '0':
        s = '10' + s
    else:
        s = '1' + s + '01'
    return int(s, 2)

l = []
for i in range(16):
    l.append(f(i))
print(max(l))
