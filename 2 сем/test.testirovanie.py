import

class TestSomeModule:


def test_some_func_positive():
    assert some_func(3) == 9
    assert some_func(5) == 4

def test_some_func_negative():
    assert  some_func(5) != 4