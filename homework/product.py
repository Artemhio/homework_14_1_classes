from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Базовый абстрактный класс для всех продуктов.

    Общая функциональность:
    - name
    - description
    - quantity
    - цена (через абстрактное свойство price)
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
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Цена продукта."""
        raise NotImplementedError

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Возвращает строку вида:
        Product('Продукт1', 'Описание', 1200.0, 10)
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price!r}, {self.quantity!r}"
            ")"
        )


class CreationLoggerMixin:
    """Миксин, печатающий информацию при создании объекта."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # После инициализации всех полей выводим repr объекта
        print(repr(self))


class Product(CreationLoggerMixin, BaseProduct):
    """Класс товара."""

    __price: float

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.__price = price
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.__price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для цены.

        Не даёт установить цену <= 0.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> Product:
        """Создаёт продукт из словаря."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    def __add__(self, other: Product) -> float:
        """
        Складывает итоговую стоимость товаров на складе.

        Разрешено складывать только экземпляры одного и того же класса.
        При попытке сложить разные типы выбрасывается TypeError.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) is not type(other):
            # по условию задачи нужно использовать type()
            raise TypeError("Нельзя складывать продукты разных типов")

        return self.price * self.quantity + other.price * other.quantity
