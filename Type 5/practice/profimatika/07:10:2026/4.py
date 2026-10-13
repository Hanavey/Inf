def f(n: int):
    s = hex(n)[2:]
    h = ''
    for i in s:
        if i in 'abcdef':
            h += i
    return int(h, 16)


print(f(440))
