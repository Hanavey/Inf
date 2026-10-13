def f(n):
    s = bin(n)[2:]
    h = 0
    for i in s:
        h += int(i)
    if h % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    return int(s, 2)

for i in range(10000):
    if f(i) > 90:
        print(i)
        break
