l = [list(map(int, input().split())) for _ in range(9)]
m = 0
x = 0
y = 0
for i in range(9):
    for g in range(9):
        if l[i][g] >= m:
            m = l[i][g]
            x = i+1
            y = g+1
print(m)
print(x, y)