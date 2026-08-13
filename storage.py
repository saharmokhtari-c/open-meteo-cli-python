
from datetime import datetime 
class Storage():
    def __init__(self,risults_meteo):
         self.risults_meteo = risults_meteo
    def WriteToFile(self):
        timestamp_attuale = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        with open("history.txt" ,"a", encoding = "utf-8") as file:
            for city,data in self.risults_meteo.items():
                temp = data.get("temperature",0)
                w_code = data.get("weathercode",0)
                line = f"[{timestamp_attuale}] {city} | {temp} degree | {w_code} WMO code\n "
                file.write(line)
        print("The Weathers data saved in history.txt")