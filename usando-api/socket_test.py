"""

Objectivo:
    1. Queremos escrever um programa que leia o endereço de um site WWW (por exemplo, pythoninstitute.org) usando a função padrão input() e busca o documento raiz (o documento HTML principal do site WWW) do site especificado;
    2. O programa exibe o documento na tela;
    3. O programa usa TCP para se conectar ao servidor HTTP .

Nosso programa deve executar os seguintes passos:

    - criar um novo soquete capaz de lidar com transmissões orientadas à conexão baseadas em TCP;
    - conectar o soquete ao servidor HTTP de um determinado endereço;
    - enviar uma solicitação ao servidor (o servidor quer saber o que queremos dele)
    - receber a resposta do servidor (conterá o documento raiz solicitado do site)
    - fechar o soquete (encerrar a conexão)
"""

import socket

server_addr = input("Para qual servidor tu queres se conectar? ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando a um servidor
sock.connect((server_addr, 80))

# Solicitando documento do servidor
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(1024)
sock.shutdown(socket.SHUT_RDWR)
sock.close()

print(repr(reply))