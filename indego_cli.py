#!/usr/bin/env python3

from indego import Indego
import sys

# Instantiate the Indego class
indego = Indego()

# Get the stations that were requested if doing a search with a CLI argument
if len(sys.argv) > 1:
    search = sys.argv[1]

# Otherwise, get all stations
else:
    search = None

# Get stations
stations = indego.get_stations(search)

# Return red error message to standard error (stderr) if no stations were found and exit with non-zero
if not stations:
    sys.stderr.write("\x1b[31mNo stations found!\x1b[0m\n")
    exit(1)

# Loop through each bike-share station
for station_id, station in stations.items():

    # List the current stations ID and name, padded with spaces so everything lines up
    print (str(station_id).ljust(8) + ' ' + station['name'].ljust(60), end='')

    # Build a graph for bikes at the current station
    graph = ''
    for bike in range(station['bikesAvailable']):
        graph += '#'

    # And continue building the graph for empty docks at the current station
    for dock in range(station['docksAvailable']):
        graph += '='

    # Pad the graph with spaces to line stuff up and color code the bikes (#) vs. docks (=) graphs that we just built
    graph = graph.ljust(60)
    graph = graph.replace('#', '\x1b[32m#\x1b[0m')    # Bikes are green
    graph = graph.replace('=', '\x1b[31m=\x1b[0m')    # Docks are red
    print(graph, end='')

    # Pad the bikes and docks numbers with spaces to line stuff up
    bike_info = str(station['bikesAvailable']) + ' bikes'
    dock_info = str(station['docksAvailable']) + ' docks'
    print(bike_info.ljust(12), end='')
    print(dock_info.ljust(12))
