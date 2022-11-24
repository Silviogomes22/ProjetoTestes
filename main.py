from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from entities.UserInterface import UserInterface
from repositories.book_repositories import BookRepositories
from csv_extract import CsvExtract


customer_repository = CustomerRepository()
order_repository = OrderRepository()
csv_extract = CsvExtract()
book_repository = BookRepositories(csv_extract)
book_repository.set_books()
user_interface = UserInterface(customer_repository)

while True:
    menu_option = user_interface.get_interactions()
    if (menu_option == 0):
        break

    print("\n")

    if menu_option == 1:
        print(user_interface.cadastrar_usuario())
    if menu_option == 2:
        id = int(input("Informe o código do pedido: "))
        customer_id = int(input("Informe o código do cliente: "))
        today = date.today()
        if (not customer_repository.verif_if_customer_exists(customer_id, customer_repository)):
            print("Cliente não existe!")
            continue

        customer = customer_repository.get_customer(customer_id, customer_repository)
        book_id = int(input("Informe o código do livro: "))

        if (not book_repository.verif_if_book_exists(book_id)):
            print("Livro não existe!")
            continue

        book = book_repository.get_book(book_id)
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

        for book in book_repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)
