def f(n: int):
    s = bin(n)[2:]
    if s[-1] == '0':
        s = '11' + s + '11'
    else:
        s = '1' + s + '00'
    return int(s, 2)

print(min([f(i) if f(i) > 200 else 100000 for i in range(100000)]))
