def f(x: str):
    d = int(f'9009{x}', 18) + int(f'2257{x}', 18)
    return d % 15 == 0, d / 15

for l in '0123456789ABCDEFGH':
    k = f(l)
    if k[0]:
        print(k[1])
        break
