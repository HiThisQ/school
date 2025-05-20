from collections import deque
def nejvice_lidi ():
    k = int(input())
    queue = deque([0] * k, maxlen=k)
    hosti_ted = 0
    max_hosti = 0

    while True:
        radek = input()
        if "-end-" in radek:
            break
        novi_hosti = int(radek)
        odchazejici = queue[0]
        hosti_ted += novi_hosti - odchazejici
        max_hosti = max(max_hosti, hosti_ted)
        queue.append(novi_hosti)

    return(max_hosti)
print(nejvice_lidi())