import boto3
import time

def delete_all_api_gateways(access_key, secret_key, region_name):
    # Create an API Gateway client
    client = boto3.client('apigateway', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

    # Rest of the code remains unchanged
    # ...
    apis = client.get_rest_apis()

    # Loop through each API and delete it
    for api in apis['items']:
        api_id = api['id']
        print(f"Deleting API Gateway: {api_id}")
        client.delete_rest_api(restApiId=api_id)
        # we need to sleep, deletinig Api is a sensitive job and you can not do this without time wait
        time.sleep(60)

    print("All API Gateways deleted.")

# Replace 'YOUR_ACCESS_KEY', 'YOUR_SECRET_KEY', and 'YOUR_REGION' with your AWS credentials and region
access_key = 'Your_Access_Key'
secret_key = 'Your_Secret'
region_name = 'Region'

# Call the function to delete all API Gateways
delete_all_api_gateways(access_key, secret_key, region_name)
