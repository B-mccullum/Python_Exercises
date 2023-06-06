import boto3

internet_gateway_id = "igw-0f3d9e203fe07b114"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(InternetGatewayId=internet_gateway_id)

