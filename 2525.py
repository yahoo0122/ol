h = int(input())
m = int(input())
t = int(input())

if h == 23 and m+t == 60:
    print("띵동댕동")
else:
    if m+t > 60:
        if h == 23:
            print(0, (m+t)-60)
        else:
            print(h+1, (m+t)-60)
    else:
        print(h, (m+t))