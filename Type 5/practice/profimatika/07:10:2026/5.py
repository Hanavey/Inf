def f(n: int):
    s = bin(n)[2:][::-1]
    for i in s:
        if i == '0':
            s = s[1:]
        if i == '1':
            break
    s = s[::-1]
    return int(s, 2)

for i in range(40, 101):
    if f(i) == 1:
        print(i)

