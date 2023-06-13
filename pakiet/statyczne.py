class Ops:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

a = Ops.add(1, 2)
b = Ops.sub(1, 2)
print(a, b)
