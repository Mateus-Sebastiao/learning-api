import json
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'close'}
h_content = {'Content-type': 'application/json'}
# Dict para criar um novo carro (1)
"""
new_car = {'id': '8',
           'brand': 'Porsche',
           'model': '911',
           'production_year': 1963,
           'convertible': False}
print(json.dumps(new_car))
"""
# Dict para atualizar um carro existente (2)
"""
car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1967,
       'convertible': True}
"""
try:
    # # Apagando um carro abaixo ----------------------------
    # reply = requests.delete('http://localhost:3000/cars/8')
    ## (1) Criando um novo carro abaixo --------------------------------------------------------------
    # reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
    ## (2) ## Actualizano um carro existente -------------------------------------------------------
    # reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
    ## ## ## ## Vendo o status da reposta, para qualquer linha acima descomentada, descomentar esta...
    # print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars', headers=h_close)
except requests.RequestException:
    print("Erro de Comunicação!")
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.OK:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Recurso não encontrado!")
    else:
        print("Erro de servidor!")