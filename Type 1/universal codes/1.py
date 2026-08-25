from itertools import permutations


print(*range(1,9), sep=' | ')

# Через пробел указываем все номера столбцов каждой строки
tab = "57 457 46 236 12 348 128 67".split()
# Через пробел указываем все соединения в графе
pic = "cg cf gh gd hd db eb ae af fb".split()

for i in permutations("abcdefgh"):
    if all(str(i.index(x) + 1) in tab[i.index(y)] for x, y in pic):
        print(*i, sep=' | ')