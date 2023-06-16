import boto3
lambda_client = boto3.client('lambda')
import json

def extract_load(origin = 'NYC', destination = 'CHI', time_delta = 14):
    event = {'origin': origin, 'destination': destination,
             'time_delta': time_delta}
    jsonified_event = json.dumps(event)
    function_name = 'flights-app-dev-extract_load'
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload=jsonified_event
    )
    
    return response['ResponseMetadata']['RequestId']

def transform_load(file_name_read = 'raw/NYC-CHI-2023-06-30.json'):
    function_name = 'flights-app-dev-transform_load'
    event = {"file_name_read": file_name_read}
    jsonified_event = json.dumps(event)
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload=jsonified_event 
    )
    
    return response['ResponseMetadata']['RequestId']

