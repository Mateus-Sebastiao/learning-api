import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Uso: python script.py <endereço> [porta]")
    sys.exit(1)

# Argumentos
server = sys.argv[1]
port = 80 if len(sys.argv) == 2 else int(sys.argv[2])

# Remove http:// se presente
if server.startswith("http://"):
    server = server[len("http://"):]

# Monta URL
url = f"http://{server}:{port}"

try:
    response = requests.head(url, timeout=5)
except requests.RequestException as e:
    print("Erro de comunicação:", e)
    sys.exit(2)

if response.status_code == 200:
    print("Servidor respondeu OK!")
    print("Content-Type:", response.headers.get("Content-Type", "desconhecido"))
else:
    print(f"Servidor respondeu com erro HTTP {response.status_code}")
