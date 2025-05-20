#dostaneme x a chceme udělat x řádků hvězdiček do pyramidy
x = int(input())

#musime dat urcity pocet mezer na zacatek a postupne je zmensovat
#v i-tem radku neni mezera, ale je tam 2i + 1 hvezdice, na prvnim je 1 hvezda
#1 hvezda a i//2 mezer


for i in range(x):
    print(" " * (x-i-1), "*" * (2*i+1))

