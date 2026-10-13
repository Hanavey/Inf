def h(j: int):
    s = ''
    while j > 0:
        s += str(j % 6)
        j //= 6
    return s[::-1]


d = 6**203 + 5 * 6**405 - 3 * 6**144 + 76
print(abs(h(d).count('5') - h(d).count('0')))
