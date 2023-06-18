import boto3
import json
from src.amadeus_client import AmadeusClient
from datetime import datetime, timedelta
s3 = boto3.client('s3')

def search_and_write(origin, destination, departure_date = None):
    client = AmadeusClient()
    departure = client.generate_departure_date(departure_date, days = 14)
    flight_data = client.search_flights(origin, destination, 
                                        departureDate = departure)
    filename = generate_file_name(origin, destination, 
                                        departure_date = departure)
    write_to_file(flight_data, filename)

def search_and_upload(origin, destination, dest_file, departure_date = datetime.today() + timedelta(days = 14)):
    client = AmadeusClient()
    flight_data = client.search_flights(origin, destination, 
                                        departureDate = departure_date)
    bucket_name = 'amadeusflightjigsaw'
    write_to_s3(flight_data, bucket_name, dest_file)
    response = {'file': dest_file, 'flight_data': flight_data['data'][:3]}
    print(response)
    return response

def build_departure_date(departure_date_str):
    # take in string, return datetime
    if not departure_date_str:
        departure_date = (datetime.today() + timedelta(days=14))
    else:
        departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d")
    return departure_date


def write_to_s3(bucket_data, bucket_name, file_name):
    s3 = boto3.client('s3')
    binary_data = bytes(json.dumps(bucket_data).encode('UTF-8'))
    return s3.put_object(Body=binary_data, Bucket=bucket_name, Key=file_name)

def write_to_file(json_data, filename):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(json_data))

def generate_file_name(origin, destination, departure_date, folder_name = 'raw'):
    departure_date_str = departure_date.strftime("%Y-%m-%d")
    return f"{folder_name}/{origin}-{destination}-{departure_date_str}.json"

def read_and_upload(file_name, bucket_name, destination_object):
    # first arg is to read from ......... then write to
    return s3.upload_file(file_name, bucket_name, destination_object)

def read_data_from(bucket, object):
    obj = s3.get_object(Bucket=bucket, Key=object)
    text = obj['Body'].read()
    data = json.loads(text)
    return data


# fix dockerfile
# find difference in files read, and read the next ones
   
# https://docs.snowflake.com/en/user-guide/json-basics-tutorial-copy-into
