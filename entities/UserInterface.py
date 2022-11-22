from repositories.book_repositories import BookRepositories

class UserInterface:
    def __init__(self) -> None:
        pass

    def principal_menu(self) -> int:
        print("1 - Cadastrar cliente")
        print("2 - Fazer pedido")
        print("3 - Relatório de Pedidos")
        print("4 - Relatório de Clientes")
        print("5 - Relatório de Livros")
        print("0 - Sair")

    def get_interactions(self):
        try:
            self.principal_menu()
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0