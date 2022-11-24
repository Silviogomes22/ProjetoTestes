from repositories.book_repositories import BookRepositories

class UserInterface:
    def __init__(self, customer_repository) -> None:
        self.customer_repository = customer_repository

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

    def cadastrar_usuario(self):
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        if (self.customer_repository.create_customer(id, nome)):
            return "Client cadastrado com sucesso!"
        else:
            return "Cliente já"