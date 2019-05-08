Indego Bike Share Python Library
==============================

About
-----

I have tried to make a re-usable Python library for the Philadelphia Indego Bike Share API! I'm not very familiar with Python, but tried to learn by creating this.

I wrote this similarly to [my existing Indego PHP library](https://github.com/ericoc/indego-php-lib).

Check out [the City of Philadelphia GitHub](https://github.com/CityOfPhiladelphia) if you think this library is interesting!


Example
-------

When combined with the provided `Indego` class, the following code will generate the example output in the next section:

    from indego import Indego

    # Instantiate the Indego class
    indego = Indego()

    # Just get "university" stations
    uni_stations = indego.get_stations('university')

    print(uni_stations)


Providing a argument/filter to `get_stations()` to return a list of stations only limits the results within the `Indego` class.

Unfortunately, there does not appear to be a signifcant amount of documentation for the API being used nor does there seem to be any parameters available to limit the stations being retrieved from the API.

Calling `get_stations()` without any arguments will return a list of all (*currently*, 132) stations:

    $ python3 example.py
    {3008: {'addressStreet': '1076 Berks Street', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19122', 'bikesAvailable': 5, 'closeTime': '03:55:00', 'docksAvailable': 14, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'isVisible': False, 'kioskId': 3008, 'kioskPublicStatus': 'Active', 'kioskStatus': 'FullService', 'name': 'Temple University Station', 'notes': None, 'openTime': '04:00:00', 'publicText': '', 'timeZone': 'Eastern Standard Time', 'totalDocks': 19, 'trikesAvailable': 0, 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'latitude': 39.98078, 'longitude': -75.15055, 'hasGeofence': False, 'classicBikesAvailable': 5, 'smartBikesAvailable': 0, 'electricBikesAvailable': 0, 'isArchived': False}, 3020: {'addressStreet': '3051 South St.', 'addressCity': 'Philadelphia', 'addressState': 'PA', 'addressZipCode': '19147', 'bikesAvailable': 6, 'closeTime': '03:55:00', 'docksAvailable': 29, 'eventEnd': None, 'eventStart': None, 'isEventBased': False, 'isVirtual': False, 'isVisible': False, 'kioskId': 3020, 'kioskPublicStatus': 'Active', 'kioskStatus': 'FullService', 'name': 'University City Station', 'notes': None, 'openTime': '04:00:00', 'publicText': '', 'timeZone': 'Eastern Standard Time', 'totalDocks': 35, 'trikesAvailable': 0, 'kioskConnectionStatus': 'Active', 'kioskType': 1, 'latitude': 39.94922, 'longitude': -75.19036, 'hasGeofence': False, 'classicBikesAvailable': 6, 'smartBikesAvailable': 0, 'electricBikesAvailable': 0, 'isArchived': False}}


More Information
----------------
* [The actual Philadelphia Indego Bike Share API, a GeoJSON file](https://www.rideindego.com/stations/json/)
* [OpenDataPhilly description of the API](https://www.opendataphilly.org/dataset/bike-share-stations)
* [Interesting article visualizing Indego usage](http://www.randalolson.com/2015/09/05/visualizing-indego-bike-share-usage-patterns-in-philadelphia-part-2/)
