# Wolt Software Engineer Internships 2024 - Backend 

A delivery fee calculator for the Wolt intership assigment(https://github.com/woltapp/engineering-internship-2024) using Python (v.312), it calculates the deliver fee based on the cart value, delivery distance, number of items and the time of the order.

API implementation is done using [flask](https://flask.palletsprojects.com/en/3.0.x/) framework.

For testing the [unittest](https://docs.python.org/3/library/unittest.html) framework was used.

# How to:

Create a virtual enviroment (recommended), as it avoids installing Python packages globally that could break system tools and other projects:
```
$ python -m venv .venv
$ source .venv/bin/activate
```
After creation, choose the Python interpreter, min. 3.10 (I used 3.12) in the command palette.

Dependencies are located in the `requirements.txt` file.

To install dependencies run:
```
$ pip install -r dependencies.txt
```
# Testing

Terminal 1: to start the app(request) 
```
$ python api.py
```
Terminal 2: to send a request
```
$ curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://127.0.0.1:5000/calculate_delivery_fee
```

The request payload was tested with the example values provided in the assigment repo, resulting in the response payload:
```
{
  "delivery_fee": 710
}
```
For testing the Friday rush surcharge (if applicable) the date and time values were adjusted  accordingly, for example:
```
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-19T17:00:00Z"}
```
Resulting in:
```
{
  "delivery_fee": 852
}
```

