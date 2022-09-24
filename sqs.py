import boto3
import config


# AWS Simple Queue Service class
class SQS:

    # Initialize SQS client
    def __init__(self):
        self.sqs_client = boto3.client(
            service_name='sqs', 
            region_name=config.REGION, 
            aws_access_key_id=config.AWS_ACCESS_KEY_ID, 
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
    
    
    # Send an image to the input queue
    def send_request(self, image_key):
        self.sqs_client.send_message(QueueUrl=config.INPUT_QUEUE_URL, MessageBody=image_key)
        print('Successfully sent request to the input queue')
    

    # Send an response to the output queue
    def send_response(self, result):
        self.sqs_client.send_message(QueueUrl=config.OUTPUT_QUEUE_URL, MessageBody=result)
        print('Successfully sent response to the output queue')

    
    # Receive and delete message from input queue
    def receive_input(self):
        try:
            # Get response
            response = self.sqs_client.receive_message(QueueUrl=config.INPUT_QUEUE_URL)
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            print('Received request from input queue')

            # Delete reponse
            self.sqs_client.delete_message(QueueUrl=config.INPUT_QUEUE_URL, ReceiptHandle=receipt_handle)

            return message['Body']
        except KeyError:
            print('Error: there is nothing in the input queue to receive')


    # Receive and delete message from output queue
    def receive_output(self):
        try:
            # Get response
            response = self.sqs_client.receive_message(QueueUrl=config.OUTPUT_QUEUE_URL)
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            print('Received response from output queue')

            # Delete reponse
            self.sqs_client.delete_message(QueueUrl=config.OUTPUT_QUEUE_URL, ReceiptHandle=receipt_handle)

            return message['Body']
        except KeyError:
            print('Error: there is nothing in the output queue to receive')