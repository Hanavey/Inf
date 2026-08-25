# https://education.yandex.ru/ege/inf/task/d82e2ec1-ce45-4e1f-b38b-c468f2886255
ls = [str(i) for i in range(1000, 10001)]

def f(n):
    return len(str(int(''.join(sorted([str(int(n[0]) * int(n[1])), str(int(n[1]) * int(n[2])), str(int(n[2]) * int(n[3]))]))))) == 4

c = 0
for i in ls:
    if f(i):
        c += 1
print(c)

