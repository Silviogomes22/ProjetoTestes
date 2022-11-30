'''Verificar se o estoque do livro foi baixado
Não permitir inserir um código de cliente que já existe
Não permitir inserir um código de pedido que já existe
Não permitir vender um livro com valor zerado
Não permitir fazer um pedido sem cliente
Não permitir um pedido sem livro
Só é permitido informar UM pedido no pedido
Caso o formato do valor do esteja errado retornar 0
Não permitir vender o mesmo livro novamente, pois a livraria só possui 1 estoque
Verificar se o código do livro que está sendo vendido, existe, caso não exista aborta o pedido e volta para o menu'''
from repositories.order_repository import OrderRepository
from repositories.book_repositories import BookRepositories
from  repositories.customer_repository import CustomerRepository
from entities.order import Order
from entities.book import Book
from entities.customer import Customer
from datetime import date
from csv_extract import CsvExtract


def test_stock():
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    order_repository = OrderRepository()
    customer_repository = CustomerRepository()
    order_id = 1
    customer_id = 1
    today = date.today()
    customer = customer_repository.get_customer(customer_id)
    book_id = 5
    book = book_repository.get_book(book_id)
    order = Order(order_id, customer, today)

    # Act
    if (order.adicionar_livro(book)):
        order_repository.list_orders.append(order)

    # Assert
    assert book.stock == 0

def test_cod_cliente():
    # Assert
    customer_one = 1
    customer_two = 1
    customer_repository = CustomerRepository()
    
    # Act
    primeiro = customer_repository.create_customer(customer_one, "Alberto")
    segundo = customer_repository.create_customer(customer_two, "Bruno")

    # Assert
    assert segundo == False

def test_cod_pedido():
    # Assert
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    order_one = 1
    order_two = 1
    order_repository = OrderRepository()
    customer = Customer(1, "Alberto")
    today = date.today()
    book_one = book_repository.get_book(5)
    book_two = book_repository.get_book(7)

    # Act
    primeiro = order_repository.create_order(order_one, customer, today, book_one)
    segundo = order_repository.create_order(order_two, customer, today, book_two)

    # Assert
    assert primeiro == "Pedido cadastrado com sucesso"
    assert segundo == "Pedido já existe"

def test_livro_zerado():
    # Assert
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer = Customer(1, "Alberto")
    today = date.today()
    order_repository = OrderRepository()
    book_one = book_repository.get_book(1)
    book_two = book_repository.get_book(2)

    # Act
    primeiro = order_repository.create_order(1, customer, today, book_one)
    segundo = order_repository.create_order(2, customer, today, book_two)

    # Assert
    assert segundo == "Pedido cadastrado com sucesso"
    assert primeiro == "Livro com preço inválido"

def test_compra_dupla():
    # Assert
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer = Customer(1, "Alberto")
    customer_two = Customer(2, "Bruno")
    today = date.today()
    order_repository = OrderRepository()
    book_one = book_repository.get_book(2)

    # Act
    primeiro = order_repository.create_order(1, customer, today, book_one)
    segundo = order_repository.create_order(2, customer_two, today, book_one)

    # Assert
    assert primeiro == "Pedido cadastrado com sucesso"
    assert segundo == "Livro sem estoque"