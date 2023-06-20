from src.flight_adapter import AmadeusFlightAdapter
import pandas as pd
import json
import boto3
from io import BytesIO

class FlightsFileReader:
    def return_flights_from_bucket(self, bucket_name, obj_name):
        pass
        
    def select_attributes(self, flights_json):
        pass
    
    def read_from_bucket(self, bucket_name, obj_name):
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket_name, Key=obj_name)
        data = obj['Body'].read()
        new_str = data.decode('utf-8')
        d = json.loads(new_str)
        return d

    def write_to_s3(self, bucket_data, bucket_name, file_name):
        s3 = boto3.client('s3')
        binary_data = bytes(json.dumps(bucket_data).encode('UTF-8'))
        return s3.put_object(Body=binary_data, Bucket=bucket_name, Key=file_name)
        
        