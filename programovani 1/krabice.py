a,b,c,d,e,f = list(map(int, input().split()))

def trideni (a,b,c,d,e,f):
    s = 0
    while f > 0:
        s += 1
        f -=1
    while e > 0:
        krabice_a_e = 11
        if a > 0:
            if a <= krabice_a_e:
                dopalety_a_e = a
            else:
                dopalety_a_e = krabice_a_e
            a -= dopalety_a_e
        s += 1
        e -= 1
    while d > 0:
        krabice_b_d = 5
        krabice_a_d = 20
        if b > 0:
            if b <= krabice_b_d:
                    dopalety_b_d = b
            else:
                dopalety_b_d = krabice_b_d
            if dopalety_b_d < krabice_b_d and a > 0:
                dopalety_a_d = 4 * krabice_b_d
                a -= dopalety_a_d
            b -= dopalety_b_d 
            s += 1
        if b == 0 and a > 0:
            if a <= krabice_a_d:
                dopalety_a_d = a
            else:
                dopalety_a_d = krabice_a_d
            a -= dopalety_a_d
            s += 1
        d -= 1
    while c > 0:
        krabice_b_c = 4
        krabice_a_c = 5
        if c > 1:
            c -= 2
        else:
            if b > 0:
                if b <= krabice_b_c:
                    dopalety_b_c = b
                else:
                    dopalety_b_c = krabice_b_c
                b -= dopalety_b_c
            if a > 0:
                if a <= krabice_a_c:
                    dopalety_a_c = a
                else:
                    dopalety_a_c = krabice_a_c
                a -= dopalety_a_c
            c -= 1
        s += 1
    while b > 0:
        krabice_a_b = 36
        krabice_b_b = 9
        if b > 0:
            if b <= krabice_b_b:
                    dopalety_b_b = b
            else:
                dopalety_b_b = krabice_b_b
            b -= dopalety_b_b
            if dopalety_b_b < krabice_b_b and a > 0:
                dopalety_a_b = 4 * krabice_b_b
                a -= dopalety_a_b 
        s += 1
    while a > 0:
        krabice_a_a = 36
        if a <= krabice_a_a:
                dopalety_a_a = a
        else:
            dopalety_a_a = krabice_a_a
        a -= dopalety_a_a
        s += 1
    return(s)
print(trideni(a,b,c,d,e,f))
        
            

