a = int(input())
r = 0
for _ in range(a):
    w = input()
    for n in range(len(w)-1):
        if w[n] == w[n+1]:
            pass
        elif w[n] in w[n+1:]:
            r += 1
            break
print(a-r)