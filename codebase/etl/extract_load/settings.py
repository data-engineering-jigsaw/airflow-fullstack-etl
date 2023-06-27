from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
bucket_name = os.getenv('bucket_name')

