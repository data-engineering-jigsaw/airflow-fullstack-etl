import boto3
import json
from src.amadeus_client import AmadeusClient
from datetime import datetime, timedelta
s3 = boto3.client('s3')

def generate_file_name(origin, destination, departure_date_str, folder_name = 'raw'):
    departure_date_str = datetime.strptime(departure_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    return f"{folder_name}/{origin}-{destination}-{departure_date_str}.json"

def search_and_upload(origin, destination, dest_file, departure_date_str):
    client = AmadeusClient()
    flight_data = client.search_flights(origin, destination, 
                                        departure_date_str = departure_date_str)
    bucket_name = 'amadeusflightjigsaw'
    write_to_s3(flight_data, bucket_name, dest_file)
    flight_data = read_data_from(bucket_name, dest_file)
    response = {'file': dest_file, 'flight_data': flight_data['data'][:3]}
    return response

def write_to_s3(bucket_data, bucket_name, file_name):
    s3 = boto3.client('s3')
    binary_data = bytes(json.dumps(bucket_data).encode('UTF-8'))
    return s3.put_object(Body=binary_data, Bucket=bucket_name, Key=file_name)

def read_data_from(bucket, object):
    obj = s3.get_object(Bucket=bucket, Key=object)
    text = obj['Body'].read()
    data = json.loads(text)
    return data


# fix dockerfile
# find difference in files read, and read the next ones
   
# https://docs.snowflake.com/en/user-guide/json-basics-tutorial-copy-into
