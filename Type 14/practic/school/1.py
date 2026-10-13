def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 7)
        j //= 7
    return s[::-1]

d = 7**103 + 20 * 7**204 + - 3 * 7**57 + 97
print(h(d).count('6'))
