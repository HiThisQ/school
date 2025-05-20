#dostaneme seznam cisel, program ma vypsat stejne dlouhy seznam cisel
#kde budou modulo 7

seznam = [11, 22, 33, 44, 55]

print([x%7 for x in seznam])

print(list(map(lambda x: x%7, seznam)))
