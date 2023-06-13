a, b = [], []
n, m = map(int, input().split())
for _ in range(n):
    l = list(map(int, input().split()))
    a.append(l)
for _ in range(n):
    l = list(map(int, input().split()))
    b.append(l)
for i in range(n):
    for g in range(m):
        print(a[i][g] + b[i][g], end=' ')
    print()