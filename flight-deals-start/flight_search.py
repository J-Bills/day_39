import requests


"""Take the city data that gets return from google sheets and return the IATA codes.
    """
    
home_set = False
class FlightSearch:
    
    def __init__(self, home:str, city:str) -> None:
        #This class is responsible for talking to the Flight Search API.
        self.url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"
        self.origID = ''
        self.destID = ''
        self.querystring= {"q":city}
        

        self.headers = {
	        "X-RapidAPI-Key": "f4cc4e8583mshc827b1dea0c7bf1p117c4ajsn2f9dab7ef1bf",
	        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
        }
        
        global home_set

        if not home_set:
            self.response = requests.get(self.url, headers=self.headers,params=self.querystring_home)
            self.data = self.response.json()
            self.origID = self.data['data'][0]['navigation']['relevantFlightParams']
            home_set = True
        
        self.response = requests.get(self.url, headers=self.headers,params=self.querystring_home)
        self.data = self.response.json()
        self.destID = self.data['data'][0]['navigation']['relevantFlightParams']