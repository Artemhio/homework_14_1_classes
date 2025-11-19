class Product:
    """
    Класс товара.

    :param name: название товара
    :param description: описание товара
    :param price: цена товара (с копейками)
    :param quantity: количество товара в наличии (в штуках)
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
