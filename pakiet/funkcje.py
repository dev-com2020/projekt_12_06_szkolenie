import random

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


def srednia(*args):
    return sum(args) / len(args)


print_args(1, 2, 3, 4, 5, a=10, b=20, c=30)
print_args()
# wynik = srednia()
# print(wynik)

kwadrat = [x ** 2 for x in range(10) if x % 2 == 0]
print(kwadrat)


def kwadrat(x):
    return x ** 2


def funkcja(x):
    return x % 2 == 0


kwadraty = map(kwadrat, filter(funkcja, range(10)))
print(list(kwadraty))

numbers = {x: x ** 2 for x in range(10)}
numbers_set = {x ** 2 for x in range(10)}
super_comp = {x ** 2: [y for y in range(x)] for x in range(10)}
losowo = [random.random() for _ in range(10)]
losowo2 = [x for x in losowo if x > 0.5]
print(losowo)
print(losowo2)
print(super_comp)
print(numbers)
print(numbers_set)
