Indego Bike Share Python Library
==============================

About
-----

I've tried to make a re-usable Python library for the Philadelphia Indego Bike Share API! I'm not very familiar with Python, but tried to learn by creating this.

I wrote this similarly to [my existing Indego PHP library](https://github.com/ericoc/indego-php-lib).

Check out [the City of Philadelphia GitHub](https://github.com/CityOfPhiladelphia) if you think this library is interesting!


Example
-------

### Code

When combined with the provided `Indego` class, the following code will generate the example output in the next section:

	from indego import Indego

	# Instantiate the Indego class
	indego = Indego();

	# Just get "university" stations
	uni_stations = indego.get_stations('university');

	print(uni_stations);


Providing a argument/filter to `get_stations()` to return a list of stations only limits the results within the `Indego` class.

Unfortunately, there does not appear to be a signifcant amount of documentation for the API being used nor does there seem to be any parameters available to limit the stations being retrieved from the API.

Calling `get_stations()` without any arguments will return a list of all (*currently*, 123) stations!

### Output

	$ python3 example.py
	{3008: {'addressStreet': '1076 Berks Street', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19122', 'bikesAvailable': 1, 'closeTime': '23:58:00', 'docksAvailable': 18, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'isVisible': False, 'kioskId': 3008, 'kioskPublicStatus': 'Active', 'kioskStatus': 'Full Service', 'name': 'Temple University Station', 'notes': None, 'openTime': '00:02:00', 'publicText': '', 'timeZone': 'Eastern Standard Time', 'totalDocks': 19, 'trikesAvailable': 0, 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'latitude': 39.98078, 'longitude': -75.15055, 'hasGeofence': False, 'classicBikesAvailable': 1, 'smartBikesAvailable': 0}, 3020: {'addressStreet': '3051 South St.', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19147', 'bikesAvailable': 0, 'closeTime': '23:58:00', 'docksAvailable': 35, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'isVisible': False, 'kioskId': 3020, 'kioskPublicStatus': 'Active', 'kioskStatus': 'Full Service', 'name': 'University City Station', 'notes': None, 'openTime': '00:02:00', 'publicText': '', 'timeZone': 'Eastern Standard Time', 'totalDocks': 35, 'trikesAvailable': 0, 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'latitude': 39.94922, 'longitude': -75.19036, 'hasGeofence': False, 'classicBikesAvailable': 0, 'smartBikesAvailable': 0}}


Command-line script
--------------------

TODO


More Information
----------------
* [The actual API, a GeoJSON file](https://www.rideindego.com/stations/json/)
* [OpenDataPhilly description of the API](https://www.opendataphilly.org/dataset/bike-share-stations)
* [Interesting article visualizing Indego usage](http://www.randalolson.com/2015/09/05/visualizing-indego-bike-share-usage-patterns-in-philadelphia-part-2/)
