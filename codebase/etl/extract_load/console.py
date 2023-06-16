from src.file_writer import *
# client = AmadeusClient()
# client.search_and_write(origin, destination, departure_date = None)

origin = 'NYC'
destination = 'CHI'
returned_payload = search_and_upload(origin, destination)
