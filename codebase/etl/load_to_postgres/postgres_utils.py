import psycopg2
import boto3
rds_client = boto3.client('rds')

def get_endpoint():
    instance_identifier = "flights-db"
    response = rds_client.describe_db_instances(
        DBInstanceIdentifier=instance_identifier
    )
    return response['DBInstances'][0]['Endpoint']['Address']

def build_conn(db_name):
    endpoint = get_endpoint()
    conn = psycopg2.connect(
    host=endpoint,
    port=5432,
    dbname=db_name,
    user='jigsaw',
    password='jigsawlabs')
    return conn