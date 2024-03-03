import boto3

# Specify your AWS credentials and region
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_Secret'
aws_region = 'Region'

# Create a Lambda client
lambda_client = boto3.client('lambda', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# List Lambda functions
response = lambda_client.list_functions()

# Print function details
for function in response['Functions']:
    print(f"Function Name: {function['FunctionName']}")
    print(f"Runtime: {function['Runtime']}")
    print(f"ARN: {function['FunctionArn']}")
    print("-" * 30)
