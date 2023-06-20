import boto3


from airflow import DAG
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from lambda_caller import *
from utils import *
import logging

default_args = {'start_date': days_ago(1)}

@dag(schedule_interval='@once', default_args=default_args, catchup=False)
def etl_dag():
    @task
    def extract_load_task(origin, destination, departure_date_str):
        pass

    @task
    def transform_load_task(origin, destination, departure_date_str):
        pass
    
    origin = "NYC" #"PHI"
    destination = "CHI"
    departure_date_str = "2023-08-8"
    data = extract_load_task(origin, destination, departure_date_str)
    result = transform_load_task(origin, destination, departure_date_str)

dag = etl_dag()