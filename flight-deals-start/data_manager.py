import requests
class DataManager:
    
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices"
        self.headers = {
            
        }
        self.response = requests.get(self.url)
        self.response.raise_for_status()
        self.flightsheet= self.response.json()['prices']

    #adds codes to the sheet
    def edit_iata(self, iata, city):
        self.url = f"https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices?filter[city]={city}"
    
        self.something = {
            "row":{
                'iataName':iata
            }
            
        }
        self.response.raise_for_status()
        self.response = requests.put(self.url, json=self.something)
        
    #updates price of the sheet    
    def add_price(self, iata, price):
        self.url = f"https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices?filter[city]={iata}"
        
        self.something = {
            "row":{
                'lowestPrice':price
            }
            
        }
        
        self.response.raise_for_status()
        self.response = requests.put(self.url, json=self.something)
        