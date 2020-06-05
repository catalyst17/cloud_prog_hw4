import sys
import requests
import boto3


def obtain_temporary_credentials() -> (str, str, str):
    """Obtain temporary credentials from AWS IoT device certificate and private key."""
    credential_provider_endpoint = 'https://c2svzaf1dnajce.credentials.iot.us-east-1.amazonaws.com/role-aliases/iot-s3-access-role-alias/credentials'
    device_cert_path = '~/certs/aws_iot_arsen/certificate.pem.crt'
    device_private_key_path = '~/certs/aws_iot_arsen/private.pem.key'
    resp = requests.get(
        credential_provider_endpoint,
        headers={'x-amzn-iot-thingname': 'RaspberryPi'},
        cert=(device_cert_path, device_private_key_path),
    )

    if resp:  # check whether https request succeeds
        credentials = resp.json()
        access_key_id = credentials['credentials']['accessKeyId']
        secrete_access_key = credentials['credentials']['secretAccessKey']
        session_token = credentials['credentials']['sessionToken']
        return access_key_id, secrete_access_key, session_token
    else:
        print('error requesting temporary access to AWS S3')
        return '', '', ''


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