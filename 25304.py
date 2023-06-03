x = int(input())
n = int(input())
d = 0
for i in range(n):
    ai, bi = map(int, input().split())
    d += ai*bi
if x == d:
    print("Yes")
else:
    print("No")