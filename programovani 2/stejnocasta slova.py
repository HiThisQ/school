
def stejnocasta_slova():
    text = []
    while True:
        line = input().strip()
        if line == "---":
            break
        text.append(line.casefold())
    return text
cisty_text = " ".join(stejnocasta_slova())
cisty_text = cisty_text.split(" ")
print(cisty_text)