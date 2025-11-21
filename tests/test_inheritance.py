from homework.category import Category
from homework.lawngrass import LawnGrass
from homework.product import Product
from homework.smartphone import Smartphone
import pytest


def test_smartphone_is_product() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    assert isinstance(smartphone, Product)
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256


def test_lawngrass_is_product() -> None:
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert isinstance(grass, Product)
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"


def test_add_same_product_types() -> None:
    p1 = Smartphone("A", "d", 100.0, 2, 90.0, "M1", 128, "Black")
    p2 = Smartphone("B", "d", 200.0, 3, 92.0, "M2", 256, "White")

    result = p1 + p2
    assert result == 100.0 * 2 + 200.0 * 3


def test_add_different_product_types_raises_type_error() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    with pytest.raises(TypeError):
        _ = smartphone + grass


def test_category_adds_only_products_or_subclasses() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    category = Category("Товары", "Описание", [smartphone])
    category.add_product(grass)

    with pytest.raises(TypeError):
        category.add_product("Not a product")
