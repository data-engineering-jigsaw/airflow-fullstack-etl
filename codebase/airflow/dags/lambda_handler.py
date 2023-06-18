import boto3
from utils import generate_file_name
lambda_client = boto3.client('lambda')
import json

def extract_load(origin = 'NYC', destination = 'CHI', departure_date_str = '2023-6-21'):
    event = {'origin': origin, 'destination': destination,
             'departure_date_str': departure_date_str}
    jsonified_event = json.dumps(event)
    function_name = 'flights-app-dev-extract_load'
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload=jsonified_event
    )
    
    return response['ResponseMetadata']['RequestId']

def transform_load(file_name_read = 'raw/2023-6-21.json'):
    function_name = 'flights-app-dev-transform_load'
    event = {"file_name_read": file_name_read}
    jsonified_event = json.dumps(event)
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload=jsonified_event 
    )
    
    return response['ResponseMetadata']['RequestId']

origin = 'NYC'
destination = 'CHI'
departure_date_str = '2023-7-4'
# extract_load(origin = origin, destination = destination, departure_date_str = departure_date_str)
file_name = generate_file_name(origin, destination, departure_date_str)
# result = transform_load(file_name_read = f'raw/{file_name}')