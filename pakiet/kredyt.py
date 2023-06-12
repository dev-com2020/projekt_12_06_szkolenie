
kwota = 1000
oprocentowanie = 0.05
lata = 5
rok = 1
# while rok <= lata:
#     kwota *= 1 + oprocentowanie
#     print(f"Po roku {rok} kwota wynosi {kwota:.2f} zł")
#     rok += 1
#
# print("Koniec programu")


for rok in range(2, lata + 2, 2):
    kwota *= 1 + oprocentowanie
    print(f"Po roku {rok} kwota wynosi {kwota:.2f} zł")

# x = 0
# while (x := x + 1) <= 10:
#     if x == 5:
#         # break
#         continue
#     print(x)

while True:
    print("MENU:")
    print("1. Dodaj")
    print("2. Odejmij")
    print("x. Wyjdź")
    x = input("Wybierz opcję: ")
    if x == "1":
        print("Dodaję")
    elif x == "2":
        print("Odejmuję")
    elif x == "x":
        print("Koniec")
        break
    else:
        print("Nieprawidłowa opcja")