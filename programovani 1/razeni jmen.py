#dostaneme seznam jmen "Jan Novak", "Tomas Dvorak", chceme seradit abecedne
#nejdrive podle prijmeni pak podle jmena
seznam = ["Jan Novak", "Tomas Dvorak", "Alena Novakova", "Jenik Novak"]


def jmena(s):
    t = [x.split() for x in s]
    u = sorted((x[1], x[0]) for x in t)
    return [jm + " " + pr for pr, jm in u]


print(jmena(seznam))
