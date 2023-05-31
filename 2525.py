a, b = map(int, input().split())
c = int(input())
d = 0
if b+c >= 60:
    d = (b+c)//60
    a = a+d
    b = b+c-(60*d)
else:
    b = b+c
if a >=24:
    a = a-24
print(a, b)