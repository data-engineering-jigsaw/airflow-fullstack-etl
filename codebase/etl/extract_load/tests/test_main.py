from main import lambda_handler
from datetime import datetime, timedelta
from src.file_writer import read_data_from, generate_file_name
def test_lambda_hander():
    two_weeks = datetime.today() + timedelta(days = 14)
    departure_date_str = two_weeks.strftime('%Y-%m-%d')
    origin = 'NYC'
    destination = 'CHI'
    context = {}
    event = {"origin": origin, "destination": destination, 'departure_date_str': departure_date_str}
    
    lambda_handler(event, context)
    file_name = generate_file_name(origin, destination, departure_date_str)
    
    bucket_name = 'amadeusflightjigsaw'
    bucket_data = read_data_from(bucket_name, file_name)
    first_instance_keys = ['type', 'id', 'source', 'instantTicketingRequired',
                             'nonHomogeneous', 'oneWay', 'lastTicketingDate', 'lastTicketingDateTime',
                               'numberOfBookableSeats', 'itineraries', 'price', 'pricingOptions', 'validatingAirlineCodes', 'travelerPricings']
    assert list(bucket_data['data'][0].keys()) == first_instance_keys
    