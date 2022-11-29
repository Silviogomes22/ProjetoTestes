from datetime import date

from entities.book import Book
from entities.customer import Customer


class Order:
    def __init__(self, id: int, customer: Customer, date_order: date) -> None:
        self.id = id
        self.customer = customer
        self.date_order = date_order
        self.purchased_book: Book
        self.total_price: float = 0

    def adicionar_livro(self, livro: Book) -> bool:
        if (livro.get_stock() == 0 or livro.verif_preco_invalido()):
            return False
        self.purchased_book = livro
        livro.baixar_estoque()
        return True