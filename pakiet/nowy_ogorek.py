import pickle
from pakiet.ogorki import Person

with open('data.pickle', 'rb') as f:
    people = pickle.load(f)

for person in people:
    person.say_hello()