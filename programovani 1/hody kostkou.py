import random
r = [0]*6
for i in random.choices(range(6), k = 1000):
    r[i] += 1
print(r)
    
