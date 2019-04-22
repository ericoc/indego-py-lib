#!/usr/bin/env python3

import requests
import re


"""
Create a class to work with the Philadelphia Indego Bike Share API
"""
class Indego():


    """Create an init function to run on instantiation of the class"""
    def __init__(self):

        # Create an empty dictionary to fill in with station data
        self.stations = {}

        # Initialization (retrieval) of station data has not happened yet
        self.initialized = False


    """Create a function to hit the API and find all of the stations"""
    def __find_stations(self):

        # Specify the Indego bikes API URL, a friendly user-agent, and custom headers to hit it with
        url = 'https://www.rideindego.com/stations/json/'
        user_agent = 'Indego Python3 API Library - https://github.com/ericoc/indego-py-lib'
        headers = {'Accept': 'application/json', 'User-Agent': user_agent}

        # Hit the API and decode the JSON response
        data = requests.get(url, headers=headers)
        json = data.json()

        # Add each station to our own dictionary that is easier to work with
        for station in json['features']:
            self.stations[station['properties']['kioskId']] = station['properties']

        # Initialization is complete since stations have been found at this point
        self.initialized = True


    """Create a function to search for and return stations"""
    def get_stations(self, where):

        # Find all of the stations first, if that has not already been done
        if not self.initialized:
            self.__find_stations()

        # Create empty dictionary to fill in with station data that will be returned by this function
        out = {}

        # Just provide all of the stations if no search query was given
        if not where:
            out = self.stations

        # If a search query was passed, process it...
        else:

            # Loop through each station in the primary dictionary
            where = str(where)
            for station in self.stations:

                # If the search query is numeric, it could either be a zip code or a kiosk ID
                if where.isdigit():

                    # Kiosk IDs are four digits (so far... new stations could break this eventually)
                    # A kiosk ID match only returns that single station immediately
                    # The kioskID from the API is an integer so it has to be compared that way
                    if len(where) == 4:
                        if self.stations[station]['kioskId'] == int(where):
                            out = {}
                            out[station] = self.stations[station]
                            return out

                    # Zip codes are five digits
                    elif len(where) == 5:
                        if self.stations[station]['addressZipCode'] == where:
                            out[station] = self.stations[station]

                # Do a regular expression match against the name and address of each station
                if (re.search(where, self.stations[station]['addressStreet'], re.IGNORECASE)) or (re.search(where, self.stations[station]['name'], re.IGNORECASE)):
                    out[station] = self.stations[station]

        # Return the stations!
        return out
