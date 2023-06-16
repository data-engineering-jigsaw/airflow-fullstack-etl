from src.file_writer import *


def lambda_handler(event, context):
    origin = 'NYC'
    destination = 'CHI'
    return search_and_upload(origin, destination)