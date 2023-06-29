from dotenv import load_dotenv
import os

load_dotenv()
db_username = os.getenv('db_username')
db_password = os.getenv('db_password')
db_instance_name = os.getenv('db_instance_name')
initial_db = os.getenv('initial_db')
db_name = os.getenv('db_name') 