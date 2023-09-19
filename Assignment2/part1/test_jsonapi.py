import json

from Assignment2.part1.jsonapi import MyEncoder, MyDecoder

my_data = {
    "hey": complex(1, 2),
    "there": range(1, 10, 3),
    73: False,
}

json_data = json.dumps(my_data, cls=MyEncoder)

decoded = json.loads(json_data, cls=MyDecoder)
print(decoded)
# {'hey': (1+2j), 'there': range(1, 10, 3), '!': False}
