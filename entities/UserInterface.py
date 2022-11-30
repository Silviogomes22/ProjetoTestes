from datetime import date
from entities.order import Order

class UserInterface:
    def __init__(self, customer_repository, book_repository, order_repository) -> None:
        self.customer_repository = customer_repository
        self.book_repository = book_repository
        self.order_repository = order_repository

    def principal_menu(self) -> None:
        return '''1 - Cadastrar cliente
2 - Fazer pedido
3 - Relatório de Pedidos
4 - Relatório de Clientes
5 - Relatório de Livros
0 - Sair'''

    def get_interactions(self) -> int:
        try:
            return int(input("Informe a opção do menu: "))
        except:
            return -1

    def cadastrar_usuario(self):
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        if (self.customer_repository.create_customer(id, nome)):
            return "Client cadastrado com sucesso!"
        else:
            return "Cliente já cadastrado"

    def fazer_pedido(self):
        order_id = int(input("Informe o código do pedido: "))
            
        customer_id = int(input("Informe o código do cliente: "))
        today = date.today()

        if (not self.customer_repository.verif_if_customer_exists(customer_id)):
            return "Cliente não existe!"

        customer = self.customer_repository.get_customer(customer_id)
        book_id = int(input("Informe o código do livro: "))

        if (not self.book_repository.verif_if_book_exists(book_id)):
            return "Livro não existe!"

        book = self.book_repository.get_book(book_id)

        if (not self.order_repository.create_order(order_id, customer, today)):
            return "Pedido existente"

        order = self.order_repository.get_order(order_id)
        if (order.adicionar_livro(book)):
            self.order_repository.list_orders.append(order)
            return "Pedido cadastrado com sucesso!"
        else:
            return "Livro indisponível"

    def relatorio_de_pedidos(self):
        buffer = "***** Relatório de pedidos *****"
        for order in self.order_repository.list_orders:
            buffer += f'''\nCódigo do Pedido: {order.id}
Cliente: {order.customer.name}
Data do Pedido: {order.date_order}
Livro Escolhido: {order.purchased_book.name}             
'''
        return buffer

    def relatorio_de_clientes(self):
        formatText = "{0:<10} {1:<20}\n"
        menu = ("\n***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in self.customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        return menu

    def relatorio_de_livros(self):
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Título", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")

        for book in self.book_repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        return menu