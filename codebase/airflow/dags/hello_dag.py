import boto3


from airflow import DAG
from airflow.decorators import task, dag
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup

from lambda_handler import *

default_args = {'start_date': days_ago(1)}

@task
def extract_load_task():
    result = extract_load()
    return result

@dag(schedule_interval='@once', default_args=default_args, catchup=False)
def hello_world():
    data = extract_load_task()

dag = hello_world()