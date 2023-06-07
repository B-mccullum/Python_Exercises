import boto3
import os

# Specify the desired key name and file name for the private key
key_name = "Key from Boto3"
file_name = 'key-from-boto3.pem'

# Create an EC2 client
ec2 = boto3.client('ec2')

# Generate a new key pair and obtain the private key material
response = ec2.create_key_pair(KeyName=key_name)

# Save the private key material to a file
with open(file_name, 'w') as f:
    f.write(response["KeyMaterial"])

# Set restrictive permissions (read-only by the owner) for the private key file
os.chmod(file_name, 0o400)
