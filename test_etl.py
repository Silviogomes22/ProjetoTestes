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
from entities.UserInterface import UserInterface
from pytest import MonkeyPatch

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

    # Act
    order_repository.create_order(order_id, customer, today, book)

    # Assert
    assert book.stock == 0

def test_cod_cliente():
    # Arrange
    customer_one = 1
    customer_two = 1
    customer_repository = CustomerRepository()
    
    # Act
    primeiro = customer_repository.create_customer(customer_one, "Alberto")
    segundo = customer_repository.create_customer(customer_two, "Bruno")

    # Assert
    assert primeiro == True
    assert segundo == False

def test_cod_pedido():
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    order_repository = OrderRepository()
    customer_repository = CustomerRepository()
    user_interface = UserInterface(customer_repository, book_repository, order_repository)
    
    order_one = 1
    order_two = 1
    customer = Customer(1, "Alberto")
    today = date.today()
    book_one = book_repository.get_book(5)
    book_two = book_repository.get_book(7)

    # Act
    primeiro = order_repository.create_order(order_one, customer, today, book_one)
    segundo = order_repository.create_order(order_two, customer, today, book_two)

    # Assert
    assert primeiro == True
    assert segundo == False

def test_livro_zerado(monkeypatch: MonkeyPatch):
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer_repository = CustomerRepository()
    customer_repository.create_customer(1, "Alberto")
    today = date.today()
    order_repository = OrderRepository()
    user_interface = UserInterface(customer_repository, book_repository, order_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "1") # Pedido, cliente e código do livro com valor zerado
    resultado = user_interface.fazer_pedido()

    # Assert
    assert resultado == "Livro com preço inválido"

def test_compra_sem_cliente(monkeypatch: MonkeyPatch):
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer = Customer(2, "Alberto")
    customer_repository = CustomerRepository() # Repositório sem cliente
    today = date.today()
    order_repository = OrderRepository()
    respostas = iter(['1', '', '2']) # Pedido, cliente nulo e código do livro
    user_interface = UserInterface(customer_repository, book_repository, order_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: next(respostas)) # Pedido, cliente e código do livro com valor zerado
    resultado = user_interface.fazer_pedido()

    # Assert
    assert resultado == "Pedido não pode ser feito sem cliente"

def test_compra_sem_livro(monkeypatch: MonkeyPatch):
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer_repository = CustomerRepository() 
    customer_repository.create_customer(1, "Alberto")
    today = date.today()
    order_repository = OrderRepository()
    respostas = iter(['1', '1', '']) # Pedido, cliente e código do livro vazio
    user_interface = UserInterface(customer_repository, book_repository, order_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: next(respostas)) # Pedido, cliente e código do livro com valor zerado
    resultado = user_interface.fazer_pedido()

    # Assert
    assert resultado == "Pedido não pode ser feito sem livro"

def test_format_str_price_to_float():
    # Arrange
    csv_extract = CsvExtract()
    valor_invalido = "R$ 1,29,00"

    # Act
    novo_valor = csv_extract.format_str_price_to_float(valor_invalido)

    # Assert
    novo_valor == 0


def test_compra_dupla(monkeypatch: MonkeyPatch):
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer_repository = CustomerRepository()
    customer_repository.create_customer(1, 'Alberto')
    customer_repository.create_customer(2, 'Bruno')
    today = date.today()
    order_repository = OrderRepository()
    user_interface = UserInterface(customer_repository, book_repository, order_repository)
    respostas1 = iter(['1', '1', '5']) # Pedido, cliente e código do livro
    respostas2 = iter(['2', '2', '5']) # Pedido, cliente e código do livro repetido

    # Act
    monkeypatch.setattr("builtins.input", lambda _: next(respostas1))
    pedido1 = user_interface.fazer_pedido()
    monkeypatch.setattr("builtins.input", lambda _: next(respostas2))
    pedido2 = user_interface.fazer_pedido()

    # Assert
    assert pedido1 == "Pedido cadastrado com sucesso"
    assert pedido2 == "Livro sem estoque"

def test_compra_livro_inexistente(monkeypatch: MonkeyPatch):
    # Arrange
    csv_extract = CsvExtract()
    book_repository = BookRepositories(csv_extract)
    book_repository.set_books()
    customer_repository = CustomerRepository() 
    customer_repository.create_customer(1, "Alberto")
    today = date.today()
    order_repository = OrderRepository()
    respostas = iter(['1', '1', '700']) # Pedido, cliente e código do livro inexistente
    user_interface = UserInterface(customer_repository, book_repository, order_repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: next(respostas)) # Pedido, cliente e código do livro com valor zerado
    resultado = user_interface.fazer_pedido()

    # Assert
    assert resultado == "Livro não existe!"