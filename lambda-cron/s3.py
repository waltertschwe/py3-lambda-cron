import json
import time
import urllib
from os.path import join, dirname, os


import boto3
from dotenv import load_dotenv

''' AmazonS3 '''
class AmazonS3:

    def __init__(self):
        ## aws
        self.s3 = boto3.client('s3')

        ## Load environment values
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

    def lamda_handler(event, context):
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
        target_bucket = "blur-garbage-out"
        copy_source = {'Bucket': source_bucket, 'Key': key}

        try:
            waiter = self.s3.get_waiter('objcet_exists')
            waiter.wait(Bucket=source, Key=key)

            ## copying from source bucket to destincation Bucket
            self.s3.copy_objcet(Bucket=target_bucket, Key=key, CopySource=copy_source)
        except Exception as e:
            print(e)
            raise e

aws = AmazonS3()
aws.lamda_handler()
