a, b = map(int, input().split())
l = [0 for _ in range(a+1)]
for _ in range(b):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        l[n] = k
print(*l[1:])