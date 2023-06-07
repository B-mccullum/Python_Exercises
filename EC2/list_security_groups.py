import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

# Extract the desired information from each security group and its permissions
for sg in response["SecurityGroups"]:
    sg_id = sg["GroupId"]
    vpc_id = sg["VpcId"]
    name = sg["GroupName"]
    description = sg["Description"]

    print(sg_id, vpc_id, name, description)

    # Iterate over the permissions of the security group
    for permission in sg["IpPermissions"]:
        from_port = permission.get("FromPort")
        ip_protocol = permission.get("IpProtocol")
        to_port = permission.get("ToPort")

        # Print the from_port, ip_protocol, and to_port if they exist
        if from_port is not None:
            print(from_port)

        if ip_protocol is not None:
            print(ip_protocol)

        if to_port is not None:
            print(to_port)

        # Iterate over the IP ranges in the permission
        for ip_range in permission.get("IpRanges", []):
            cidr_ip = ip_range.get("CidrIp")
            if cidr_ip is not None:
                print(cidr_ip)
