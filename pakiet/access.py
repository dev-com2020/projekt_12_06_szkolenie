import random


class Access:

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Pobieranie', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Ustawianie', self.name)
        self.val = val

    def __delete__(self, obj):
        print('Usuwanie', self.name)
        del self.val


class MyClass:
    x = Access(10, 'var "x"')
    y = 5


m = MyClass()
print(m.x)
m.x = 20
del m.x


def f():
    print('f()')


print(hasattr(f, '__get__'))
print(hasattr(f, '__set__'))


class InitOnAccess:
    def __init__(self, init_func, *args, **kwargs):
        self.init_func = init_func
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print('Inicjalizacja')
            self.initialized = self.init_func(instance, *self.args, **self.kwargs)
        else:
            print('Ponowne uzycie')
        return self._initialized


# class WithSortedRandoms:
#     lazily_initialized_list = InitOnAccess(sorted, [random.random() for _ in range(10)])
#

class lazy_property:
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, cls):
        value = self.func(obj)
        setattr(obj, self.func.__name__, value)
        return value


class WithSortedRandoms:
    @lazy_property
    def lazily_initialized_list(self):
        print('Inicjalizacja')
        return sorted([random.random() for _ in range(10)])

w = WithSortedRandoms()
print(w.lazily_initialized_list)
print(w.lazily_initialized_list)