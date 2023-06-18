from src.file_writer import *
from datetime import timedelta, datetime

def lambda_handler(event, context):
    origin = event.get('origin', 'NYC')
    destination = event.get('destination', 'CHI')
    departure_date_str = event.get('departure_date_str', None) # "%Y-%m-%d"

    departure_date = build_departure_date(departure_date_str)
    file_name = generate_file_name(origin, destination, 
                                            departure_date = departure_date)
    print(file_name)
    
    response = search_and_upload(origin, destination,
                                  file_name, departure_date)
    return response

# context = {}
# event = {'origin': 'NYC', 'destination': 'CHI','departure_date_str': '2023-6-21'}
# lambda_handler(event, context)

