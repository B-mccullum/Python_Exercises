import boto3

s3 = boto3.client('s3')

bucket = 'bmccullum-boto3-06022023'
key = 'test_text_string.txt'

# Retrieve the object from the specified S3 bucket and key
response = s3.get_object(Bucket=bucket, Key=key)

# Read the content of the object
object_content = response['Body'].read()

# Decode the content from bytes to UTF-8 string
contents = object_content.decode('utf-8')

# Print the contents of the object
print(contents)
