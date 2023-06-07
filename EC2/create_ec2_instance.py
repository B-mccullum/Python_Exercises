import boto3  # Importing the boto3 library for interacting with AWS services

def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    response = client.run_instances(
            ImageId=ami_id,  # Specify the AMI ID
            InstanceType='t2.micro',  # Specify the instance type
            KeyName=key_pair_name,  # Specify the key pair name
            MaxCount=1,  # Specify the maximum number of instances to launch
            MinCount=1,  # Specify the minimum number of instances to launch
            SecurityGroupIds=[security_group_id
            ],# Specify the security group ID
            UserData=user_data
    
    )
        
    print(response["Instances"][0]["InstanceId"])  # Print the ID of the launched instance

# Specify the required parameters
ami_id = "ami-0355aa3549eab6e12"  # ID of the Amazon Machine Image (AMI) to launch
key_pair_name = "Key from Boto3"  # Name of the key pair for SSH access
security_group_id = "sg-046d6752cc338a2e6"  # ID of the security group to associate with the instance

user_data='''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')  # Creating an EC2 client object
create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)