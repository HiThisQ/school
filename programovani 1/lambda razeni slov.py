#dostaneme text ve stringu, mame napsat program ktery dostane text a vrati
#seznam slov podle delky slova a sekundarne podle abecedy diky lambda funkci

seznam = "prosim boze at to funguje"
serazeny_seznam = seznam.split()

print(sorted(serazeny_seznam, key = lambda x: (len (x), x)))

print()

print(sorted(seznam.split(), key = lambda x: (len(x), x)))
