import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="bmccullum-boto3-06022023", 
                Key="folder/foldera/folder1/test_text_string.txt" , 
                Body="Hey this is a string", 
                ContentType="text/plain")
  


