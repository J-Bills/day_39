import requests
class DataManager:
    
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices"
        self.response = requests.get(self.url)
        self.response.raise_for_status()
        self.flightdata = self.response.json()['prices']

    #adds codes to the sheet
    def edit_iata(self, iata):
        self.url = "https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices"
        self.response = requests.put(self.url)
        
    #updates price of the sheet    
    def add_price(self, price):
        self.url = "https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices"
        self.response = requests.put(self.url)