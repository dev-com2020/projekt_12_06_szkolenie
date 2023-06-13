import pickle


class Person:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def say_hello(self):
        print(f'Hello, my name is {self.name} {self.surname} and my id is {self.id}')

people = [
    Person('Jan', 'Kowalski', 1),
    Person('Anna', 'Nowak', 2),
]

with open('data.pickle', 'wb') as f:
    pickle.dump(people, f)