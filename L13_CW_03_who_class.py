import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + 'is not JSON setializable')

def decode_who(w):
    return Who(w['name'], w['age'])

old_man = Who("Jane Doe", 23)
print(old_man)
json_str = json.dumps(old_man, default=encode_who)
print(json_str)

new_man = json.loads(json_str, object_hook=decode_who)
print(new_man)
print(type(new_man))
print(new_man.__dict__)"""

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(seld, d):
        return Who(**d)

some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)