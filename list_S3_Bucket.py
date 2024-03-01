import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'Your_access_Key'
aws_secret_access_key = 'Your_Secret'
aws_region = 'Region'

# Create an S3 client
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# List S3 buckets
response = s3_client.list_buckets()

# Print the bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])
