from utils import FoodContainer


def test_food_container_iterable_empty():
    fc = FoodContainer()
    assert list(fc) == []


def test_food_container_iterable_non_empty():
    fc = FoodContainer()
    fc.add()
    fc.add()
    fc.add()

    assert len(list(fc)) == 3


def test_food_container_iterable_called_multiple_times():
    fc = FoodContainer()
    fc.add()
    fc.add()
    fc.add()

    assert len(list(fc)) == 3
    assert len(list(fc)) == 3
    assert len(list(fc)) == 3
