import json
import ast

class vehicle:
    def __init__(self, registration_number=None, year_of_production=None, passenger=None, mass=None):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

    @classmethod
    def from_input(cls):
        one = input(f"Número de registro: ")
        two = input(f"Ano de produção: ")
        three = input(f"Passenger [y/n]: ")
        four = input(f"Massa do veículo: ")
        if three == "n":
            three = False
        elif three == "y":
            three = True
        try:
            one_val = ast.literal_eval(one)
        except (ValueError, SyntaxError):
            one_val = one
        try:
            two_val = ast.literal_eval(two)
        except (ValueError, SyntaxError):
            two_val = two
        try:
            three_val = ast.literal_eval(three)
        except (ValueError, SyntaxError):
            three_val = three
        try:
            four_val = ast.literal_eval(four)
        except (ValueError, SyntaxError):
            four_val = four
        return cls(registration_number=one_val, year_of_production=two_val, passenger=three_val, mass=four_val)

    def __repr__(self):
        return (
            f"vehicle(registration_number={self.registration_number}, "
            f"year_of_production={self.year_of_production}, "
            f"passenger={self.passenger}, mass={self.mass})"
        )

def encode_vehicle(v):
    if isinstance(v, vehicle):
        return v.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        if {"registration_number", "year_of_production", "passenger", "mass"} <= d.keys():
            return vehicle(**d)
        return d

print("O que eu posso fazer por ti?\n1 - Produzir uma string JSON descrevendo um veículo\n2 - Decodificar uma string JSON em dados de veículo")
choice = input("Tua escolha: ")

if choice == "1":
    veiculo = vehicle.from_input()
    print("Resultado de string JSON é: ")
    print(json.dumps(veiculo, default=encode_vehicle))
elif choice == "2":
    json_str = input("Insira a string JSON do veiculo: ")
    dicionario = json.loads(json_str, cls=MyDecoder)
    print(dicionario)