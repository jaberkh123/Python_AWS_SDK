import boto3
#this script must run from local system
def get_ec2_instances(aws_access_key_id, aws_secret_access_key, aws_region):
    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Retrieve information about EC2 instances
    response = ec2.describe_instances()

    instances_info = []

    # Extract relevant information about each instance
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceID': instance['InstanceId'],
                'Name': next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), 'N/A'),
                'InstanceType': instance['InstanceType'],
                'PublicIPAddress': instance.get('PublicIpAddress', 'N/A'),
                'PrivateIPAddress': instance['PrivateIpAddress'],
                'State': instance['State']['Name']
            }
            instances_info.append(instance_info)

    return instances_info

# Example usage
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_Secret'
aws_region = 'Region'

instances = get_ec2_instances(aws_access_key_id, aws_secret_access_key, aws_region)

# Print information about each instance
for instance in instances:
    print(f"Instance ID: {instance['InstanceID']}")
    print(f"Instance Name: {instance['Name']}")
    print(f"Instance Type: {instance['InstanceType']}")
    print(f"Public IP Address: {instance['PublicIPAddress']}")
    print(f"Private IP Address: {instance['PrivateIPAddress']}")
    print(f"State: {instance['State']}")
    print("--------------")
