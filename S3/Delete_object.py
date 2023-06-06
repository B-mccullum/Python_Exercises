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
        

if __name__ == '__main__':
    bucket = "bmccullum-boto3-06022023"
    s3= boto3.client('s3')
    
    prefix="folder/fodlera/"
    
    keys = list_objects_keys(s3, bucket, prefix=prefix)
    
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    print(keys)
    delete_objects(s3, bucket, keys)
