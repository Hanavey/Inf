def f(n: int):
    s = bin(n)[2:]
    k = 0
    for i in s:
        if i == '1':
            k += 1
    if k % 2 == 0:
        s += '0'
    else:
        s += '1'
    return int(s, 2)

print(f(22))
