a = input().upper()
al = list(set(a))
idx = []
for i in al:
    idx.append(a.count(i))
if idx.count(max(idx)) > 1:
    print("?")
else:
    print(al[idx.index(max(idx))])