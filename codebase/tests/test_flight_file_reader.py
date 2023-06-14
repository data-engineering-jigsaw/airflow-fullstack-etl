from etl.flights_file_reader import FlightsFileReader
def test_file_reader_returns_selected_attrs():
    file_reader = FlightsFileReader()
    filename = './data/NYC-CHI-2023-06-28.json'
    selected_flights = file_reader.return_flights_from(filename)
    first_record = {'departure_time': '2023-06-28T06:00:00', 'arrival_time': '2023-06-28T07:33:00', 'departure_airport': 'LGA', 'arrival_airport': 'ORD'}
    second_record = {'departure_time': '2023-06-28T07:30:00', 'arrival_time': '2023-06-28T09:05:00', 'departure_airport': 'LGA', 'arrival_airport': 'ORD'}
    assert selected_flights[0] == first_record
    assert selected_flights[1] == second_record
    assert len(selected_flights) == 147