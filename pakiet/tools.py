from functools import reduce
from itertools import count

f = map(lambda x: x ** 2, range(10))
print(list(f))
mapped = list(map(print, range(5), range(4), range(5)))
print(mapped)
evens = filter(lambda x: x % 2 == 0, range(10))
odds = filter(lambda x: x % 2 != 0, range(10))
animals = ['cat', 'dog', 'parrot', 'rabbit']
print(list(map(len, animals)))
print(list(map(str.upper, animals)))
animals_s = filter(lambda x: x.startswith('c'), animals)
print(list(animals_s))
print(list(evens))
print(list(odds))

r = reduce(lambda x, y: x + y, range(10))
print(r)
r1 = reduce(lambda x, y: x + y, [2, 3, 4])
print(r1)

sekwencja = map(lambda x: x ** 2, count())
print(next(sekwencja))
print(next(sekwencja))
print(next(sekwencja))
print("inne rzeczy")
print(next(sekwencja))
print(next(sekwencja))
print("inne rzeczy")
print(next(sekwencja))

def prosty_generator():
    yield 1
    yield 2
    yield 3

gen = prosty_generator()
print("Z generatora",next(gen))
print(next(sekwencja))
print("Z generatora",next(gen))
print(next(sekwencja))
print(next(sekwencja))
print("Z generatora",next(gen))
# print("Z generatora",next(gen))
print(next(sekwencja))