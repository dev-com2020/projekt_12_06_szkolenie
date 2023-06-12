# Treść komentarza
'''
Komentarz
wieloliniowy
'''

"""
Komentarz
wieloliniowy
"""

x: int = 1
y = 2.5
z = "tekst"
b: bool = True
print(x, y, z, b)
print(type(x), type(y), type(z), type(b))

# x1 = int(input("Podaj x: "))
# x2 = int(input("Podaj y: "))
# print("Wynik dodawania:", x1 + x2)

liczba = 1276.1564654562
print(f"{liczba:.2f}")
x = x + 1
x += 1

if x == 3:
    print("x jest równe 3")
    if y == 2.5:
        print("y jest równe 2.5")
    elif y == 2:
        print("y jest równe 2")
elif x == 4:
    print("x jest równe 4")
else:
    print("x nie jest równe 3 ani 4")


def funkcja():
    pass


def response_status(status_code: int) -> str:
    if status_code == 200:
        return "OK"
    elif status_code == 400:
        return "Bad Request"
    elif status_code == 404:
        return "Not Found"
    else:
        return "Unknown"

def response_status310(status_code):
    x = 200
    match status_code:
        case 200:
            x = 2000
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"


print(response_status(200))
print(response_status("Tomek"))

print(response_status310("Tomek"))
print(response_status310(404))


