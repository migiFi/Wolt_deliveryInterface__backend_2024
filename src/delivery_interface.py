import pytz

class DeliveryInterface:
    DISTANCE_THRESHOLD = 1000
    MIN_VALUE_FOR_FREE_DELIVERY = 20000
    EXTRA_DELIVERY_FEE = 100
    BASE_DELIVERY_FEE = 200
    ITEM_SURCHARGE_LIMIT = 4
    OVER_ITEM_LIMIT = 12
    BULK_FEE = 120
    MAX_DELIVERY_FEE = 1500
    FIVE_ITEMS = 5
    
    def __init__(self, cart_value, delivery_distance, number_of_items, delivery_time):
        if cart_value < 1 or delivery_distance < 1 or number_of_items < 1:
            raise ValueError("Invalid input values")
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.delivery_time = delivery_time

    def _calculate_small_order_surcharge(self, cart_value):
        return max(0, 1000 - cart_value)

    def _calculate_distance_fee(self, delivery_distance, distance_threshold=DISTANCE_THRESHOLD):
        delivery_fee = self.BASE_DELIVERY_FEE
        additional_distance = max(0, delivery_distance - distance_threshold)
        # This is used to  calculate additional delivery fee based on additonal distance
        delivery_fee += (additional_distance // 500) * self.EXTRA_DELIVERY_FEE
        # checks if there is a remaining distance
        if additional_distance % 500 > 0:
            delivery_fee += self.EXTRA_DELIVERY_FEE
        return delivery_fee

    def _calculate_surcharge_per_item(self, number_of_items):
        item_surcharge = 0
        if number_of_items >= self.FIVE_ITEMS:
            item_surcharge = (self.number_of_items - self.ITEM_SURCHARGE_LIMIT) * 50
        if number_of_items > self.OVER_ITEM_LIMIT:
            item_surcharge += self.BULK_FEE
        return item_surcharge

    def _calculate_friday_rush_surcharge(self, delivery_fee, delivery_time):
        delivery_time_utc = delivery_time.astimezone(pytz.utc)
        is_friday = delivery_time_utc.weekday() == 4
        is_after_15 = delivery_time_utc.hour >= 15
        is_after_19 = delivery_time_utc.hour < 19 or (delivery_time_utc.hour == 19 and delivery_time_utc.minute == 0)

        rush_surcharge = delivery_fee * 0.2 if is_friday and is_after_15 and is_after_19 else 0
        return rush_surcharge

    # Checks if the value exceeds 200€ for free delivery
    def _apply_free_delivery(self, cart_value, delivery_fee):
        return 0 if cart_value >= self.MIN_VALUE_FOR_FREE_DELIVERY else delivery_fee

    def _calculate_delivery_fee(self):
        # Calculate individual surcharges
        small_order_surcharge = self._calculate_small_order_surcharge(self.cart_value)
        delivery_fee = self._calculate_distance_fee(self.delivery_distance)
        item_surcharge = self._calculate_surcharge_per_item(self.number_of_items)

        # Calculate total delivery before adding the Friday-rush fee
        delivery_fee += small_order_surcharge + item_surcharge

        # Calculate and adds the Friday-rush hour surcharge if applicable
        rush_surcharge = self._calculate_friday_rush_surcharge(delivery_fee, self.delivery_time)
        total_fee = delivery_fee + rush_surcharge

        total_fee = min(total_fee, self.MAX_DELIVERY_FEE)
        total_fee = self._apply_free_delivery(self.cart_value, total_fee)

        return int(total_fee)