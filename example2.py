#!/usr/bin/env python3

from indego import Indego

# Instantiate the Indego class
indego = Indego()

# Just get all stations
stations = indego.get_stations()

# This will print each of the stations names
for station in stations.values():
    print(station['name'])
