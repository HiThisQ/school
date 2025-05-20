import heapq

class MaxFronta:
    def __init__(self):
        self.fronta = []
        self.poradi = 0

    def push(self, cislo: int):
        heapq.heappush(self.fronta, (-cislo, self.poradi, cislo))
        self.poradi += 1

    def pop(self) -> int:
        return heapq.heappop(self.fronta)[2]

    def is_empty(self) -> bool:
        return not self.fronta

def main():
    fronta = MaxFronta()
    vystup = []
    while True:
        try:
            radek = input().strip()
            if radek == "-end-":
                vystup.append("-end-")
                break
            elif radek == "->":
                if not fronta.is_empty():
                    vystup.append(str(fronta.pop()))
            else:
                try:
                    fronta.push(int(radek))
                except ValueError:
                    pass
        except EOFError:
            break
    print("\n".join(vystup))

if __name__ == "__main__":
    main()
