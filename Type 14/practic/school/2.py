def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 7)
        j //= 7
    return s[::-1]

d = 7**103 + 6 * 7**104 - 3 * 7**57 + 98
k = 0
for i in h(d):
    k += int(i)
print(k)
