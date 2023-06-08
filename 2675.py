t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    for n in s:
        print(n*r, end="")
    print()