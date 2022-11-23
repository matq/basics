import pytest

from functions import gest_form


def test_GestForm_WithListOf3_ReturnsGeste():
    assert gest_form([3]) == "Geste"


def test_GestForm_WithListOfNegative3_ReturnsGeste():
    assert gest_form([-3]) == "Geste"


def test_GestForm_WithListOf5_ReturnsForme():
    assert gest_form([5]) == "Forme"


def test_GestForm_WithListOfNegative5_ReturnsForme():
    assert gest_form([-5]) == "Forme"


def test_GestForm_WithListOf15_ReturnsGestForm():
    assert gest_form([15]) == "Gestform"


def test_GestForm_WithListOfNegative15_ReturnsGestForm():
    assert gest_form([-15]) == "Gestform"


def test_GestForm_WithListOf3And15_ReturnsGestForm():
    assert gest_form([3, 15]) == "GesteGestform"


def test_GestForm_WithListOf3And7And15_ReturnsGestForm():
    assert gest_form([3, 7, 15]) == "Geste7Gestform"


def test_GestForm_WithListOfNumberUnder1000_RaisesValueError():
    with pytest.raises(ValueError):
        gest_form([-1001])


def test_GestForm_WithListOfNumberOver1000_RaisesValueError():
    with pytest.raises(ValueError):
        gest_form([1001])


def test_GestForm_WithListOfString_RaisesTypeError():
    with pytest.raises(TypeError):
        gest_form(["wrong type"])
