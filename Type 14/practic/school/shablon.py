def h(j: int, n: int):
    s = ''
    while j > 0:
        s += str(j % n) if j % n < 10 else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[j % n - 10]
        j //= n
    return s[::-1]