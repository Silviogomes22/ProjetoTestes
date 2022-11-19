from repositories.book_repositories import BookRepositories

class UserInterface:
    def __init__(self, book_repositories: BookRepositories) -> None:
        self.book_repositories = book_repositories

    def principal_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0

    def get_interactions(self):
        menu_option = self.principal_menu()
        if (menu_option == 0):
            return False

        print("\n")

        def cadastrar cliente
            id = int(input("Informe o código do cliente: "))
            nome = input("Informe o nome do cliente: ")
            customer = Customer(id, nome)
            customer_repository.list_customers.append(customer)
            print("Client cadastrado com sucesso!")

        def cadastrar produto
            id = int(input("Informe o código do pedido: "))
            customer_id = int(input("Informe o código do cliente: "))
            today = date.today()
            if (not verif_if_customer_exists(customer_id, customer_repository)):
                print("Cliente não existe!")
                continue

            customer = get_customer(customer_id, customer_repository)
            book_id = int(input("Informe o código do livro: "))

            if (not verif_if_book_exists(book_id)):
                print("Livro não existe!")
                continue

            book = get_book(book_id)
            order = Order(id, customer, today)
            order.purchased_book = book

            order_repository.list_orders.append(order)
            print("Pedido cadastrado com sucesso!")
        if menu_option == 3:
            print("\n***** Relatório de pedidos *****\n")
            for order in order_repository.list_orders:
                print(f"Código do Pedido: {order.id}")
                print(f"Cliente: {order.customer.name}")
                print(f"Data do pedido: {order.date_order}")
                print(f"Livro escolhido: {order.purchased_book.name} \n")
        if menu_option == 4:
            formatText = "{0:<10} {1:<20}\n"
            menu = ("\n***** Relatório de clientes *****\n")
            menu += formatText.format("Id", "Cliente")

            for customer in customer_repository.list_customers:
                menu += formatText.format(customer.id, customer.name)
            print(menu)
        if menu_option == 5:
            formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
            menu = ("\n***** Relatório de livros cadastrados *****\n")
            menu += formatText.format("Id", "Ttítulo", "ISBN",
                                      "Autor", "Assunto", "Valor", "Estoque")

            for book in list_books:
                menu += formatText.format(book.id, book.name, book.isbn,
                                          book.author, book.category, book.price, book.stock)
            print(menu)