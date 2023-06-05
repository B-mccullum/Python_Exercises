import boto3


def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket, 
        Key=key
        )
    return response

def delete_objects(client, buckets, keys):
    objects = [{'Key': key} for key in keys]
     
  
    response = client.delete_objects(
        Bucket=bucket, 
        Delete={
            'Objects':objects
        }
    )
    
    return response
        
bucket = "bmccullum-boto3-06022023"
key = "test_text.txt"

s3= boto3.client('s3')

keys = ["test_text_string.txt", "test_text_upload.txt"]

delete_objects(s3, bucket, keys)
