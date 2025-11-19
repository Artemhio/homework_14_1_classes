from homework.product import Product
from homework.category import Category


def test_category_init_and_counters() -> None:
    # сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("A", "desc", 10.0, 1)
    c = Category("Phones", "desc", [p1])

    assert c.name == "Phones"
    assert c.description == "desc"
    assert Category.category_count == 1
    assert Category.product_count == 1

    # products теперь строка
    expected = "A, 10.0 руб. Остаток: 1 шт.\n"
    assert c.products == expected


def test_category_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("A", "d1", 10.0, 1)
    p2 = Product("B", "d2", 20.0, 2)

    c1 = Category("Phones", "desc", [p1])
    c2 = Category("TV", "desc2", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2
