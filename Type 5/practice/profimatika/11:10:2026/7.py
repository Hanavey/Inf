def f(n: int):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-2::1]
    else:
        s += bin((n % 3) * 3)[2:]
    return int(s, 2)

print(min([f(i) if f(i) >= 300 else 10000 for i in range(10000)]))