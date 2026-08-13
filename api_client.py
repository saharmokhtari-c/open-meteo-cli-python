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
          #print(data) => {'results': [{'id': 3165524, 'name': 'Turin', 'latitude': 45.07049, 'longitude': 7.68682, 'elevation': 239.0,
          #'feature_code': 'PPLA', 'country_code': 'IT', 'admin1_id': 3170831, 'admin2_id': 3165523, 'admin3_id': 3165525,
          #'admin4_id': 11352097, 'timezone': 'Europe/Rome', 'population': 847287, 'postcodes': ['10121'], 'country_id': 3175395, 'country': 'Italy', 'admin1': 'Piedmont', 'admin2': 'Province of Turin', 'admin3': 'Torino', 'admin4': 'Centro - Crocetta'}], 'generationtime_ms': 0.4916191}
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
        # {...,'current_weather': {'time': '2026-07-15T09:30', 'interval': 900, 'temperature': 29.9, 'windspeed': 4.8,
        #  'winddirection': 207, 'is_day': 1, 'weathercode': 2}}
      

    
       
        