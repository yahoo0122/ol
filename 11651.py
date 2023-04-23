n=int(input())
l=[]
for i in range(n):
    a, b=(map(int, input().split()))
    l.append((b, a))
l.sort()
for b, a in l:
    print(a, b)