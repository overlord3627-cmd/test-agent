from calculator import divide

def test_divide_returns_zero_on_zero_denominator():
    assert divide(10, 0) == 0