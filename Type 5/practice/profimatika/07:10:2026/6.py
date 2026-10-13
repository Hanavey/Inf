def f(n: int):
    return int(str((n // 10) + (n % 10)) + str((n // 10) * (n % 10)))

for i in range(10, 100):
    if f(i) == 918:
        print(i)
        break
