x = 10


def dzielenie(a: int, b: int):
    '''Funkcja dzieli a przez b i zwraca wynik'''
    q = a // b
    w = a - q * b
    return (q, w)


def print_global():
    global x
    x = 5
    print("Zmienna w funkcji:", x)


print_global()
print("Zmienna globalna:", x)


def append_to_list(lista: list, element: int):
    lista.append(element)
    return lista


def append_to_list2(element: int, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista


lista = [1, 2, 3]
print(append_to_list(lista, 4))
print(append_to_list2(10, lista))


def print_args(*args, **kwargs):
    print(args)
    print(kwargs)


print_args(1, 2, 3, 4, 5, a=10, b=20, c=30)
print_args()
