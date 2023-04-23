l = []
for i in range(9):
    t=list(map(int, input().split()))
    l.append(t)

m=0
for i in range(9):
    for j in range(9):
        if m < l[i][j]:
            m=l[i][j]
            a=i
            b=j
print(m)
print(a+1, b+1)