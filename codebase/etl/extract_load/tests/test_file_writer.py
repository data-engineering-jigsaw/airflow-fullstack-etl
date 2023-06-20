from src.file_writer import generate_file_name, search_and_upload

def test_generate_file_name():
    origin = 'NYC'
    destination = 'CHI'
    departure_date_str = '2023-06-28'
    file_name = generate_file_name(origin, destination, departure_date_str)
    assert file_name == 'raw/NYC-CHI-2023-06-28.json'

def test_generate_file_name_coerces_strings_without_two_digits():
    origin = 'NYC'
    destination = 'CHI'
    departure_date_str = '2023-6-28'
    file_name = generate_file_name(origin, destination, departure_date_str)
    assert file_name == 'raw/NYC-CHI-2023-06-28.json'

def test_file_reader_returns_selected_attrs():
    origin = 'NYC'
    destination = 'CHI'
    departure_date_str = '2023-6-28'
    dest_file = generate_file_name(origin, destination, departure_date_str, folder_name = 'raw')
    results = search_and_upload(origin, destination, dest_file, departure_date_str)
    assert results['file'] == dest_file
    first_instance_keys = ['type', 'id', 'source', 'instantTicketingRequired',
                             'nonHomogeneous', 'oneWay', 'lastTicketingDate', 'lastTicketingDateTime',
                               'numberOfBookableSeats', 'itineraries', 'price', 'pricingOptions', 'validatingAirlineCodes', 'travelerPricings']
    assert list(results['flight_data'][0].keys()) == first_instance_keys
    assert len(results['flight_data']) == 3
    