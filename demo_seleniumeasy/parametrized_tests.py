import pytest


@pytest.mark.parametrize("first_value, second_value, result_value", [(10, 15, 25), (22, 33, 55), (21, 12, 33)])
def test_multiplication_11(first_value, second_value, result_value):
   assert first_value + second_value == result_value
