import pika
import json
from config import RABBITMQ_PASS, RABBITMQ_USER


def send_to_rabbitmq(data, queue_name='weather_queue'):
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(data),
        properties=pika.BasicProperties(delivery_mode=2)  # persistent
    )
    connection.close()

