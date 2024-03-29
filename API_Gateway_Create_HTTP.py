import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_region'

# Replace with your API details
api_name = 'YourApiName'
protocol_type = 'HTTP'

# Create an API Gateway V2 client
api_gateway_client = boto3.client('apigatewayv2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Create API
response = api_gateway_client.create_api(
    Name=api_name,
    ProtocolType=protocol_type
)

api_id = response['ApiId']
print(f"API created with ID: {api_id}")
