a = int(input("Wprowadz a: "))

if a % 2 == 0:
    print("licza jest parzysta")
else:
    print("Liczba nie jest parzysta")

wiek = int(input("Wprowadz wiek: "))

if wiek >= 18:
    print("Jesteś dorosły")
else:
    print("Nie jesteś dorosły")

slowo = input("Wprowadz słowo: ")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in list:
    if i > 10:
        print(f"{i}")

lp = 1

petla = True

while (petla == True):
    for i in range(1, 12):
        if i == 11:
            lp = lp + 1
            i = 1
        if lp == 11:
            petla = False
        else:
            m = lp * i
            print(f"Tabliczka mnożenia dla {lp} - {m}")

slowoo = slowo[::-1]

if slowo == slowoo:
    print("Słowo jest palindromem")
else:
    print("Słowo nie jest palindromem")