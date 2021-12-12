import json

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))

my_list = [1, 2.34, True, "False", None,]
print(json.dumps(my_list))

my_dict = {'me': "Python", 'pi': 3.141592653589,\
            'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))

class Who:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializabble')

some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self)

print(json.dumps(some_man, cls=MyEncoder))
