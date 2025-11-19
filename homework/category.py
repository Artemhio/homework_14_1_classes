from __future__ import annotations

from typing import List

from .product import Product


class Category:
    """
    Класс категории товаров.

    :param name: название категории
    :param description: описание категории
    :param products: список товаров (объекты Product)
    """

    category_count: int = 0
    product_count: int = 0


    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []

        # учёт категории
        Category.category_count += 1

        # добавляем стартовые товары через add_product,
        # чтобы корректно обновился product_count
        for product in products:
            self.add_product(product)


    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в приватный список товаров категории.
        """
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        """
        Возвращает список товаров в виде строк:

        'Название продукта, 80 руб. Остаток: 15 шт.'
        Каждая запись с новой строки.
        """
        lines: list[str] = []

        for product in self.__products:
            line = (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт."
            )
            lines.append(line)

        return "\n".join(lines)
