import pytest
from app.rabbitmq_client import send_to_rabbitmq

def test_send_to_rabbitmq(monkeypatch):
    called = {}
    class MockChannel:
        def queue_declare(self, queue, durable):
            called['queue'] = queue
        def basic_publish(self, exchange, routing_key, body, properties):
            called['body'] = body
    class MockConnection:
        def channel(self):
            return MockChannel()
        def close(self):
            called['closed'] = True

    monkeypatch.setattr("rabbitmq_client.pika.BlockingConnection", lambda params: MockConnection())

    send_to_rabbitmq({"temp": 10}, queue_name="test_queue")
    assert called['queue'] == "test_queue"
    assert '"temp": 10' in called['body']
    assert called['closed'] is True
