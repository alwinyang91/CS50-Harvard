from hello0 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


'''
does not work, because hello function does not return anything
'''