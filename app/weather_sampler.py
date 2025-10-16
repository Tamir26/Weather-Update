import requests
from datetime import datetime 
from config import CHOSEN_CITY,WEATHER_UPDATE_KEY,URL_GET_COORDINATES


def get_coordinates():
    coordinatesResponse = requests.get(URL_GET_COORDINATES)

    if coordinatesResponse.status_code != 200:
        print(f"Error ! there is a problem with the coordinates Requests: {coordinatesResponse.status_code}")
    else:
        coordinatesData=coordinatesResponse.json()
        cityLat = coordinatesData[0]['lat']
        cityLon = coordinatesData[0]['lon']
        return [cityLat,cityLon]


def get_current_weather(cityLat,cityLon):
    currentWeatherResponse = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={cityLat}&lon={cityLon}&appid={WEATHER_UPDATE_KEY}&units=metric")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    if currentWeatherResponse.status_code != 200:
        print(f"Error ! there is a problem with  the  weather Requests: {currentWeatherResponse.status_code}")
    else:
        print(currentWeatherResponse)
        currentWeatherData = currentWeatherResponse.json()
        print(f"{currentWeatherData}\n")
        print(f"{timestamp}")
        return currentWeatherData, timestamp