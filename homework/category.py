from __future__ import annotations
from homework.product import Product


class Category:
    """Класс категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products[:]       # приватный список
        Category.category_count += 1
        Category.product_count += len(products)

    # ---------------- ADD PRODUCT ----------------
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    # ---------------- PRODUCTS GETTER ----------------
    @property
    def products(self) -> str:
        return "".join(str(p) + "\n" for p in self.__products)

    # ---------------- STR ----------------
    def __str__(self) -> str:
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
