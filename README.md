Indego Bike Share Python Library
================================


About
-----

I have tried to make a re-usable Python library for the Philadelphia Indego Bike Share API!

I wrote this similarly to [my existing Indego PHP library](https://github.com/ericoc/indego-php-lib).

Check out [the City of Philadelphia GitHub](https://github.com/CityOfPhiladelphia) if you think this library is interesting!

I created [indego.ericoc.com](https://indego.ericoc.com/) ([source code](https://github.com/ericoc/indego.ericoc.com)) using this library as well

Installation
------------

Installation of this library should be as simple as running:

    pip install indego


Compatibility
-------------

Please note that this library is only compatible with Python 3+. Python 2 is not supported.


Example
-------

When combined with the provided `Indego` class, the following code will generate the example output:

    from indego import Indego

    # Instantiate the Indego class
    indego = Indego()

    # Retrieve and print "university" stations
    uni_stations = indego.get_stations('university')
    print(uni_stations)

    # Show how many stations were returned above
    uni_count = len(uni_stations)
    print(uni_count, 'stations returned')

Output:

    $ python3 university_example.py
    {3008: {'id': 3008, 'name': 'Temple University Station', 'coordinates': [-75.15067, 39.98081], 'totalDocks': 17, 'docksAvailable': 11, 'bikesAvailable': 5, 'classicBikesAvailable': 3, 'smartBikesAvailable': 0, 'electricBikesAvailable': 2, 'rewardBikesAvailable': 5, 'rewardDocksAvailable': 12, 'kioskStatus': 'FullService', 'kioskPublicStatus': 'Active', 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'addressStreet': '1076 Berks Street', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19122', 'bikes': [{'dockNumber': 2, 'isElectric': False, 'isAvailable': True, 'battery': None}, {'dockNumber': 4, 'isElectric': False, 'isAvailable': True, 'battery': None}, {'dockNumber': 7, 'isElectric': False, 'isAvailable': True, 'battery': None}, {'dockNumber': 10, 'isElectric': True, 'isAvailable': True, 'battery': 42}, {'dockNumber': 12, 'isElectric': True, 'isAvailable': True, 'battery': 29}, {'dockNumber': 16, 'isElectric': False, 'isAvailable': False, 'battery': None}], 'closeTime': None, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'kioskId': 3008, 'notes': None, 'openTime': None, 'publicText': '', 'timeZone': None, 'trikesAvailable': 0, 'latitude': 39.98081, 'longitude': -75.15067}, 3020: {'id': 3020, 'name': 'University City Station', 'coordinates': [-75.19007, 39.94855], 'totalDocks': 36, 'docksAvailable': 35, 'bikesAvailable': 0, 'classicBikesAvailable': 0, 'smartBikesAvailable': 0, 'electricBikesAvailable': 0, 'rewardBikesAvailable': 0, 'rewardDocksAvailable': 36, 'kioskStatus': 'FullService', 'kioskPublicStatus': 'Active', 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'addressStreet': '3051 South St.', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19147', 'bikes': [{'dockNumber': 23, 'isElectric': False, 'isAvailable': False, 'battery': None}], 'closeTime': None, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'kioskId': 3020, 'notes': None, 'openTime': None, 'publicText': '', 'timeZone': None, 'trikesAvailable': 0, 'latitude': 39.94855, 'longitude': -75.19007}}
    2 stations returned


Providing an argument/filter to `get_stations()` to limit the selection of stations only limits the results within the `Indego` class. The API end-point itself always returns all stations.

Unfortunately, there does not appear to be a signifcant amount of documentation for the API being used nor does there seem to be any parameters available to limit the stations being retrieved from the API.

Calling `get_stations()` without any arguments will return a list of all (*currently*, 132) stations.


More Information
----------------
* [The actual Philadelphia Indego Bike Share API, a GeoJSON file](https://www.rideindego.com/stations/json/)
* [OpenDataPhilly description of the API](https://opendataphilly.org/datasets/indego-bike-share-stations/)
* [Interesting article visualizing Indego usage](http://www.randalolson.com/2015/09/05/visualizing-indego-bike-share-usage-patterns-in-philadelphia-part-2/)
