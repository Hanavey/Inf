def f(x: str, y: str):
    d = int(f'{x}23{x}5', 22) + int(f'67{y}9{y}', 13)
    return d % 57 == 0, d / 57

l = []
for x in '123456789ABCDEFGHIJKL':
    for y in '123456789ABC':
        if f(x, y)[0]:
            l.append((f(x, y)[1], int(x, 22) + int(y, 13)))
print(l)