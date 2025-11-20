from homework.product import Product


def test_product_str():
    p = Product("Test", "desc", 100.0, 5)
    assert str(p) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_add():
    p1 = Product("A", "d", 100.0, 10)
    p2 = Product("B", "d", 200.0, 2)
    assert p1 + p2 == 1000 + 400
    