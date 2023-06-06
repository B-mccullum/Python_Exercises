import boto3

route_table_id = "rtb-0320ae62372195b8a"

ec2 = boto3.client('ec2')

# Retrieve information about the specified route table
response = ec2.describe_route_tables(RouteTableIds=[route_table_id])

# Iterate over the associations of the route table
for association in response["RouteTables"][0]["Associations"]:
    # Check if the association is not the main route table
    if not association["Main"]:
        # Retrieve the association ID
        association_id = association["RouteTableAssociationId"]
        # Print the association ID
        print(association_id)
        # Disassociate the route table from the association
        ec2.disassociate_route_table(AssociationId=association_id)


