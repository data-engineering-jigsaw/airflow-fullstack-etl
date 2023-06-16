import boto3
lambda_client = boto3.client('lambda')

def extract_load():
    function_name = 'flights-app-dev-extract_load'
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload='{"key1": "value1", "key2": "value2"}' 
    )
    response_payload = response['Payload'].read()
    return response_payload

def transform_load():
    function_name = 'flights-app-dev-transform_load'
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='Event',  
        Payload='{"key1": "value1", "key2": "value2"}'  
    )
    response_payload = response['Payload'].read()
    return response_payload