import sys
import boto3

s3_client = boto3.client('s3')


def upload_to_s3(local_file, bucket, s3_file):
    try:
        s3_client.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except:
        print(sys.exc_info())
        return False
    

upload_to_s3("jdj.jpg", "nthu-x1080066", "jdj.jpg")