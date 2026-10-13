def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 15) if j % 15 < 10 else '№#@$*'[j % 15 - 10]
        j //= 15
    return s[::-1]

d = 100**2 + 625**25 + 5**100
print(h(d).count('@'))
