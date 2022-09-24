import boto3
import config


# AWS S3 class
class S3:

    # Initialize S3 bucket client
    def __init__(self):
        self.s3_client = boto3.client(
            service_name='s3', 
            region_name=config.REGION, 
            aws_access_key_id=config.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
    
    
    # Store an image to the input bucket
    def store_image(self, image_path, image_key):
        response = self.s3_client.upload_file(image_path, config.INPUT_BUCKET_NAME, image_key)
        print('Successfully stored new image')