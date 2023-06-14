import sys
input = sys.stdin.readline
l = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    for j in range(x, x+10):
        for k in range(y, y+10):
            l[j][k] = 1
r = 0
for i in l:
    r += i.count(1)
print(r)