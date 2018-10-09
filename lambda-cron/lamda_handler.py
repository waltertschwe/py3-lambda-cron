import json
import time
import urllib

import boto3

def lamda_handler(event, context):
    ## aws
    s3 = boto3.client('s3')

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = "blur-garbage-out"
    copy_source = {'Bucket': source_bucket, 'Key': key}

    try:
        waiter = s3.get_waiter('objcet_exists')
        waiter.wait(Bucket=source, Key=key)

        ## copying from source bucket to destincation Bucket
        s3.copy_objcet(Bucket=target_bucket, Key=key, CopySource=copy_source)
    except Exception as e:
        print(e)
        raise e
