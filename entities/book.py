class Book:
    def __init__(self, id: int, name: str, isbn: str, author: str, category: str, price: float) -> None:
        self.id = id
        self.name = name
        self.isbn = isbn
        self.author = author
        self.category = category
        self.price = price
        self.stock: int = 1

    def verif_preco_invalido(self):
        return self.price == 0

    def baixar_estoque(self):
        if(self.stock > 0):
            self.stock -= 1

    def get_stock(self):
        return self.stock