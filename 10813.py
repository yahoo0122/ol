a, b = map(int, input().split())
l = []
for n in range(a+1):
    l.append(n)
k = 0
for _ in range(b):
    i, j = map(int, input().split())
    k = l[i]
    l[i] = l[j]
    l[j] = k
print(*l[1:])