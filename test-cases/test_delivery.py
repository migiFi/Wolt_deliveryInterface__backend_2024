# test_delivery_interface.py

import unittest
from datetime import datetime
import pytz
from src.delivery_interface import DeliveryInterface

class TestDeliveryInterface(unittest.TestCase):
    def test_calculate_small_order_surcharge(self):
        cart_value = 1100
        expected_surcharge = 0
        self.assertEqual(DeliveryInterface.calculate_small_order_surcharge(cart_value), expected_surcharge)

    def test_calculate_distance_fee(self):
        delivery_distance = 1200
        expected_fee = 200 + 100  
        self.assertEqual(DeliveryInterface.calculate_distance_fee(delivery_distance), expected_fee)

    def test_calculate_item_surcharge(self):
        self.assertEqual(DeliveryInterface.calculate_item_surcharge(3), 0)

        self.assertEqual(DeliveryInterface.calculate_item_surcharge(5), 50)

        self.assertEqual(DeliveryInterface.calculate_item_surcharge(7), 150)

        self.assertEqual(DeliveryInterface.calculate_item_surcharge(15), 670)

    def test_calculate_rush_surcharge(self):
        delivery_time = datetime(2024, 1, 19, 17, 30)

        rush_surcharge = DeliveryInterface.calculate_rush_surcharge(200, delivery_time)
        self.assertEqual(rush_surcharge, 40)

        delivery_time = datetime(2024, 1, 20, 14, 30)
        rush_surcharge = DeliveryInterface.calculate_rush_surcharge(200, delivery_time)
        self.assertEqual(rush_surcharge, 0)

    def test_apply_free_delivery(self):
        self.assertEqual(DeliveryInterface.apply_free_delivery(10000, 500), 500)

        self.assertEqual(DeliveryInterface.apply_free_delivery(25000, 500), 0)

if __name__ == '__main__':
    unittest.main()
