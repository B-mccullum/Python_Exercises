import boto3

routeTable_id = 'rtb-0320ae62372195b8a'
subnet_id = 'subnet-088a7ccc76b035879'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(RouteTableId=routeTable_id, SubnetId=subnet_id)

print(association["AssociationId"])