import itertools
import logging
import operator

months = [10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = list(itertools.accumulate(months, operator.add))
print(lista)


def multi(a, b):
    return a * b


def multi2(a, b):
    try:
        return a * b
    except TypeError:
        logging.warning('Nie można pomnożyć stringów')


try:
    print(multi('2', '2'))
except TypeError:
    logging.warning('Nie można pomnożyć stringów')

print(multi(2, 2))
print(multi2('2', '2'))
print(multi2(2, 2))


def check_age(users, age):
    count = 0
    for i, user in enumerate(users):
        try:
            if int(user['age']) < age:
                count += 1
        except KeyError:
            logging.warning(f'Brak klucza age: {user}')
        except ValueError:
            logging.warning(f'Wartość age nie jest liczbą: {user}')
        else:
            print(f'Wiek {user["name"]} jest ok')
        finally:
            print(f'{i}-{user}')
    return count


valid_data = [{'name': 'Jan', 'age': '20'}, {'name': 'Anna', 'age': '30'}, {'name': 'Paweł', 'age': '40'}]
invalid_data = [{}, {'name': 'Anna', 'age': '30'}, {'name': 'Paweł', 'age': '40'}]
invalid_data2 = [{'name': 'Jan', 'age': 'age'}, {'name': 'Anna', 'age': '30'}, {'name': 'Paweł', 'age': '40'}]
licznik = check_age(valid_data, 30)
print(licznik)
licznik2 = check_age(invalid_data, 30)
print(licznik2)
licznik3 = check_age(invalid_data2, 30)
print(licznik3)
