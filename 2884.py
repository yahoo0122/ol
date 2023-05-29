a, b = map(int, input().split())

if b < 45:

    if a == 0:
        a = 23
        b = 60-(45-b)    
    else:
        a = a-1
        b = 60-(45-b)
else:
    b = b-45

print(a, b)