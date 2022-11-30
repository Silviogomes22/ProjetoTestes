from entities.order import Order
from entities.customer import Customer
from datetime import date
from entities.book import Book

class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []

    def verif_oder_exist(self,id: int) -> bool:
        for order in self.list_orders:
            if (order.id == id):
                return True
        return False

    def create_order(self, id: int, customer: Customer, date_order: date, livro: Book):
        if(self.verif_oder_exist(id)):
           return "Pedido já existe"
        order = Order(id, customer, date_order)
        status = order.adicionar_livro(livro)
        if (status == "Livro adicionado"):
            self.list_orders.append(order)
            return "Pedido cadastrado com sucesso"
        return status
    
    def get_order(self, id):
        for order in self.list_orders:
            if (order.id == id):
                return order
