import boto3

s3 = boto3.client('s3')

bucket = "bmccullum-boto3-06022023"
key = "test_text_string.txt"

# Configure public access block settings for the S3 bucket
response = s3.put_public_access_block(
    Bucket=bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

# Configure ownership controls for the S3 bucket
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

# Set the bucket ACL to private
response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket,
)

# Set the object ACL to public-read for the specified bucket and key
response = s3.put_object_acl(
    ACL='public-read',
    Bucket=bucket,
    Key=key
)

print(response)
