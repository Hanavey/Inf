# ¬(y →w)∨(x ≡z)∨¬x
print('w | x | y | z | F')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(y <= w) or (x == z) or not x
                if not f:
                    print(w, x, y, z, f, sep=' | ')

# yxzw