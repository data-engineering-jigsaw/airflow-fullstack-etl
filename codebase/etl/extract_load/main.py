from src.file_writer import *
from datetime import timedelta, datetime

def lambda_handler(event, context):
    
    origin = event.get('origin', 'NYC')
    destination = event.get('destination', 'CHI')
    departure_date_str = event.get('departure_date_str', '2023-06-23') # "%Y-%m-%d"

    file_name = generate_file_name(origin, destination, 
                                    departure_date_str = departure_date_str, folder_name = 'raw')
    print(file_name)
    
    response = search_and_upload(origin, destination,
                                  file_name, departure_date_str)
    return response



# context = {}
# event = {"origin": "NYC", "destination": "CHI", "departure_date_str": "2023-08-02"}
# lambda_handler(event, context)