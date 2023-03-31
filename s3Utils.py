# import os
import boto3
from botocore.exceptions import ClientError

class S3Utils:
    def __init__(self):
        self.access_key = 'AKIATR3L5NH5KTIH7B57'
        self.secret = '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'
        self.bucket_name = 'ineuron-courses-buckets'
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret
        )
    def upload_file(self, file_path):
        try:
            file_name=file_path.split("/")[-1]
            self.s3_client.upload_file(
                file_path,
                self.bucket_name,
                file_name
            )
        except ClientError as ce:
            print("Incorrect Credentials")
            print(e)
        except Exception as e:
            print(e)