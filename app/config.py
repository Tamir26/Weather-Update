from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_UPDATE_KEY = os.getenv("WEATHER_UPDATE_KEY")
CHOSEN_CITY = os.getenv("CHOSEN_CITY")
URL_GET_COORDINATES = f"http://api.openweathermap.org/geo/1.0/direct?q={CHOSEN_CITY}&limit=1&appid={WEATHER_UPDATE_KEY}"
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS")