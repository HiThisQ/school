from collections import deque
def palindrom():
    palindromy = []
    while True:
        n = input()
        if n == "0":
            break
        if n[-1] == "0" and len(n) > 1:
            continue


        zasobnik = []
        fronta = deque()

        for cifra in n:
            zasobnik.append(cifra)
            fronta.append(cifra)

        je_palindrom = True
        while fronta and zasobnik:
            if zasobnik.pop() != fronta.popleft():
                je_palindrom = False
                break
        if je_palindrom:
            palindromy.append(n)
    print(" ".join(palindromy))
palindrom()







