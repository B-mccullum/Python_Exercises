import boto3

s3 = boto3.client('s3')

bucket = "bmccullum-boto3-06022023"
key = "test_text_string.txt"

response = s3.put_public_access_block(
    Bucket=bucket,
    
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket,
)



response = s3.put_object_acl(ACL='public-read', Bucket="bmccullum-boto3-06022023", Key="test_text_string.txt")


print(response)