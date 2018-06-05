#!/usr/bin/env python3

from indego import Indego

# Instantiate the Indego class
indego = Indego();

# Just get "university" stations
uni_stations = indego.get_stations('university');

print(uni_stations);
