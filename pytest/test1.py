import unittest
#import pytest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
def func(x):
    return x+1
def test_answer():
    assert func(3)==5

if __name__ == '__main__':
    #unittest.main()
    a= test_answer()
    print a
