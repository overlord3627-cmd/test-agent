from calculator import divide

def test_normal_division():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(0, 2) == 0
