import unittest
from shopping_list import shopping_list

class ShoppingListTest(unittest.TestCase):
    def setUp(self):
        self.shopping_list = shopping_list({"zj":8,"mz":30})

    def test_positive(self):
        self.assertEqual(self.shopping_list.item_count(),2)

    def test_negative(self):
        self.assertEqual(self.shopping_list.total_price(),38)
