import requests
class FlightData:
    
    def __init__(self, destID:str, origID:str, startdate, enddate) -> list:
        #This class is responsible for talking to the Flight Search API.
        self.url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getPriceCalendar"
        self.destID = destID
        self.origID = origID
        self.querystring = {"originSkyId":origID, "destinationSkyId":destID, "fromDate":startdate, 'toDate':enddate}
        

        self.headers = {
	        "X-RapidAPI-Key": "f4cc4e8583mshc827b1dea0c7bf1p117c4ajsn2f9dab7ef1bf",
	        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
        }

        self.response = requests.get(self.url, headers=self.headers,params=self.querystring)
        self.data = self.response.json()
        self.price_list = self.data['data']['flights']
        
    def find_min_price(self):
        flightprices = [price for (day,price) in self.price_list]
        cheapest = min(flightprices)
        return cheapest
    
    def get_key_by_value(self, cheapest):
        for key, value in self.price_list.items():
            if value == cheapest:
                return key
        # If the search value is not found, return None or raise an exception
        return None 
        
        # return self.price_list
        
        
        
    #This class is responsible for structuring the flight data.