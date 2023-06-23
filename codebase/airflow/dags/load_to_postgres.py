import boto3
import pandas as pd
import psycopg2
import io
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from utils import build_conn
import json

s3_client = boto3.client('s3')


def get_s3_data(s3_file_key):
    s3_bucket = 'amadeusflightjigsaw'
    response = s3_client.get_object(Bucket=s3_bucket, Key=s3_file_key)
    file_content = response['Body'].read().decode('utf-8')
    cols = ['departure_time','arrival_time','departure_airport','arrival_airport']
    df = pd.read_json(file_content)
    return df[cols]

def copy_data(s3_df, db_name, table_name):
    pg_conn = build_conn(db_name)
    pg_cursor = pg_conn.cursor()
    col_str = ', '.join(s3_df.columns)
    copy_command = f"""COPY {table_name} ({col_str}) FROM STDIN DELIMITER ',' CSV HEADER;"""
    s3_data = s3_df.to_csv(index = False)
    pg_cursor.copy_expert(copy_command, io.StringIO(s3_data))
    pg_cursor.execute(f'select * from {table_name} order by id desc limit 3')
    last_records = pg_cursor.fetchall()
    pg_conn.commit()
    pg_conn.close()
    return json.dumps(last_records, default = str)

def load_data_from(s3_file):
    db_name = 'flightsdb'
    s3_df = get_s3_data(s3_file)
    copy_data(s3_df, db_name, 'flights')