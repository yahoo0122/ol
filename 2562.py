l = []
for _ in range(1, 9+1):
    l.append(int(input()))
print(max(l))
print(l.index(max(l))+1)