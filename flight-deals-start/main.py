#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# today = datetime.now().date()
# startdate = today+timedelta(days=1)
# enddate = startdate +timedelta(weeks=24)

# startdate = startdate.strftime("%Y-%m-%d")
# enddate = enddate.strftime("%Y-%m-%d")

# sheet = DataManager()
# for flight in sheet.flightsheet:
#     flightsearch = FlightSearch(home="san diego", city=flight['city'])
#     flightsearch.destID = "REP"
#     sheet.edit_iata(flightsearch.destID, flight['id'])
#     # flightdata = FlightData(flightsearch.destID, flightsearch.origID, startdate, enddate)
    
    
    # if flight[0].get('lowestPrice') > flightdata.

# flightsearch = FlightSearch('something', 'something')
# flight1 = FlightSearch('something', 'something')
# flight2 = FlightSearch('something', 'something')

price_list = {
    0:{'2012-02-02':2},
    1:{'2012-02-02':4},
    2:{'2012-02-02':8}    
}

def find_min_price():    
    min_values = []
    for inner_dict in price_list.values():
        min_values.extend(inner_dict.values())
    min_value = min(min_values)
    return min_value
        
def get_key_by_value(cheapest):
        for key, value in price_list.items():
            for inner_key, inner_value in value.items():
                if inner_value == cheapest:
                    return key
            
lowest_price = find_min_price()
key = get_key_by_value(lowest_price)

print(key)

