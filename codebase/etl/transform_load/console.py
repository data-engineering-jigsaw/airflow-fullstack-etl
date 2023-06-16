import boto3
import json

from src.flights_file_reader import FlightsFileReader

def lambda_handler(event, context):
    file_reader = FlightsFileReader()
    bucket_name = 'amadeusflightjigsaw'
    file_name = 'NYC-CHI-2023-06-29.json'
    import_file_name = f'raw/{file_name}'
    export_name = f'transformed/{file_name}'
    
    bucket_data = file_reader.return_flights_from_bucket(bucket_name, import_file_name)
    extracted_file_name = file_name.split('/')[-1]
    return file_reader.write_to_s3(bucket_data, bucket_name, export_name)

