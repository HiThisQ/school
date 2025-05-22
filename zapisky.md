# Zkouška

## 1. přednáška, časová složitost

Algoritmus:

intuitivní pojem, není pro něj specifikcká definice
možnou definicí by mohlo být
- Konečná posloupnost elementárních příkazů, jejichž provádění
umožňuje pro každá přípustná vstupní data mechanickým způsobem
získat po konečném počtu kroků příslušná výstupní data

Typické vlastnosti:
- konečnost
- hromadnost
- resultativnost
- jednoznačnost
- determinismus

Největší společný dělitel:

NSD(x,y), od 1 do min(x,y)
- zkoušet od min(x,y) dolů do nalezení prvního společného dělitele
- nalézt prvočíselné rozklady x,y, maximální společná část je pak NSD(x,y
- Euklidův algoritmus:
  - x < y --> NSD(x,y) = NSD(x,y-x)
  - x > y --> NSD(x,y) = NSD(x-y,y)
  - x = y --> NSD(x,y) = X
```python
while y > 0:
  z = x % y
  x = y
  y = z
print(x)
```

Efektivita algoritmu:

časová - rychlost výpočtu programu

prostorová(paměťová) - paměť potřebná na uložení dat při výpočtu programu

optimalizujeme zpravidla jen jedno, protože obě kritéria mohou mířit proti sobě
"výměna času za paměť"

Funkce:

počet vykonaných operací v závislosti na velikosti vstupních dat
funkce časové i prostorové složitosti většinou rostoucí

Asymptotická časová složitost:

Symbol velké O, odhad zhora
f, g: N → R
f ∈ O(g) <=> E c > 0 V n0 > 0 V n ≥ n0 : 0 ≤ f(n) ≤ c.g(n)

Opačný odhad zdola: f ∈ Omega(g) 0 ≤ c.g(n) ≤ f(n)

Přesný (těsný) odhad: f ∈ Phi(g) <=> f ∈ O(g) a f ∈ Omega(g)

Typické třídy asymptotické složitosti jsou
- O(1)
- O(log N)
- O(N)
- O(N log N)
- O(N<sup>2</sup>)
- O(N<sup>x</sup>)
- O(2<sup>N</sup>)
- O(N!)

polynomiálně omezený čas zvládnutelný i pro velká n, exponenciální časově nezvládnutelný
## 2. přednáška, základní algoritmy

Složitost algoritmu v různých příkladech:

Pro každá vstupní data velikosti \n nemusí trvat výpočet stejně dlouho
Časová složitost algoritmu v
- nejhorším případě: maximální počet vykonaných operací
- nejlepším případě: minimální počet vykonaných operací
- průměrném případě: očekávaný počet vykonaných operací
nejčastěji se používá časová složitost v nejhorším případě
v průměrném případě se dobře charakterizuje kvalita algoritmu, ale je obtížně oddůvoditelná

Složitost problému:

- složitost nejlepšího algoritmu (z hlediska časové složitosti),
kterým lze řešit daný problém

odvození bývá často obtížné, pro řadu problémů je složitost neznámá

Pro dokazování nejhoršího případu potřebujeme
- existuje algoritmus, který vyřeší problém v dané časové složitosti v nejhorším případě, předvedeme konkrétní algoritmus
- každý algoritmus řešící daný problém pracuje v dané časové složitosti v nejhorším příkladě, bývá složité na dokázání

Příklad
Nalézt maximum z N čísel
- existuje algoritmus v čase O(N)
- nemůže existovat algoritmus s lepší časovou obtížností, protože musíme projít všech N čísel

Základní algoritmy s čísly:

Rozklad čísla na cifry
```python
def ciferny_soucet(x):
y = 0
while x != 0:
  y += x % 10
  x //= 10
return y
```
Test prvočíselnosti 

- zkusit všechny dělitele od 2 do N-1, cca O(N)
- zkusit všechny dělitele od 2 do N/2, cca O(N) ale lepší
- zkusit všechny dělitele od 2 do $\sqrt{2}$




