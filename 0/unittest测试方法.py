import unittest
from my_calculator import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5,3),8)

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5,3),-1)

#然后在终端里面输入 python -m unittest
#就可以测试结果