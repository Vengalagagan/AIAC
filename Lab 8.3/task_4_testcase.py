import unittest
from task_4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_add_single_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.5)
    def test_add_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertIn("apple", self.cart.items)
        self.assertIn("banana", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.5)
        self.assertEqual(self.cart.items["banana"], 2.0)
    def test_add_same_item_accumulates_price(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.assertEqual(self.cart.items["apple"], 3.5)
    def test_remove_existing_item(self):
        self.cart.add_item("milk", 2.5)
        self.cart.remove_item("milk")
        self.assertNotIn("milk", self.cart.items)
    def test_remove_nonexistent_item_raises(self):
        with self.assertRaises(KeyError):
            self.cart.remove_item("bread")
    def test_total_cost_empty_cart(self):
        self.assertAlmostEqual(self.cart.total_cost(), 0.0)
    def test_total_cost_with_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertAlmostEqual(self.cart.total_cost(), 3.5)
    def test_total_cost_with_accumulated_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.5)
        self.cart.add_item("banana", 2.0)
        self.assertAlmostEqual(self.cart.total_cost(), 6.0)
    def test_add_item_invalid_name(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("", 1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item(123, 1.0)
    def test_add_item_invalid_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("apple", -1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item("apple", "free")
if __name__ == "__main__":
    unittest.main()