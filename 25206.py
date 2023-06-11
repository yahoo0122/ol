import sys
d = {"A+":4.5, "A0":4.0, 
     "B+": 3.5, "B0": 3.0, 
     "C+": 2.5, "C0": 2.0, 
     "D+": 1.5, "D0": 1.0, 
     "F": 0.0}
s = 0
t = 0
for i in range(20):
    data = sys.stdin.readline().split()
    if data[2] != 'P':
        t += float(data[1])
        s += float(data[1])*d[data[2]]
g = s/t
print(f'{g:.6f}')