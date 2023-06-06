import boto3

subnet_id = "subnet-088a7ccc76b035879"

ec2 = boto3.client('ec2')

# Delete the specified subnet
ec2.delete_subnet(SubnetId=subnet_id)

