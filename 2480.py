a = int(input())
b = int(input())
c = int(input())

if a==b and b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a, b, c)*100)