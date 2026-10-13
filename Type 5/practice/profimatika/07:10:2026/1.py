def f(n: int):
    s = ''
    while n != 0:
        s += str(n % 4)
        n //= 4
    s = s[::-1].replace('0', '')
    return int(s, 4)


print(f(100))
