import os
from etl.amadeus_client import AmadeusClient
from datetime import datetime, timedelta

def test_get_access_token():
    client = AmadeusClient()
    assert type(client.get_access_token()) == str

def test_search_flights_returns_flights_from_two_weeks_from_now():
    client = AmadeusClient()
    origin = 'NYC'
    destination = 'CHI'
    flight_data = client.search_flights(origin, destination)
    flight_itinerary = flight_data['data'][0]
    departure_str = flight_itinerary['itineraries'][0]['segments'][0]['departure']['at']
    datetime_object = datetime.strptime(departure_str, '%Y-%m-%dT%H:%M:%S')
    response_datetime_str = datetime_object.strftime('%Y-%m-%d')
    two_weeks_from_now = datetime.today() + timedelta(days=14)
    assert response_datetime_str == two_weeks_from_now.strftime('%Y-%m-%d')

def test_search_and_write_to_file_writes_json_to_data_folder():
    client = AmadeusClient()
    origin = 'NYC'
    destination = 'CHI'
    client.search_and_write(origin, destination)
    files = os.listdir('./data')
    last_file = files[-1]
    assert last_file.startswith('NYC-CHI-')

