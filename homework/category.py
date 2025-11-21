from __future__ import annotations

from typing import List

from homework.product import Product


class Category:
    """Класс категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []

        Category.category_count += 1

        # добавляем стартовые товары через add_product,
        # чтобы сработали все проверки и счётчики
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.

        Разрешены только объекты Product и его наследников.
        В остальных случаях выбрасывается TypeError.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты "
                "Product или его наследников"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает строку со всеми продуктами вида:
        'Название продукта, X руб. Остаток: Y шт.\n'
        """
        return "".join(str(product) + "\n" for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строку вида:
        'Название категории, количество продуктов: X шт.'
        """
        total_quantity = sum(product.quantity for product in self.__products)
        prefix = f"{self.name}, количество продуктов: "
        return f"{prefix}{total_quantity} шт."

    def middle_price(self) -> float:
        """
        Возвращает среднюю цену товаров в категории.

        Складывает price всех товаров и делит на их количество.
        Если товаров нет, возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            count = len(self.__products)
            return total_price / count
        except ZeroDivisionError:
            return 0.0
