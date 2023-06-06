import boto3

route_table_id = "rtb-0320ae62372195b8a"

ec2 = boto3.client('ec2')

# Delete the specified route table
ec2.delete_route_table(RouteTableId=route_table_id)

