import boto3

route_table_id = 'rtb-0320ae62372195b8a'
internet_gateway_id = 'igw-0f3d9e203fe07b114'

ec2 = boto3.client('ec2')

ec2.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway_id, RouteTableId=route_table_id)


