h = int(input())
m = int(input())

if m >= 45:
    print(h, m-45)
else:
    if h==0:
        print(h-1, m+15)
    else:
        print(h-1, 60+15+m)