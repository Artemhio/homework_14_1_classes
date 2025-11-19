from __future__ import annotations


class Product:
    """
    Класс товара.

    :param name: название товара
    :param description: описание товара
    :param price: цена товара
    :param quantity: количество товара в наличии
    """

    __price: float  # ← приватный атрибут класса (ВАЖНО!)

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

        Если цена <= 0 — выводим сообщение и не обновляем значение.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создаёт продукт из словаря."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
