import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1) # solicita o index do servidor json, podendo ser outro endereço
except requests.exceptions.Timeout:
    print("Desculpe! Você não obteve seus dados.")
except:
    print("Conexão falhada!")
else:
    print("Aqui está seus dados: ")
    print(reply.status_code) # imprime o status da solicitação. Código 200 quer dizer que está tudo OK!
    print(reply.headers) # imprime o cabeçalho
    print(reply.text) # imprime o conteúdo