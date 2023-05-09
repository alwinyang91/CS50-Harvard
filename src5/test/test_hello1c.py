from hello1 import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"

'''
with __init__.py in the folder test, 
now you can run:
% pytest test
'''