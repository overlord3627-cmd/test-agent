from calculator import divide
def test_zero_and_normal_division():
    assert divide(10, 0) == 0
    assert divide(0, 0) == 0
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
