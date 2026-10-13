def f(n: int):
    s = bin(n)[2:]
    if s[0] == '0':
        s = '10' + s
    else:
        s = '1' + s + '01'
    return int(s, 2)

for i in range(10000):
    if f(i) >= 250:
        print(i)
        break
