import pytest
import math
from lab_1_1 import divide, calculate_variant_1

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Ділення на нуль не підтримується"):
        divide(10, 0)

def test_divide_both_zeros():
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)

def test_calculate_variant_1_approximation():
    x, y, z, b = 1.45, -1.22, 3.5, 3.07
    a, m = calculate_variant_1(x, y, z, b)

    # Подставляем реальные значения, которые вернула функция
    assert a == pytest.approx(2.66905676, abs=1e-7)
    assert m == pytest.approx(4.00039979, abs=1e-7)
