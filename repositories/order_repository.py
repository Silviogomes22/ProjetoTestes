from entities.order import Order


class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []

    def verif_oder_exist(self,id: int) -> bool:
        for order in self.list_orders:
            if (order.id == id):
                return True
        return False

