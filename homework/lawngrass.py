from __future__ import annotations

from homework.product import Product


class LawnGrass(Product):
    """
    Класс газонной травы, наследуется от Product.

    Дополнительные атрибуты:
    - country: страна-производитель
    - germination_period: срок прорастания
    - color: цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
