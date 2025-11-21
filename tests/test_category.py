from homework.product import Product
from homework.category import Category


def test_category_init_and_counters() -> None:
    # сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("A", "desc", 10.0, 1)
    category = Category("Phones", "desc", [p1])

    assert category.name == "Phones"
    assert category.description == "desc"
    assert Category.category_count == 1
    assert Category.product_count == 1

    expected = "A, 10.0 руб. Остаток: 1 шт.\n"
    assert category.products == expected


def test_category_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("A", "d1", 10.0, 1)
    p2 = Product("B", "d2", 20.0, 2)

    Category("Phones", "desc", [p1])
    Category("TV", "desc2", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_middle_price_non_empty_category() -> None:
    p1 = Product("A", "desc", 100.0, 1)
    p2 = Product("B", "desc", 200.0, 1)
    category = Category("Phones", "desc", [p1, p2])

    assert category.middle_price() == 150.0


def test_middle_price_empty_category_returns_zero() -> None:
    category = Category("Empty", "desc", [])

    assert category.middle_price() == 0.0
