import re

from homework.product import BaseProduct, Product
from homework.smartphone import Smartphone
from homework.lawngrass import LawnGrass


def test_product_is_subclass_of_baseproduct() -> None:
    assert issubclass(Product, BaseProduct)


def test_smartphone_and_lawngrass_are_products() -> None:
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_creation_logger_mixin_prints_on_init(capsys) -> None:
    product = Product("Test", "Desc", 100.0, 2)
    captured = capsys.readouterr()

    # Ожидаем строку вида Product('Test', 'Desc', 100.0, 2)
    pattern = r"Product\('Test', 'Desc', 100\.0, 2\)"
    assert re.search(pattern, captured.out) is not None
    assert product.price == 100.0
    assert product.quantity == 2
