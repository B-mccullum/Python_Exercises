import boto3 

ec2 = boto3.client('ec2')

# Retrieve information about all EC2 instances
response = ec2.describe_instances()

# Iterate over each reservation
for reservation in response["Reservations"]:
    # Iterate over each instance within the reservation
    for instance in reservation["Instances"]:
        # Print basic information about the instance
        print(instance["InstanceId"], instance["InstanceType"], instance["ImageId"], 
              instance["VpcId"], instance["SubnetId"], instance["State"]["Name"])
        
        # Iterate over tags associated with the instance
        for tag in instance["Tags"]:
            # Print the value of the "Name" tag
            if tag["Key"] == "Name":
                print(tag["Value"])
                
        # Iterate over security groups associated with the instance
        for sg in instance["SecurityGroups"]:
            # Print the ID and name of each security group
            print(sg["GroupId"], sg["GroupName"])
            
        # Print the public IP address of the instance, if available
        if "PublicIpAddress" in instance:
            print(instance["PublicIpAddress"])
            
        # Print the key name associated with the instance, if available
        if "KeyName" in instance:
            print(instance["KeyName"])
        
        # Print the ID and ARN of the IAM instance profile associated with the instance, if available
        if "IamInstanceProfile" in instance:
            print(instance["IamInstanceProfile"]["Id"], instance["IamInstanceProfile"]["Arn"])
