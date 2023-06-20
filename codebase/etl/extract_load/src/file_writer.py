import boto3
import json
from src.amadeus_client import AmadeusClient
from datetime import datetime, timedelta
s3 = boto3.client('s3')

def generate_file_name(origin, destination, departure_date_str, folder_name = 'raw'):
    pass

def search_and_upload(origin, destination, dest_file, departure_date_str):
    pass

def write_to_s3(bucket_data, bucket_name, file_name):
    s3 = boto3.client('s3')
    binary_data = bytes(json.dumps(bucket_data).encode('UTF-8'))
    return s3.put_object(Body=binary_data, Bucket=bucket_name, Key=file_name)

def read_data_from(bucket, object):
    obj = s3.get_object(Bucket=bucket, Key=object)
    text = obj['Body'].read()
    data = json.loads(text)
    return data