import sys
import requests

def buscar_atividade(username):
    """
    Faz uma requisição à API do GitHub para obter as atividades públicas do usuário.
    """
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        resposta = requests.get(url, headers=headers)

        if resposta.status_code == 404:
            print(f"Usuário '{username}' não encontrado.")
            return
        elif resposta.status_code != 200:
            print(f"Erro ao acessar API do GitHub (status: {resposta.status_code})")
            return

        eventos = resposta.json()
        if not eventos:
            print(f"Nenhuma atividade recente encontrada para '{username}'.")
            return

        print(f"Atividades recentes de {username}:\n")

        for evento in eventos:
            tipo = evento['type']
            repo = evento['repo']['name']

            if tipo == "PushEvent":
                commits = len(evento['payload']['commits'])
                print(f"- Pushed {commits} commit(s) to {repo}")

            elif tipo == "IssuesEvent":
                acao = evento['payload']['action']
                print(f"- {acao.capitalize()} an issue in {repo}")

            elif tipo == "IssueCommentEvent":
                print(f"- Commented on an issue in {repo}")

            elif tipo == "WatchEvent":
                print(f"- Starred {repo}")

            elif tipo == "ForkEvent":
                print(f"- Forked {repo}")

            elif tipo == "CreateEvent":
                ref_type = evento['payload'].get('ref_type', 'repository')
                print(f"- Created a new {ref_type} in {repo}")

            elif tipo == "PullRequestEvent":
                acao = evento['payload']['action']
                print(f"- {acao.capitalize()} a pull request in {repo}")

            else:
                print(f"- {tipo} in {repo}")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

def main():
    """
    Função principal: lê argumentos da linha de comando e chama a função de busca.
    """
    if len(sys.argv) != 2:
        print("Uso: github_activity <nome_de_usuário>")
        sys.exit(1)

    username = sys.argv[1]
    buscar_atividade(username)

if __name__ == "__main__":
    main()