from src.file_writer import *
from datetime import timedelta, datetime

def lambda_handler(event, context):
    origin = event.get('origin', 'NYC')
    destination = event.get('destination', 'CHI')
    time_delta = event.get('time_delta', 14)
    departure_date = datetime.today() + timedelta(days=time_delta)
    
    file_name = generate_file_name(origin, destination, 
                                            departure_date = departure_date)

    response = search_and_upload(origin, destination, file_name, departure_date)
    return response

# context = {}
# event = {'origin': 'NYC', 'destination': 'CHI','time_delta': 3}


