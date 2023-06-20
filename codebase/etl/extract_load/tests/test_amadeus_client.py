import os
from src.amadeus_client import AmadeusClient
from datetime import datetime, timedelta

def test_get_access_token():
    client = AmadeusClient()
    assert type(client.get_access_token()) == str

def test_search_flights_returns_flights_from_two_weeks_from_now():
    client = AmadeusClient()
    two_weeks = datetime.today() + timedelta(days = 14)
    origin = 'NYC'
    destination = 'CHI'
    departure_date_str = two_weeks.strftime('%Y-%m-%d')
    flight_data = client.search_flights(origin, destination, departure_date_str)
    flight_itinerary = flight_data['data'][0]
    departure_str = flight_itinerary['itineraries'][0]['segments'][0]['departure']['at']
    
    response_datetime_str = datetime.strptime(departure_str, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
    assert response_datetime_str == departure_date_str
