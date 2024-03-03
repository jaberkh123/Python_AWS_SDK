import boto3

# Specify your AWS credentials and region
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_Secret'
aws_region = 'Region'

# Create an EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Specify the AMI ID for Amazon Linux 2 (replace it with the desired AMI)
ami_id = 'ami-xxxxxxxxxx'

# Specify the instance type (T2 Micro in this case)
instance_type = 't2.micro'

# Specify the key pair name for SSH access (replace it with your key pair)
key_name = 'Your_key_pair'

# Specify the security group IDs (replace them with your security group IDs)
security_group_ids = ['sg-xxxxxxxxxxxx']

# Specify the subnet ID (replace it with your subnet ID)
#Leave it if you want to use default subnet:
#subnet_id = 'subnet-xxxxxxxxxxxxxxxxx'

# Launch the EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    #SubnetId=subnet_id,(must be uncomment if you wont use default subnet)
    MinCount=1,
    MaxCount=1
)

# Print the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance {instance_id} created successfully.")

