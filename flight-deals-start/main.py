#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

sheet = DataManager()
sheet.edit_iata()
for flight in sheet.flightdata:
    flightsearch = FlightSearch()
    if flight[0].get('lowestPrice') > flightsearch.

# flightsearch = FlightSearch('something', 'something')
# flight1 = FlightSearch('something', 'something')
# flight2 = FlightSearch('something', 'something')

