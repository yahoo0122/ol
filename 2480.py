a, b, c = map(int, input().split())
d = 0
if a == b and b == c:
    d = 10000+a*1000
else:
    if a == b or a == c:
        d = 1000+a*100
    elif b == c:
        d = 1000+b*100
    else:
        if a > b and a > c:
            d = a*100
        elif b > a and b > c:
            d = b*100
        elif c > b and c > a:
            d = c*100

print(d)