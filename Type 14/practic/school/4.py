def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 17) if j % 17 < 10 else 'ABCDEFG'[j % 17 - 10]
        j //= 17
    return s[::-1]

d = 17**5 + 85**8 - 10
print(h(d).count('G'))