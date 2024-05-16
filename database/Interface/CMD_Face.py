from os import system as Cmd
from .SQL_Interface import DB
from colorama import Fore as paint
class DB_CMD:
    def __init__(self, path):
        self.db = DB(path)

    def cmd_search_name(self):
        Cmd("cls")
        print(f"Digite o nome que deseja pesquisar")
        request = input("Pesquisar: ")
        print(f"Pesquisando <{request}>...")
        response = self.db.search_name(request)

        if not len(response) == 0:
            for k, v in enumerate(response):
                print(f"{k} {paint.LIGHTGREEN_EX}{v}{paint.RESET}")
        else:
            print(f"{paint.RED}Nenhum item foi achado{paint.RESET} => {len(response)}")
        input("Digite qualquer coisa para sair: ")

    def cmd_search_position(self):
        Cmd("cls")
        print(f"Digite a quantidade de votos")
        while True:
            request = input(f"Votos: ")
            if request.isdigit():
                break
            print(f"{paint.RED}Só aceitamos números!!!{paint.RESET}")
        print(f"Pesquisando votos = {request}")
        response = self.db.seach_vote(int(request))
        if not len(response) == 0:
            for k, v in enumerate(response):
                print(f"{k} {paint.LIGHTGREEN_EX}{v}{paint.RESET}")
        else:
            print(f"{paint.RESET}Não a ninguém com esse número de votos {request}{paint.RESET}")
        input("Digite qualquer coisa para sair: ")

    def cmd_search_vote(self):
        Cmd("cls")
        print(f"Digite a quantidade de votos")
        while True:
            request = input(f"Position[1/1816]: ")
            if request.isdigit():
                request_int = int(request)
                if request_int <= 1816 and request_int >= 1:
                    break
                else:
                    print(f"{paint.RED}Digite uma posição valida{paint.RED}")
            print(f"{paint.RED}Só aceitamos números!!!{paint.RESET}")
        print(f"Pesquisando votos = {request_int}")
        response = self.db.search_position(request_int)
        if not len(response) == 0:
            for k, v in enumerate(response):
                print(f"{k} {paint.LIGHTGREEN_EX}{v}{paint.RESET}")
        else:
            print(f"{paint.RESET}Não a ninguém com esse número de votos {request}{paint.RESET}")
        input("Digite qualquer coisa para sair: ")

    def cmd_search_repo(self):
        Cmd("cls")
        print(f"Digite a pesquisa do repositorio")
        request = input("Pesquisar: ")
        print(f"Pesquisando <{request}>...")
        response = self.db.search_repo(request)

        if not len(response) == 0:
            for k, x in enumerate(response):
                print(f"{k} {paint.LIGHTGREEN_EX}{v}{paint.RESET}")
        else:
            print(f"{paint.RED}Nenhum item foi achado{paint.RESET} => {len(response)}")
        input("Digite qualquer coisa para sair: ")


    def cmd_get_all(self):
        Cmd("cls")
        response = self.db.get_all()
        for x in response:
            print(f"{paint.LIGHTGREEN_EX}[{x[0]}] nome: {x[1]} || votos: {x[2]} => repositorio: {x[3]}")

    def cmd_get_repo(self):
        Cmd("cls")
        response = self.db.get_link()
        for x in response:
            print(f"{paint.LIGHTGREEN_EX}[{x[0]}]{paint.RESET}")

    def cmd_get_name(self):
        Cmd("cls")
        response = self.db.get_name()
        for x in response:
            print(f"{paint.LIGHTGREEN_EX}[{x[0]}]{paint.RESET}")

    def cmd_get_vote(self):
        Cmd("cls")
        response = self.db.get_votes()
        for x in response:
            print(f"{paint.LIGHTGREEN_EX}[{x[0]}]{paint.RESET}")

    def cmd_get_position(self):
        Cmd("cls")
        response = self.db.get_position()
        for x in response:
            print(f"{paint.LIGHTGREEN_EX}[{x[0]}]{paint.RESET}")