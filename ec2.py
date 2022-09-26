import boto3
import config


# AWS EC2 class
class EC2:

    # Initialize EC2 client and resource
    def __init__(self):
        # EC2 Client
        self.ec2_client = boto3.client(
            service_name='ec2', 
            region_name=config.REGION, 
            aws_access_key_id=config.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
        # EC2 Resource
        self.ec2_resource = boto3.resource(
            service_name='ec2', 
            region_name=config.REGION, 
            aws_access_key_id=config.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )


    # Create an app instance and return it
    def create_app_instance(self):
        instance = self.ec2_resource.create_instances(
            ImageId=config.MODEL_IMAGE_ID,
            MinCount=1,
            MaxCount=1,
            UserData=config.USER_DATA
        )
        
        return instance[0]


    # Start an instance
    def start_instance(self, instance_id):
        self.ec2_client.start_instances(InstanceIds=[instance_id])
        print(f'Successfully started instance {instance_id}')

    
    # Stop an instance
    def stop_instance(self, instance_id):
        self.ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f'Successfully stopped instance {instance_id}')


    # Terminate an instance
    def terminate_instance(self, instance):
        instance.terminate()
        print(f'Successfully terminated instance {instance.id}')