import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_secret'
aws_region = 'Region'

# Replace 'your_bucket_name' and 'your_file_path' with your actual S3 bucket name and file path
bucket_name = 'Your_bucket_name'
file_path = 'Your_file_path'

# Create an S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Upload the file to S3
with open(file_path, 'rb') as file_data:
    s3_client.put_object(Bucket=bucket_name, Key='lambda.zip', Body=file_data)

print(f"File uploaded to S3 bucket '{bucket_name}' with key 'your_destination_key'")
