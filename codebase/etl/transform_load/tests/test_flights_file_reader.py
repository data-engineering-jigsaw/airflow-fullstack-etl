from src.flights_file_reader import *
from tests.data import flights_json

def test_file_reader_returns_selected_attrs_of_each_flight():
    file_reader = FlightsFileReader()
    flights_selected_attrs = file_reader.select_attributes(flights_json)
    assert flights_selected_attrs[0] == {'departure_time': '2023-06-28T06:00:00', 'arrival_time': '2023-06-28T07:33:00', 
                                     'departure_airport': 'LGA', 
                                     'arrival_airport': 'ORD', 'total_price': '148.25'}
    assert len(flights_selected_attrs) == 132

def test_return_flights_from_bucket():
    file_reader = FlightsFileReader()
    bucket_name = 'amadeusflightjigsaw'
    obj_name = 'raw/NYC-CHI-2023-06-28.json'
    selected_flights = file_reader.return_flights_from_bucket(bucket_name, 
                                                              obj_name)
    assert list(selected_flights[0].keys()) == ['departure_time', 'arrival_time', 
                                                'departure_airport', 'arrival_airport', 'total_price']
    assert len(selected_flights) > 5