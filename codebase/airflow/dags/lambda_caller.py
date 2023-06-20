import boto3
from utils import generate_file_name
lambda_client = boto3.client('lambda')
import json

def extract_load(origin, destination, departure_date_str):
    event = {"origin": origin,
              "destination": destination,
                "departure_date_str": departure_date_str}
    function_name = 'flights-app-dev-extract_load'
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload=json.dumps(event)
    )
    
    return response['ResponseMetadata']['RequestId']

def transform_load(file_name_read):
    pass

origin = "NYC"
destination = "CHI"
departure_date_str = "2023-07-5"
extract_load(origin = origin, destination = destination,
               departure_date_str = departure_date_str)
# file_name = generate_file_name(origin, destination, departure_date_str)
# result = transform_load(file_name_read = f'raw/{file_name}')
