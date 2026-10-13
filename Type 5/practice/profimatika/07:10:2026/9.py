def f(n: int):
    s = bin(n)[2:]
    if s[-1] == '0':
        s = '1' + s + '1'
    else:
        s += '10'
    return int(s, 2)

for i in range(1, 10000):
    if f(i) > 250:
        print(i)
        break