input()
l = list(map(int, input().split()))
ol=l.copy()
l = set(l)
l = sorted(l)
d = {}
for i, v in enumerate(l):
    d[v] = i

for i in ol:
    print(d[i], end=" ")
