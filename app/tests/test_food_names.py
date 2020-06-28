import pytest

from app.foodname import FoodName


def test_same_string():
    s = "this is a test name"
    fn = FoodName()
    assert fn.generate(s) == fn.generate(s)


def test_different_string():
    s1 = "this is a test name"
    s2 = "this is a different name"
    fn = FoodName()
    assert fn.generate(s1) != fn.generate(s2)
