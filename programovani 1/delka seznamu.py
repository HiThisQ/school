si = [int(_) for _ in input().split()]

def seznam(s):
    p = 0
    while s:
        p += 1
        x = s[0]
        while x in s:
            s.remove(x)
    return p

print(seznam(si))
