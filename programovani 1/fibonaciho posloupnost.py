
def fib(n):
    s = [1, 1]
    for _ in range(n-2):
        s.append(s[-1] + s[-2])
    return s

print(fib(11))
    
    
        
        
