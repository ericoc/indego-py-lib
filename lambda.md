AWS Lambda function
--------------------

The included [`lambda_function.py` script](lambda_function.py) is my first attempt at ever creating an AWS "Lambda function" along with an AWS "API Gateway". It simply returns JSON of the bike-share stations using the `Indego` class that I've written, allowing for searching the stations. For example, see the following requests:

    https://indego.ericoc.com/api/?search=fairmount
    https://indego.ericoc.com/api/?search=municipal
    https://indego.ericoc.com/api/?search=3009      # Single kioskID
    https://indego.ericoc.com/api/?search=19132     # Zip code
    https://indego.ericoc.com/api/                  # All stations
