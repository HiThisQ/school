# Zkouška

## Přednáška 1  Časová složitost

### Algoritmus

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

### Největší společný dělitel:

NSD(x,y), od 1 do min(x,y)
- zkoušet od min(x,y) dolů do nalezení prvního společného dělitele
- nalézt prvočíselné rozklady x,y, maximální společná část je pak NSD(x,y
- Euklidův algoritmus:
  - x < y --> NSD(x,y) = NSD(x,y-x)
  - x > y --> NSD(x,y) = NSD(x-y,y)
  - x = y --> NSD(x,y) = x
```python
while y > 0:
  z = x % y
  x = y
  y = z
print(x)
```

### Efektivita algoritmu:

časová - rychlost výpočtu programu

prostorová(paměťová) - paměť potřebná na uložení dat při výpočtu programu

optimalizujeme zpravidla jen jedno, protože obě kritéria mohou mířit proti sobě
"výměna času za paměť"

### Funkce:

počet vykonaných operací v závislosti na velikosti vstupních dat
funkce časové i prostorové složitosti většinou rostoucí

### Asymptotická časová složitost:

Symbol velké O, odhad shora
f, g: N → R
f ∈ O(g) <=> E c > 0 V n0 > 0 V n ≥ n0 : 0 ≤ f(n) ≤ c.g(n)

Opačný odhad zdola: f ∈ Ω(g) 0 ≤ c.g(n) ≤ f(n)

Přesný (těsný) odhad: f ∈ Θ(g) <=> f ∈ O(g) a f ∈ Ω(g)

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
## Přednáška 2  Základní algoritmy

### Složitost algoritmu v různých příkladech:

Pro každá vstupní data velikosti N nemusí trvat výpočet stejně dlouho
Časová složitost algoritmu v
- nejhorším případě: maximální počet vykonaných operací
- nejlepším případě: minimální počet vykonaných operací
- průměrném případě: očekávaný počet vykonaných operací
nejčastěji se používá časová složitost v nejhorším případě
v průměrném případě se dobře charakterizuje kvalita algoritmu, ale je obtížně oddůvoditelná

### Složitost problému:

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

### Základní algoritmy s čísly:

#### Rozklad čísla na cifry
```python
def ciferny_soucet(x):
y = 0
while x != 0:
  y += x % 10
  x //= 10
return y
```
#### Test prvočíselnosti 

- zkusit všechny dělitele od 2 do N-1, cca O(N)
- zkusit všechny dělitele od 2 do $\frac{N}{2}$, cca O(N) ale lepší
- zkusit všechny dělitele od 2 do $\sqrt{N}$, cca O($\sqrt{N}$)
- zkusit dělitele od 2 do $\sqrt{N}$ do nalezení prvního
  - v nejhoším O($\sqrt{N}$)
  - v nejlepším 1
- zkusit 2 a poté liché dělitele lichých čísel
```python
from math import sqrt

def prvocislo(n):
  for d in range(2, int(sqrt(n) + 1):
    if n % d == 0:
      return False
  return True
```
nebo 
```python
def prvocislo(n):
  if n % 2 == 0: 
    return n == 2  #jediné sudé prvočíslo
  d = 3
  while d * d <= n:
      if n % d == 0:
        return False
      d += 2
  return True
```

#### Eratosthenovo síto 

Určete všechna prvočísla od 2 do N

princip - v řadě od 2 do N postupně škrtáme všechny násobky jednotlivých prvočísel, zbývající čísla pak jsou hledaná prvočísla 
```python
def eratosth(n):
  sito = [False, False] + [True] * (n-1)
  prvocisla = []

  for i in range(n + 1):
    if sito[i]:
      prvocisla.append(i)
      j = i * i         #staci zacit s nasobky od kvadratu
      while j <= n:
        sito[j] = False
        j = j + i
  return prvocisla
```
časová složitost je O($\frac{N}{2}$ + $\frac{N}{3}$ + $\frac{N}{5}$ + ...) = O(N log(log N))

#### Dlouhá čísla 

počítání s čísly s desítkami nebo stovkami cifer
pyzhon to umí sám

reprezentace
- vytvoříme seznam cifer
- použijeme seznam čísel nikoli znaků
- pořadí cifer zvolíme odpředu nebo odzadu

operace
- po cifrách sčítání, odčítání, násobení, dělení
- počítání modulo 10

desetinné číslo, ukládáme pozici desetinné čárky
- speciální hodnota uložená v seznamu (nešikovné)
- proměnná s indexem nulového řádu
- použít dvě pole (celá a desetinná část)

Příklad

Součet dvou kladných celých čísel s mnoha ciframi
Vstup: a,b jsou seznamy cifer sčítaných čísel, a[0] = cifra v řádu jednotek
Výstup: c je výsledný seznam cifer součtu čísel a + b

- sčítání s přenosem v rozsahu cifer kratšího čísla
- ošetřit přečnívající část delšího čísla
- přidat případný poslední nenulový přenos
```python
if len(a) < len(b)
  a, b = b, a

prenos = 0
c = []
for i in range(len(b)):
  x = a[i] + b[i] + prenos
  c.append(x%10)
  prenos = x // 10

for i in range(len(b), len(a)):
  x = a[i] + prenos
  c.append(x%10)
    prenos = x // 10

if prenos > 0:
  c.append(prenos)
```

#### Vyhodnocení polynomu v bodě 

a(x) = a<sub>n</sub>x<sup>n</sup> + a<sub>n-1</sub>x<sup>n-1</sup> ... + a<sub>1</sub>x + a<sub>0</sub>
- n stupeň polynomu
- a<sub>0</sub>, ...,a<sub>n</sub> koeficienty (reálné konstanty)
- x proměnná, dosazujeme různé hodnoty

Přímý výpočet podle předpisu 

- počet násobení: n + (n-1) + (n-2) + ... + 1 = $\frac{n(n+1)}{2}$
- počet sčítání: n
- časová složitost: Θ(n<sup>2</sup>)

Hornerovo schéma

a(x) = (...((a<sub>n</sub>x + a<sub>n-1</sub>)x + a<sub>n-2</sub>)x + ... + a<sub>1</sub>)x + a<sub>0</sub>
  - počet násobení: n
  - počet sčítání: n
  - časová složitost: Θ(n)
```python
def horner(a, x):
# a: seznam s koeficienty polynomu a[i] * x^i, x: bod z Df, vrátí hodnotu v bodě x
  h = 0
  for i in range(len(a)-1, -1, -1):
    h = h * x + a[i]
  return h
```
Příklady použití jsou vstup čísla po znacích nebo konverze číselného str na int

#### Operace s polynomy 

a(x) = a<sub>n</sub>x<sup>n</sup> + a<sub>n-1</sub>x<sup>n-1</sup> ... + a<sub>1</sub>x + a<sub>0</sub>

b = b<sub>m</sub>x<sup>m</sup> + b<sub>m-1</sub>x<sup>m-1</sup> ... + b<sub>1</sub>x + b<sub>0</sub>

součet
```python
a = [2, -5, 0, 4, 6]     # 6x^4 + 4x^3 - 5x + 2
b = [11, 0, -2]          # -2^2 + 11

def soucet(a, b):
  c = []
  if len(a) < len(b)
    a, b = b,a
  for i in range(leb(b)):
    c.append(a[i]+b[i])
  for i in range(len(b), len(a)):
    c.append(a[i])
  while len(c) > 1 and c[-1] == 0:
    del[-1]
  return c

print(soucet(a,b))
```
součin
```python
a = [2, -5, 0, 4, 6]     # 6x^4 + 4x^3 - 5x + 2
b = [11, 0, -2]          # -2^2 + 11

def soucin(a, b):
  c = [0] * (len(a) + len(b) - 1)
  for i in range(len(a)):
    for j in range(len(b)):
      c[i+j] += a[i] * b[j]
  return c

print(soucin(a,b))
```
#### Číselné soustavy 

převod z dvojkové soustavy na číselnou hodnotu přes Hornerovo schéma

***110010*** = ***1***.2<sup>5</sup> + ***1***.2<sup>4</sup> + ***0***.2<sup>3</sup> + ***0***.2<sup>2</sup> + ***1***.2<sup>1</sup> + ***0***.2<sup>0</sup> = ((((***1***.2 + ***1***).2 + ***0***).2 + ***0***).2 + ***1***).2 + ***0*** = 50

převod z šestnáctkové soustavy na číselnou hodnotu

A1F = ***A***.16<sup>2</sup> + ***1***.16<sup>1</sup> + ***F***.16<sup>0</sup> = ***10***.16<sup>2</sup> + ***1***.16<sup>1</sup> + ***15***.16<sup>0</sup> = (***10***.16 + ***1***)16 + ***15*** = 2591

Převod binárního zápisu (str) na číselnou hodnotu, O(N)
```python
def bin_int(s):
  n = 0
  for i in range(len(s)):
    n = n * 2 + int(s[i])
  return n
```
Převod hexadecimálního zápisu (str) na číselnou hodnotu, O(N)
```python
def hex_int(s):
  cifry = "0123456789ABCDEF"
  n = 0
  for i in range(len(s)):
    n = n * 16 + cifry.index(s[i])
  return n
```
Pro převod číselné hodnoty do dvojkové soustavy využijeme Hornerovo schéme v opačném směru, posloupnost zbytků při celočíselném dělení dvěma tvoří odzadu dvojkový zápis čísla, O(n)
```python
def int_bin(n):
  if n == 0:
    return "0"
  s = []
  while n > 0:
    s.append.(str(n % 2))
    n //= 2
  return "".join(reversed(s))
```
Převod z číselné hodnoty do hexadecimální soustavy, O(n)
```python
def int_hex(n):
  if n == 0:
    return "0"
  cifry = "0123456789ABCDEF"
  s = []
  while n > 0:
    s.append(cifry[n % 16])
    n //= 16
  return "".join(reverse(s))
```
#### Rychlé umocňování 

Příklad

spočítat hodnotu x<sup>n</sup> 
 - n: velké kladné číslo
 - x: reálné číslo(nebo matice)

přímočaré řešení, Θ(N)
```python
def mocnina1(x, n):
  v = 1
  for i in range(n):
    v *= x
  return v
```
postupně počítáme hodnoty x, x<sup>2</sup>, x<sup>4</sup>... a vhodně z nich vynásobíme

mocninu rozložíme na definitivní rozklad mocnin dvojky, a jsou to ty mocniny dvojky, kde je jednička v binárním zápisu čísla n, Θ(log N)
```python
def mocnina2(x, n):
  v = 1
  while n > 0:
    if n % 2 == 1:
      v *= x
    x = *= x
    n //= 2
  return v
```
## Přednáška 3, Vyhledávání v seznamu

Příklad

kde se nachází daná hodnota x v seznamu pokud v něm je

Základní algoritmus je sekvenční vyhledávání, jeden průchod celým polem, neefektivní, O(N)
```python
j = -1
for i in range(len(s)):
  if a[i] == x:
    j = i
    break
if j == -1:
  print ("není tam")
else:
  print("je na pozici", j)
```
pomocí while cykklu
```python
i = 0
while i < len(a) and s[i] =! x:
  i += 1
if i = len(s):
  print("není tam")
else:
  print("je na pozici", i)
```
binární vyhledávání 

Data musí být uspořádaná, vezmeme prostřední prvek a porovnáme ho s hledaným, dále se dívame jen na menší nebo větší půlku a dostáváme úseky $frac{n}{2}$, $frac{n}{4}$, $frac{n}{8}$...1

časová složitost - n/2 



  
  
  








      



