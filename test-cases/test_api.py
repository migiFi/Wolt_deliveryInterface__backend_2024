import unittest
from src.delivery_interface import DeliveryInterface

class TestDeliveryInterface(unittest.TestCase):
    def setUp(self):
        self.calculator = DeliveryInterface()

    def test_calculate_small_order_surcharge(self):
        self.assertEqual(self.calculator.calculate_small_order_surcharge(800), 200)
        self.assertEqual(self.calculator.calculate_small_order_surcharge(1200), 0)

    def test_calculate_distance_fee(self):
        self.assertEqual(self.calculator.calculate_distance_fee(800), 200)
        self.assertEqual(self.calculator.calculate_distance_fee(1500), 300)
        self.assertEqual(self.calculator.calculate_distance_fee(2500), 500)

if __name__ == '__main__':
    unittest.main()
