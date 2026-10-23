import requests
from exceptions import CityNotFoundError
class ApiClient:
    def __init__(self):
        pass
        

    def get_geocode(self,city_name):
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response1 = requests.get(geocoding_url)
        if response1.status_code == 200 :
          data = response1.json()
         
          if "results" in data and len(data["results"]) > 0:
                first_result = data["results"][0]
                return first_result["latitude"],first_result["longitude"]  
          else:
             raise CityNotFoundError(city_name)        
    
    def get_api(self,city_name) :
        x , y = self.get_geocode(city_name)
        api_url = f"https://api.open-meteo.com/v1/forecast?latitude={x}&longitude={y}&current_weather=true"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data["current_weather"]
      
      

    
       
        
