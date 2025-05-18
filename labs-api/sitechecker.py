import sys
import socket

def connection(server_addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, port))

    sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
            bytes(server_addr, "utf8") +
            b"\r\nConnection: close\r\n\r\n")
    reply = sock.recv(1024).decode(errors="ignore")

    status_line = reply.splitlines()[0]
    print(status_line)

if len(sys.argv) not in [2, 3]:
    print("Número inapropriado de argumentos: no mínimo um é solicitado e não mais do que dois são permitidos:\n-Endereço do servidor http (obrigatório)\n-Número de porta (porta 80 se não especificada)")
    sys.exit(1)
elif len(sys.argv) == 2:
    server_addr = sys.argv[1]
    port = 80
    connection(server_addr, port)
elif len(sys.argv) in [2, 3]: 
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Número de porta está inválido - saindo")
            sys.exit(2)    
        if isinstance(port, int): 
            if (not(port >= 1 and port <= 65535)):
                print("Número de porta está inválido - saindo")
                sys.exit(2)
            
            else:
                server_addr = sys.argv[1]
                connection(server_addr, port)