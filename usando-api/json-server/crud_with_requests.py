import requests

try:
    reply = requests.get('http://localhost:3000/cars') # Solicitando no servidor
except requests.RequestException:
    print("Erro de Comunicação!") # Se gerar algum erro, retornará este print
else:
    if reply.status_code == requests.codes.OK: 
        print(reply.text) # Se o código da solicitação for 200, que é OK, que quer dizer que a comunicação foi bem sucedida, esse print será impresso!
        print(reply.headers['content-type'])
        print(reply.json())
    else:
        print("Erro de Servidor!") # Senão retornar o código 200, deve ter retornado alguma outra coisa, daí esse print.

