import re
import requests


"""
Create a class to work with the Philadelphia Indego Bike Share API
"""
class Indego(object):


    """Trigger function to find all Indego stations upon instantiation of the class"""
    def __init__(self):
        self.__find_stations()


    """Define a function to hit the API and find all of the Indego stations from the API"""
    def __find_stations(self):

        # Specify the Indego API URL, a friendly user-agent, and custom headers to use in the HTTP request
        url = 'https://www.rideindego.com/stations/json/'
        user_agent = 'Indego Python3 API Library - https://github.com/ericoc/indego-py-lib'
        headers = {'Accept': 'application/json', 'User-Agent': user_agent}

        # Perform HTTP request to the API and decode the JSON response, assuming there was a valid HTTP response code
        data = requests.get(url, headers=headers)
        data.raise_for_status()
        json = data.json()

        # Add each station to our own dictionary that is easier to work with
        self.stations = {}
        for station in json['features']:
            self.stations[station['properties']['kioskId']] = station['properties']


    """Define a function to search for and return stations from our larger dictionary which contains all stations from the Indego API"""
    def get_stations(self, where=None):

        # Find all of the stations first, if that has not already been done
        if not self.stations:
            self.__find_stations()

        # Simply provide all of the stations if no search query was given
        if not where or where == '':
            return self.stations

        # Otherwise, a search query was provided so create an empty dictionary to fill with station data, which will be returned by this function
        where = str(where)
        out = {}

        # Loop through eery station that was found by the API
        for station_id, station in self.stations.items():

            # If the search query is numeric, it could either be a zip code or a kiosk ID
            if where.isdigit():

                # Kiosk IDs are four digits (so far... new stations could break this eventually)
                # A kiosk ID match only returns that single station immediately
                if len(where) == 4 and station_id == int(where):
                    return { station_id : station }

                # Zip codes are five digits
                if len(where) == 5 and station['addressZipCode'] == where:
                    out[station_id] = station

            # Do a regular expression match against the name and address of each station
            if (re.search(where, station['addressStreet'], re.IGNORECASE)) or (re.search(where, station['name'], re.IGNORECASE)):
                out[station_id] = station

        # Return the limited set of stations that were found by the search query
        return out
