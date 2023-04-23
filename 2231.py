n = int(input())
a=0
for i in range(1, n):
    if i+sum(map(int, str(i)))==n:
        a=i
        break
print(a)