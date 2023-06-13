
# with open("plik.txt", "a") as plik:
#     plik.write("napisanie nowej linii\n")


with open("plik.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")