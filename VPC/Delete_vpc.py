import boto3

vpc_id = "vpc-0ec98404fa527970e"

ec2 = boto3.client('ec2')

# Delete the specified VPC
ec2.delete_vpc(VpcId=vpc_id)

