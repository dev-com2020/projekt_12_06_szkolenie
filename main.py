if __name__ == '__main__':
    # from pakiet import czas, teksty
    from pakiet import *
    from pakiet import funkcje as f

    # z1 = f.dzielenie(10, 2)
    reszta, iloraz = f.dzielenie(10, 2)
    lista = [reszta, iloraz]
    print("Hello World!")
    print(lista)

    a, *b, c = (1, 2, 3, 4)
    print(a, b, c)
