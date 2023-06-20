import boto3
import json
from src.flights_file_reader import FlightsFileReader

def lambda_handler(event, context):
    file_name_read = event.get('file_name_read')
    bucket_name = 'amadeusflightjigsaw'
    file_reader = FlightsFileReader()
    bucket_data = file_reader.return_flights_from_bucket(bucket_name, file_name_read)
    file_name = file_name_read.split('/')[-1]

    return file_reader.write_to_s3(bucket_data, bucket_name, f'transformed/{file_name}')


# event = {"file_name_read": "raw/NYC-CHI-2023-07-06.json"}
# context = {}
# lambda_handler(event, context)