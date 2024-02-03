from flask import Flask, request, jsonify
import datetime
import pytz

from delivery_interface import DeliveryInterface

app = Flask(__name__)

@app.route('/calculate_delivery_fee', methods=['POST'])
def calculate_delivery_fee_endpoint():
    try:
        data = request.get_json()

        cart_value = data['cart_value']
        delivery_distance = data['delivery_distance']
        number_of_items = data['number_of_items'] 
        delivery_time = data['time']

        delivery_time = datetime.datetime.strptime(delivery_time, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)

        calculator = DeliveryInterface(cart_value, delivery_distance, number_of_items, delivery_time)

        delivery_fee = calculator._calculate_delivery_fee()

        return jsonify({
            'delivery_fee': delivery_fee
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
