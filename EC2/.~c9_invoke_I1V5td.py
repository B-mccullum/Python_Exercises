import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(Owners=['self'])

for image in response["Images"]:
    print(image["ImageId"], image["Name"], image["CreationDate"])
    
