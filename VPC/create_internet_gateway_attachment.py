import boto3

internet_gatewat_id = 'igw-0f3d9e203fe07b114'
vpc_id = 'vpc-0ec98404fa527970e'

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(InternetGatewayId=internet_gatewat_id, VpcId=vpc_id)
