from src.flights_file_reader import FlightsFileReader
from main import lambda_handler
def test_lambda_handler():
    file_name = 'NYC-CHI-2023-07-06.json'
    event = {'file_name_read': f'raw/{file_name}'}
    context = {}
    lambda_handler(event, context)
    bucket_name = 'amadeusflightjigsaw'
    returned_data = FlightsFileReader().read_from_bucket(bucket_name, f'transformed/{file_name}')
    assert list(returned_data[0].keys()) == ['departure_time', 'arrival_time', 
                                            'departure_airport', 'arrival_airport',
                                            'total_price']
    assert len(returned_data) > 5
