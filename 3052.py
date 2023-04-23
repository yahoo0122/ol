l = [0]*42
for i in range(10):
    a = int(input())
    l[a % 42] = 1
print(sum(l))
