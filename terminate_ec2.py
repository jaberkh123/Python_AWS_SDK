import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_region'

# Replace 'your_instance_id' with the actual ID of the instance you want to terminate
instance_id_to_terminate = 'your_instance_id'

# Create an EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Terminate the instance
response = ec2_client.terminate_instances(InstanceIds=[instance_id_to_terminate])

# Print the termination response
print(response)
