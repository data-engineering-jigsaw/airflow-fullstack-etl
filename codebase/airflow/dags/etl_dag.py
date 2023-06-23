import boto3


from airflow import DAG
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from load_to_postgres import load_data_from
from lambda_caller import *
from utils import *
import logging

default_args = {'start_date': days_ago(1)}

@dag(schedule_interval='@once', default_args=default_args, catchup=False)
def etl_dag():
    @task
    def extract_load_task(origin, destination, departure_date_str):
        
        result = extract_load(origin = origin, destination = destination, 
                              departure_date_str = departure_date_str)
        logging.info(f'extracting data from: {origin}, {destination}, departure: {departure_date_str}')
        logging.info(f'extract load lambda id: {result}')
        
        return result

    @task
    def transform_load_task(origin, destination, departure_date_str):
        file_name = generate_file_name(origin, destination, departure_date_str)
        # print(file_name)
        file_name_read = f"raw/{file_name}"
        result = transform_load(file_name_read = file_name_read)
        logging.info(f'reading data from file: {file_name_read}')
        logging.info(f'transform load: {result}')
        return result
    
    @task
    def load_data_from_to_db(s3_file):
        logging.info(f'loading data from file: {s3_file}')
        last_records = load_data_from(s3_file)
        logging.info(f'records inserted: {last_records}')


    origin = "NYC" #"PHI"
    destination = "CHI"
    departure_date_str = "2023-08-12"
    extract_and_load_data = extract_load_task(origin, destination, departure_date_str)
    load_and_transform_data = transform_load_task(origin, destination, departure_date_str)
    file_name = generate_file_name(origin, destination, departure_date_str)
    load_to_db = load_data_from_to_db(f'transformed/{file_name}')
    extract_and_load_data >> load_and_transform_data >> load_to_db


dag = etl_dag()