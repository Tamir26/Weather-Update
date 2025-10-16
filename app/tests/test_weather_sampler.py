import pytest
from app.weather_sampler import get_coordinates, get_current_weather

def test_get_coordinates(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return [{'lat': 51.5074, 'lon': -0.1278}]
    
    monkeypatch.setattr("weather_sampler.requests.get", lambda url: MockResponse())
    
    coords = get_coordinates()
    assert coords == [51.5074, -0.1278]

def test_get_current_weather(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "main": {"temp": 15.5, "humidity": 70},
                "wind": {"speed": 3.2},
                "name": "London"
            }

    monkeypatch.setattr("weather_sampler.requests.get", lambda url: MockResponse())
    
    data, timestamp = get_current_weather(51.5074, -0.1278)
    assert data["main"]["temp"] == 15.5
    assert data["wind"]["speed"] == 3.2
    assert data["name"] == "London"
