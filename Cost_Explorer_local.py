import boto3

def get_aws_billing_data():
    # Replace 'your_aws_access_key' and 'your_aws_secret_key' with your actual AWS credentials
    aws_access_key = 'AKIAZI2LHIMVDVXJOGPX'
    aws_secret_key = 'DO9p5C2MQTiemIRumMjF2pNFoY50oGkxn0TPPhUQ'
    
    # Replace 'your_aws_region' with your AWS region, e.g., 'us-east-1'
    aws_region = 'us-east-1'

    # Create a Cost Explorer client
    ce_client = boto3.client('ce', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

    # Define the time period for which you want to retrieve cost and usage data
    start_date = '2024-01-01'
    end_date = '2024-02-26'

    # Get cost and usage data
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',  # You can change this to 'DAILY' if needed
        Metrics=['BlendedCost']  # You can customize the metrics you want to retrieve
    )

    # Print the cost and usage data
    print(response)

if __name__ == "__main__":
    get_aws_billing_data()
