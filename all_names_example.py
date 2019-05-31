from indego import Indego

# Instantiate the Indego class
indego = Indego()

# Just get all stations
all_stations = indego.get_stations()

# This will print each of the stations names
for station in all_stations.values():
    print(station['name'])
