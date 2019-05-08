from indego import Indego

# Instantiate the Indego class
indego = Indego()

# Retrieve and print "university" stations
uni_stations = indego.get_stations('university')
print(uni_stations)

# Show how many stations were returned above
uni_count = len(uni_stations)
print(uni_count, 'stations returned')
