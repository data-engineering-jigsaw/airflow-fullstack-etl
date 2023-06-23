import boto3
import io
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from postgres_utils import build_conn

def create_database():
    conn = build_conn('postgres')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute("create database if not exists flightsdb")
    conn.commit()
    conn.close()

def create_table():
    conn = build_conn('flightsdb')
    cursor = conn.cursor()
    sql = open("./create_table.sql", "r").read()
    cursor.execute(sql)
    conn.commit()