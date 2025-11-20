from homework.product import Product
from homework.category import Category


def test_category_str():
    p1 = Product("A", "d", 10.0, 1)
    p2 = Product("B", "d", 20.0, 3)
    cat = Category("Phones", "desc", [p1, p2])

    assert str(cat) == "Phones, количество продуктов: 4 шт."
