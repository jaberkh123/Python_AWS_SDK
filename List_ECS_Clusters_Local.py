#A script for list ECS cluster  from local system
import boto3

def get_all_ecs_clusters(aws_access_key_id, aws_secret_access_key, aws_region):
    # Create an ECS client
    ecs = boto3.client('ecs', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # List all ECS clusters
    response = ecs.list_clusters()

    clusters_info = []

    # Describe each cluster to get detailed information
    for cluster_arn in response.get('clusterArns', []):
        cluster_description = ecs.describe_clusters(clusters=[cluster_arn])
        cluster_info = {
            'ClusterName': cluster_description['clusters'][0]['clusterName'],
            'ClusterArn': cluster_arn,
            'Status': cluster_description['clusters'][0]['status'],
            'RegisteredContainerInstancesCount': cluster_description['clusters'][0]['registeredContainerInstancesCount'],
            'RunningTasksCount': cluster_description['clusters'][0]['runningTasksCount'],
            'PendingTasksCount': cluster_description['clusters'][0]['pendingTasksCount']
        }
        clusters_info.append(cluster_info)

    return clusters_info

# Example usage
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
aws_region = 'your_aws_region'

ecs_clusters = get_all_ecs_clusters(aws_access_key_id, aws_secret_access_key, aws_region)

# Print information about each ECS cluster
for cluster in ecs_clusters:
    print(f"Cluster Name: {cluster['ClusterName']}")
    print(f"Cluster ARN: {cluster['ClusterArn']}")
    print(f"Status: {cluster['Status']}")
    print(f"Registered Container Instances Count: {cluster['RegisteredContainerInstancesCount']}")
    print(f"Running Tasks Count: {cluster['RunningTasksCount']}")
    print(f"Pending Tasks Count: {cluster['PendingTasksCount']}")
    print("--------------")
