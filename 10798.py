l = [input() for _ in range(5)]
for j in range(15):
    for k in range(5):
        if len(l[k]) > j:
            print(l[k][j], end='')