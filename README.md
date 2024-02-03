Wolt Software Engineer Intern 2024 - Backend 

API implementation is done using 'flask' framework.

For testing the 'unittest' framework was used.

Bellow you can information on how to execute:

Create a virtual enviroment (recommended), as it avoids installing Python packages globally
that could break system tools and other projects:

python -m venv .venv
source .venv/bin/activate

After creation, choose the Python interpreter, min. 3.10 (I used 3.12) in the command palette.

Dependencies are located in the requirements.txt file.

To install dependencies run -->> pip install -r dependencies.txt

Terminal 1 - run the code -->> python api.py

Terminal 2 - send a request -->> curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://127.0.0.1:5000/calculate_delivery_fee

The request payload was tested with the example values provided in the assigment
repo, resulting in the response payload:

{
  "delivery_fee": 710
}

For testing the Friday rush surcharge (if applicable) the date and time values were adjusted  accordingly, for example:

{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-19T17:00:00Z"}

Resulting in:

{
  "delivery_fee": 852
}


