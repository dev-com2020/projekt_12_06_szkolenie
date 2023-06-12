a = 'Witaj'
b = "świecie"
c = '''Witaj'''

d = f"""
    Witaj
    *****
    {b}
            ^^^
            ^^^
$$$$$$$
"""

# print(d)
osoba = "dominik kamykowski"
# print(a[0:3])
# print(a[:3])
print(a[-3:-1])
# print(len(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.replace('W', 'w'))
print(osoba.capitalize())
print(osoba.endswith('ki'))
print(osoba.startswith('dom'))
print(osoba.split(' '))
print(osoba.find('k'))
print(osoba.count('k'))
print(osoba.replace('k', 'K'))

x = 5.555

print("Witaj", "świecie", sep=" >*< ", end="\n!")
print("Wartość liczby x:{} jest równa 5".format(x, '0.2f'))
print(f"Wartość liczby x:{x: .2f} jest równa 5")
print("Wartość liczby x: %.2f jest równa 5" % x)

