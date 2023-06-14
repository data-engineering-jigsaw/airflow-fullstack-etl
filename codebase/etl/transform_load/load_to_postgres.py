import boto3
import psycopg2
import io

# Set up the AWS S3 and PostgreSQL connections
s3_client = boto3.client('s3')
pg_conn = psycopg2.connect(
    host='your_postgres_host',
    port=your_postgres_port,
    dbname='your_database_name',
    user='your_username',
    password='your_password'
)

# Define the S3 bucket and file you want to copy
s3_bucket = 'your_s3_bucket_name'
s3_file_key = 'path/to/your/file.csv'

# Download the file from S3
response = s3_client.get_object(Bucket=s3_bucket, Key=s3_file_key)
file_content = response['Body'].read().decode('utf-8')

# Connect to the PostgreSQL database and execute the copy command
pg_cursor = pg_conn.cursor()

# Assuming your PostgreSQL table has already been created
# Adjust the COPY command based on your table structure and file format
copy_command = f"COPY your_table_name FROM STDIN WITH (FORMAT csv, DELIMITER ',', HEADER true)"
pg_cursor.copy_expert(copy_command, io.StringIO(file_content))
pg_conn.commit()

# Close the connections
pg_cursor.close()
pg_conn.close()