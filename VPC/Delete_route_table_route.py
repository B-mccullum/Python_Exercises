import boto3

route_table_id = "rtb-0320ae62372195b8a"

ec2 = boto3.client('ec2')

ec2.delete_route(DestinationCidrBlock='0.0.0.0/0', RouteTableId=route_table_id)

