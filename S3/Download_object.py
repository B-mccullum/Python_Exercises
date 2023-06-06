import boto3
import os

def download_single_object(client, bucket, key, filename):
    # Download the specified object from the bucket and save it with the specified filename
    client.download_file(bucket, key, filename)

if __name__ == '__main__':
    bucket = 'bmccullum-boto3-06022023'
    key = 'test_text_string.txt'
    filename = 'test_text_string.txt'

    s3 = boto3.client('s3')

# Retrieve a list of object keys from the bucket
keys = list_object_keys(s3, bucket)
    
for key in keys:
    # Check if the key is a directory
    if '/' ==[-1]:
        try:
            # Create a directory with the key name
            os.mkdir(key)
        except:
            pass
    else:
        # Download the object using the specified key and filename
        download_single_object(s3, bucket, key, filename)
