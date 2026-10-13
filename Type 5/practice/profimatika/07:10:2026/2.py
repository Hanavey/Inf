def f(n: int):
    s = bin(n)[2:]
    k = 0
    for i in s:
        k += int(i)
    return bin(k)[2:]

print(f(511))