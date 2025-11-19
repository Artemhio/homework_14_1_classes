from homework.product import Product
from homework.category import Category


def test_category_init():
    p1 = Product("A", "desc", 10.0, 1)
    c = Category("Phones", "desc", [p1])

    assert c.name == "Phones"
    assert c.description == "desc"
    assert len(c.products) == 1


def test_category_counters():
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("A", "d", 1.0, 1)
    p2 = Product("B", "d", 2.0, 2)

    Category("Phones", "d", [p1])
    Category("Audio", "d", [p2])

    assert Category.category_count == 2
    assert Category.product_count == 2
