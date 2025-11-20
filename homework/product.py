from __future__ import annotations


class Product:
    """Класс товара."""

    __price: float
    # приватный атрибут класса — для выполнения требований SkyPro

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

    # ---------------- STR ----------------
    def __str__(self):
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    # ---------------- PRICE GETTER/SETTER ----------------
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    # ---------------- CLASSMETHOD ----------------
    @classmethod
    def new_product(cls, data: dict) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    # ---------------- ADD ----------------
    def __add__(self, other: "Product") -> float:
        """
        Складывает итоговую стоимость товаров на складе:
        price * quantity + other.price * other.quantity
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity
