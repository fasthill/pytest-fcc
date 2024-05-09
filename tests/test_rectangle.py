import pytest

import source.shapes as shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)


def test_area(rectangle):
    assert rectangle.area() == 10 * 20


def test_perimeter(rectangle):
    assert rectangle.perimeter() == (10 + 20) * 2


def test_not_equal(rectangle, weird_rectangle):
    assert rectangle != weird_rectangle
