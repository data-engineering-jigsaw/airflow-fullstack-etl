import boto3


from airflow import DAG
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from lambda_handler import *
from utils import *

default_args = {'start_date': days_ago(1)}

@task
def extract_load_task(origin, destination, time_delta = 14):
    result = extract_load(origin = 'NYC', destination = 'CHI', time_delta = time_delta)
    return result

@task
def transform_load_task():
    result = transform_load()
    return result

@dag(schedule_interval='@once', default_args=default_args, catchup=False)
def hello_world(origin, destination, time_delta = 14):
    departure_date = generate_departure_date()
    file_name = generate_file_name(origin, destination, departure_date)

    data = extract_load_task(origin, destination, time_delta)
    result = transform_load_task(file_name_read = file_name)

dag = hello_world(origin = 'NYC', destination = 'CHI')

