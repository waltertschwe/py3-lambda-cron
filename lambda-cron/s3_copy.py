import boto3
import json
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = s3.Bucket('blur-garbage-in')
    dest_bucket = s3.Bucket('blur-garbage-out')
    print(bucket)
    print(dest_bucket)

    for obj in bucket.objects.all():
        dest_key = obj.key
        print(dest_key)
        s3.Object(
            dest_bucket.name,
            dest_key)
        .copy_from(
            CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key}
        )
