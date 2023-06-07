import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-046d6752cc338a2e6'
)

print(response)
