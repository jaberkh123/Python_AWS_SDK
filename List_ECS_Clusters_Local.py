#A script for list ECS cluster  from local system
import boto3

def get_ecs_clusters(aws_access_key_id, aws_secret_access_key, aws_region):
    # Create an ECS client
    ecs = boto3.client('ecs', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Retrieve information about ECS clusters
    response = ecs.describe_clusters()

    clusters_info = []

    # Extract relevant information about each cluster
    for cluster in response['clusters']:
        cluster_info = {
            'ClusterName': cluster['clusterName'],
            'ClusterArn': cluster['clusterArn'],
            'Status': cluster['status'],
            'RegisteredContainerInstancesCount': cluster['registeredContainerInstancesCount'],
            'RunningTasksCount': cluster['runningTasksCount'],
            'PendingTasksCount': cluster['pendingTasksCount']
        }
        clusters_info.append(cluster_info)

    return clusters_info

# Example usage
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_aws_region'

ecs_clusters = get_ecs_clusters(aws_access_key_id, aws_secret_access_key, aws_region)

# Print information about each ECS cluster
for cluster in ecs_clusters:
    print(f"Cluster Name: {cluster['ClusterName']}")
    print(f"Cluster ARN: {cluster['ClusterArn']}")
    print(f"Status: {cluster['Status']}")
    print(f"Registered Container Instances Count: {cluster['RegisteredContainerInstancesCount']}")
    print(f"Running Tasks Count: {cluster['RunningTasksCount']}")
    print(f"Pending Tasks Count: {cluster['PendingTasksCount']}")
    print("--------------")

