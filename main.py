import argparse
from exceptions import CityNotFoundError
from api_client import ApiClient
from storage import Storage
def start_cli():
    parser = argparse.ArgumentParser(description="Open-Meteo CLI Weather Tool")
    parser.add_argument("cities", nargs="+", help="Name Of Cities")
    args = parser.parse_args()
    client = ApiClient()
    results_meteo = {}
    max_1 = -100
    min_1 = 100
    max_city =" "
    min_city =" "
    count = False
    
    for city in args.cities :
        try:
            dati = client.get_api(city)
            results_meteo[city] = dati
            #print(dati) => {'time': '2026-07-07T08:30', 'interval': 900, 'temperature': 27.5, 'windspeed': 5.5,
            #'winddirection': 32, 'is_day': 1, 'weathercode': 0}            
            #print(results_meteo) => {'turin': {'time': '2026-07-07T08:30', 'interval': 900, 'temperature': 27.5,
            #'windspeed': 5.5, 'winddirection': 32, 'is_day': 1, 'weathercode': 0}}
            current_temp = dati.get("temperature",0)
            current_weathercode = dati.get("weathercode",0)
           
            if  current_temp > max_1 :
                    max_1 = current_temp
                    max_city = city
            if  current_temp < min_1 :
                    min_1 = current_temp
                    min_city = city
          
            if  current_temp > 30 or current_weathercode > 50 :
                count = True

        except CityNotFoundError as e:
            print(f"Error:{e}")

    print (f"The Hottest City is {max_city} {max_1} degrees\nThe Coldest City is {min_city} {min_1} degrees" )

    if  count :
            print("SEVERE WEATHER WARNING")

    history = Storage(results_meteo)
    history.WriteToFile()

if __name__ == "__main__" :
 start_cli() 




