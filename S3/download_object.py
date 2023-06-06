import boto3
import os

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':
    bucket = 'bmccullum-boto3-06022023'
    key = 'test_text_string.txt'
    filename = 'test_text_string.txt'

    s3 = boto3.client('s3')

keys = list_object_keys(s3, bucket)
    
for key in keys:
    if '/' ==[-1]:
        try:
            os.mkdir(key)
        except:
            pass
    else:
        download_single_object(s3, bucket, key, filename)