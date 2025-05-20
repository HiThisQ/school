from operator import itemgetter

lide = [("Jana", "Nováková", 1964),
    ("Kateřina", "Kocourová", 1962),
    ("Jozef", "Winkler", 1952),
    ("Petr", "Suchý", 1968),
    ("Jan", "Michal", 1951)]
sorted(lide, key = lambda t : t[2])
sorted(lide, key = lambda t : t[2], reverse = True)
sorted(lide, key = itemgetter(2))

