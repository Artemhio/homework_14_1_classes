from homework.product import Product
from homework.category import Category


def test_category_init_and_counters() -> None:
    # сбрасываем счётчики, чтобы тест был детерминированным
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("P1", "desc1", 100.0, 1)
    product2 = Product("P2", "desc2", 200.0, 2)
    product3 = Product("P3", "desc3", 300.0, 3)

    category = Category(
        "Смартфоны", "Описание",
        [product1, product2, product3]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Описание"

    # категория одна
    assert Category.category_count == 1
    # товаров всего 3
    assert Category.product_count == 3


def test_add_product_and_products_property() -> None:
    # сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Телевизоры", "Описание", [])

    assert Category.category_count == 1
    assert Category.product_count == 0

    product1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    product2 = Product("OLED", "Другое описание", 150000.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    # после добавления двух товаров
    assert Category.product_count == 2

    expected = (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
        "OLED, 150000.0 руб. Остаток: 3 шт.\n"
    )

    assert category.products == expected
