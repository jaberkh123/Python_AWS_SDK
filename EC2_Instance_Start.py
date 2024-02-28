# An script for run existing instances
import boto3

def start_ec2_instance(aws_access_key_id, aws_secret_access_key, aws_region, instance_id):
    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Start the existing EC2 instance
    ec2.start_instances(InstanceIds=[instance_id])

    print(f"EC2 instance {instance_id} is starting...")

# Example usage
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_Secret'
aws_region = 'Region'
existing_instance_id = 'instance_ID'  # Replace with your existing instance ID

start_ec2_instance(aws_access_key_id, aws_secret_access_key, aws_region, existing_instance_id)
