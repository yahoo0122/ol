s = input()
l = [-1 for _ in range(26)]
for i, c in enumerate(s):
    idx = ord(c)-97
    if l[idx] == -1:
        l[idx] = i
print(*l)