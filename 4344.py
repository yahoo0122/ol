c = int(input())
for _ in range(c):
    l = list(map(int, input().split()))
    v = sum(l[1:]) / l[0]
    s = 0
    for i in l[1:]:
        if i > v:
            s += 1
    b = s/l[0]*100
    print(f'{b:.3f}%')