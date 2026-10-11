from calculator import divide

def test_divide_zero_returns_zero():
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        result = None
    assert result == 0, "Expected divide to return 0 when divisor is zero"