import pytest

from functions import binary_gap


def test_BinaryGap_With1041_Returns5():
    assert binary_gap(1041) == 5


def test_BinaryGap_With32_Returns0():
    assert binary_gap(32) == 0


def test_BinaryGap_With15_Returns0():
    assert binary_gap(15) == 0


def test_BinaryGap_With561892_Returns3():
    assert binary_gap(561892) == 3


def test_BinaryGap_With74901729_Returns4():
    assert binary_gap(74901729) == 4


def test_BinaryGap_WithString_RaisesTypeError():
    with pytest.raises(TypeError):
        binary_gap("wrong type")
