radek = input().strip()
slovnik = {}
while radek != "---":
    if ": " in radek:
        radek = radek.split(": ")
        hodnota = radek[0]
        klice = radek[1].split(", ")
        for klic in klice:
            if klic not in slovnik:
                slovnik[klic] = []
            slovnik[klic].append(hodnota)
    radek = input().strip()
for klic in sorted(slovnik):
    print(f"{klic}: {', '.join(slovnik[klic])}")
print("---\n")
