
# Assuming ciap.py has the following content:
# def add(a, b):
#     return a + b

from ciap import add

def test_add():
    assert add(2, 3) == 5
