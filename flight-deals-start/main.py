#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

today = datetime.now().date()
startdate = today+timedelta(days=1)
enddate = startdate +timedelta(weeks=24)

startdate = startdate.strftime("%Y-%m-%d")
enddate = enddate.strftime("%Y-%m-%d")

sheet = DataManager()
for flight in sheet.flightsheet:
    flightsearch = FlightSearch(home="san diego", city=flight['city'])
    flightsearch.destID = "REP"
    sheet.edit_iata(flightsearch.destID, flight['city'])
    # flightdata = FlightData(flightsearch.destID, flightsearch.origID, startdate, enddate)
    
    
    # if flight[0].get('lowestPrice') > flightdata.

# flightsearch = FlightSearch('something', 'something')
# flight1 = FlightSearch('something', 'something')
# flight2 = FlightSearch('something', 'something')

