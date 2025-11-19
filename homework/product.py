from __future__ import annotations


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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает цену товара.

        Если цена меньше или равна нулю, выводит сообщение и
        не меняет цену.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создаёт новый продукт из словаря с полями:
        name, description, price, quantity.
        """
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
