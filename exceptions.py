class CityNotFoundError(Exception) :
    def __init__(self,city_name):
        self.message = f"The city {city_name} Not Found"
        super().__init__(self.message)