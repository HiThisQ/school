s = input().split()
d = {}
for x in s:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

for y in d.items():
    print(y)
