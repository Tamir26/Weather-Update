from weather_sampler import get_coordinates, get_current_weather
from rabbitmq_client import send_to_rabbitmq
coordinates=get_coordinates()
lat = coordinates[0]
lon = coordinates[1]
weather_data, timestamp = get_current_weather(lat, lon)

payload = {
    'temp': weather_data['main']['temp'],
    'humidity': weather_data['main']['humidity'],
    'wind_speed': weather_data['wind']['speed'],
    'timestamp': timestamp,
    'city': weather_data['name']
}

send_to_rabbitmq(data=payload, queue_name='weather_queue')
print("Weather data sent to RabbitMQ!")
