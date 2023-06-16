import boto3
import json

from src.flights_file_reader import FlightsFileReader



file_reader = FlightsFileReader()
bucket_name = 'amadeusflightjigsaw'
file_name = 'raw/NYC-CHI-2023-06-29.json'

bucket_data = file_reader.return_flights_from_bucket(bucket_name, file_name)
extracted_file_name = file_name.split('/')[-1]
file_reader.write_to_s3(bucket_data, bucket_name, file_name)


# 
# read_and_upload(file_name, bucket_name, f'transformed/{extracted_file_name}')
# write_to_file(flight_data, file_name)

