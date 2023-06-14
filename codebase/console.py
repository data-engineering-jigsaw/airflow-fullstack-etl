from etl.extract_load.amadeus_client import AmadeusClient
from etl.transform_load.flights_file_reader import FlightsFileReader

client = AmadeusClient()
origin = 'NYC'
destination = 'CHI'

file_reader = FlightsFileReader()
filename = './data/NYC-CHI-2023-06-28.json'
# file_reader.return_flights_from(filename)


# client.search_and_write(origin, destination, departure_date = None)