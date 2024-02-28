#You can run this script in an instance in AWS
#Remember your instance must has permission to access instances
import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve information about EC2 instances
response = ec2.describe_instances()

# Print information about each instance
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP Address: {instance['PrivateIpAddress']}")
        print(f"State: {instance['State']['Name']}")
        print("--------------")
