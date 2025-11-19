from homework.product import Product


def test_product_init():
    p = Product("iPhone", "phone", 120000.0, 3)
    assert p.name == "iPhone"
    assert p.description == "phone"
    assert p.price == 120000.0
    assert p.quantity == 3
