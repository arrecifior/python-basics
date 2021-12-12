import json

jstr = '1.60217662'
electron = json.loads(jstr)
print(type(electron))
print(electron)

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)
print(type(my_list))
print(my_list)

json_str = '{"me":"Python","pi":3.141592653589,\
            "data":[1, 2, 4, 8],"friend":"JSON","set":null}'
my_dict = json.loads(json_str)
print(type(my_dict))
print(my_dict)
