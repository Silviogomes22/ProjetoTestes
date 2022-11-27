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
user_interface = UserInterface(customer_repository, book_repository, order_repository)

while True:
    print(user_interface.principal_menu())
    menu_option = user_interface.get_interactions()
    if (menu_option == 0):
        break
    if menu_option == -1:
        print("A opção informada é inválida, o programa vai ser encerrado...")
        break

    print("\n")

    if menu_option == 1:
        print(user_interface.cadastrar_usuario())
    if menu_option == 2:
        print(user_interface.fazer_pedido())
    if menu_option == 3:
        print(user_interface.relatorio_de_pedidos())
    if menu_option == 4:
        print(user_interface.relatorio_de_clientes())
    if menu_option == 5:
        print(user_interface.relatorio_de_livros())