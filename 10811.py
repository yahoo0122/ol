a, b = map(int, input().split())
l = [n for n in range(a+1)]
for _ in range(b):
    i, j = map(int, input().split())
    l[i:j+1] = l[i:j+1][::-1]
print(*l[1:])