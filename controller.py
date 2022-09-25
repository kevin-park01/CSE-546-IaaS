from sqs import SQS
from s3 import S3
from ec2 import EC2


def main():
    '''
    # Examples:

    sqs = SQS()
    # Input queue
    sqs.send_request('input test')
    print(f'Request message: {sqs.receive_input()}')
    # Output queue
    sqs.send_response('response test')
    print(f'Response message: {sqs.receive_output()}')

    s3 = S3()
    s3.store_image('./images/test_0.JPEG', 'test_0.JPEG')    
    
    ec2 = EC2()
    # Start web instance
    ec2.start_web_instance()
    # Create, start, and terminate an app instance
    inst = ec2.create_app_instance()
    ec2.start_instance(inst.id)
    ec2.terminate_instance(inst)
    # Stop web instance
    ec2.stop_web_instance()
    '''

    


if __name__ == '__main__':
    main()