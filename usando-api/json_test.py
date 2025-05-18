import json

# """""""""""""""""""""""""""""""" Python to JSON """"""""""""""""""""""""""""""""
electron = 1.602176620898E10
print(json.dumps(electron))

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """""""""""""""""""""""""""""""" JSON to Python """"""""""""""""""""""""""""""""
jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
comics = json.loads(jstr)
print(type(comics))
print(comics)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Usando dicionário como destino para a mensagem JSON. Primeira serialização!
class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """"""""""""""""""" Desserializar de JSON para Python, função: """"""""""""""""
def decode_who(w):
    return Who(w['name'], w['age'])

old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# """""""""""""""""""""""""" Desserialização de objecto """"""""""""""""""""""""""""""""
class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_whois)

    def decode_whois(self, d):
        return Who(**d)

some_m = Who('Jane Doe', 23)
json_str = json.dumps(some_m, cls=MyEncoder)
new_m = json.loads(json_str, cls=MyDecoder)

print(type(new_m))
print(new_m.__dict__)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""