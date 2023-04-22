input()
l = list(map(int, input().split()))
target = int(input())
count = 0
for i in l:
    if target == i:
        count += 1
print(count)