n=int(input())
l=[]
for i in range(n):
    a, b=(map(int, input().split()))
    l.append((a, b))
l.sort()
for a, b in l:
    print(a, b)