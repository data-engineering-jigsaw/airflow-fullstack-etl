import boto3
import json

from src.flights_file_reader import FlightsFileReader

bucket_name = 'amadeusflightjigsaw'
import_file_name = 'raw/NYC-CHI-2023-06-28.json'
file_reader = FlightsFileReader()
data = file_reader.read_from_bucket(bucket_name, import_file_name)
print(data)
# with open('./data') as file
    

