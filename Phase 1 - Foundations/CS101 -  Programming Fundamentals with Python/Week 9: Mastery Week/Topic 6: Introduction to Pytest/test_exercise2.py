import pytest
from exercise2 import calculate_average

def test_average():
    assert calculate_average([1, 2, 3] ) == 2.0
    assert calculate_average([5, 10]) == 7.5
    assert calculate_average([0]) == 0.0

    with pytest.raises(ValueError):
        calculate_average([])
