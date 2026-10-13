def f(n: int):
    if '0' in str(n):
        return 0
    e = ''
    o = ''
    for i in str(n):
        if int(i) % 2 == 0:
            e += i
        else:
            o += i
    if len(e) != len(o):
        return 0
    return int(str(int(e[0]) + int(e[1])) + str(int(o[0]) + int(o[1])))


for i in range(1000, 10000):
    if f(i) == 68:
        print(i)
        break
