import requests
class DataManager:
    
    def __init__(self) -> None:
        self.url_base = "https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices"
        self.headers = {
            
        }
        self.response = requests.get(self.url_base)
        self.response.raise_for_status()
        self.flightsheet= self.response.json()['prices']

    #adds codes to the sheet
    def edit_iata(self, iata, row):
        url  = f'{self.url_base}/{row}'
    
        data = {
            "price":{
                'iataCode':iata
            }
            
        }
        
        self.response = requests.put(url, json=data)
        self.response.raise_for_status()

    #updates price of the sheet    
    def add_price(self, row, price):
        url  = f'{self.url_base}/{row}'
    
        data = {
            "price":{
                'lowestPrice':price
            }
        }
        
        self.response = requests.put(url, json=data)
        self.response.raise_for_status()
        