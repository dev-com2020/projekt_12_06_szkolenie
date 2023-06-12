names = ['jan', 'Zofia', 'Krzysztof', 'anna', 'Paweł', 'Maria', 'Stanisław', 'Katarzyna',
         'Tomasz', 'Małgorzata']
names.sort()
print(names)
names.sort(key=str.lower)
print(names)
names.sort(key=len)
print(names)
names.sort(key=len, reverse=True)
print(names)

for name in names:
    print(name.capitalize())

names.append('Marcin')
names.insert(0, 'Dominik')
print(names[2:5])
print(names[2:-1])
names[2] = 'Kamil'
print(names)
names.remove('Kamil')
# names.pop(222)
# names[222] = 'Kamil'
print(len(names))

print(names.index('Tomasz'))
print(names.count('Tomasz'))

lista = []
for i in range(1, 11):
    lista.append(2)

print(lista)

lista2 = [0 for i in range(1, 11)]
print(lista2)

zakupy = [12, "tomek", 12.5, True, None, [1, 2, 3]]
print(zakupy[5][1])

lista_zakupow = tuple(zakupy)
print(lista_zakupow)
print(lista_zakupow[0:2])
zakupy = list(lista_zakupow)
print(zakupy)
krotka = 3,
print(krotka)

nowa_lista = zakupy + lista2
print(nowa_lista)

kolejna_lista = lista * 2
print(kolejna_lista)

print(12 in lista_zakupow)
print(123232 not in lista_zakupow)

tablica = [[1, 2, 3],
           [4, 5, 6]]
print(tablica[1][1])

slownik = {'imie': 'Jan',
           'nazwisko': 'Kowalski',
           'wiek': 25,
           'hobby': ['programowanie', 'rower', 'piłka nożna']
           }

print(slownik['imie'])
# print('Kowalski' in slownik.values())
# print('Kowalski' in slownik.items())

# print(slownik.items())
#
# for key, value in slownik.items():
#     print(f"{key} -> {value}")

# print('wiek' in slownik.keys())
slownik['wzrost'] = 180
slownik['wzrost'] = 280
print(slownik)

del slownik['wzrost']
print(slownik)