n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
print(*l, sep="\n")