import boto3
import io
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from postgres_utils import build_conn
from settings import db_username, db_password, db_instance_name, initial_db
def create_database():
    conn = build_conn(initial_db)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"create database if not exists {db_instance_name}")
    conn.commit()
    conn.close()

def create_table():
    conn = build_conn(db_instance_name)
    cursor = conn.cursor()
    sql = open("./create_table.sql", "r").read()
    cursor.execute(sql)
    conn.commit()