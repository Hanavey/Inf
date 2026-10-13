def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 14) if j % 14 < 10 else 'ABCD'[j % 14 - 10]
        j //= 14
    return s[::-1]

d = 7**2 + 49**4 - 21
print(h(d).count('A') + h(d).count('0'))
