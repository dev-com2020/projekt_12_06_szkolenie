dodaj = lambda x, y: x + y
podwojenie = lambda x: x * 2
dlugosc = lambda x: len(x)
print(dodaj(2, 3))
print(podwojenie(7))
print(dlugosc("Ala ma kota"))

values = dict(one=1, two=2, three=3)

print(values)
print(sorted(values.items(), key=lambda x: x[1]))
print(sorted(values.items()))

# Y2 = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
Y3 = lambda f: lambda *args: f(Y3(f))(*args)

def Y(f):
    def y(*args):
        y_function = f(Y(f))
        return y_function(*args)
    return y
