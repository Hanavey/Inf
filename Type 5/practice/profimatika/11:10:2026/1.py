def f(n: int):
    s = bin(n)[2:]
    if s[-1] == '0':
        s += '01'
    else:
        s = '1' + s + '1'
    return int(s, 2)

for i in range(1, 10000):
    if f(i) > 200:
        print(i)
        break
