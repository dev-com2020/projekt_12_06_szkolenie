import json
import sys

data = {'big_number': 100000000,
        'max_float': sys.float_info.max,
        'a_list': [1, 2, 3, 4, 5], }

print(data)
json_data = json.dumps(data)
print(json_data)
print(type(json_data))
data_out = json.loads(json_data)
assert data == data_out

info = {
    'full_name': 'Sherlock Holmes',
    'address': {
        'street': '221B Baker St',
        'zip': 'NW1 6XE',
        'city': 'London',
        'country': 'UK',
    }
}

print(json.dumps(info, indent=4, sort_keys=True))

data_in = {'a_tuple': (1, 2, 3), }

json_data = json.dumps(data_in)
print(json_data)
data_out = json.loads(json_data)
print(data_out)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return super().default(obj)


data = {
    'a_complex_number': 4 + 1j,
    'a_list': [1, 2, 3, 4, 5],
    'a_flot': 4.343434340,
}

json_data = json.dumps(data, cls=ComplexEncoder)
print(json_data)


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


data_out = json.loads(json_data, object_hook=as_complex)
print(data_out)

from datetime import datetime, timedelta, timezone

now = datetime.now()

data = {
    'an_int': 42,
    'a_float': 3.141592653589,
    'a_string': 'string',
    'a_datetime': now,
}
print(data)


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


json_data = json.dumps(data, cls=DatetimeEncoder)
print(json_data)


def as_datetime(dct):
    if 'a_datetime' in dct:
        return datetime.fromisoformat(dct['a_datetime'])
    return dct

data_out = json.loads(json_data, object_hook=as_datetime)
print(data_out)

with open('dane.json', 'r') as f:
    dane = json.load(f)

moce = dane['members'][0]['powers']
print(moce)