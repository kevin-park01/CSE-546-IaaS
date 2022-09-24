from sqs import SQS
from s3 import S3


def main():
    
    sqs = SQS()
    # Input queue
    sqs.send_request('input test')
    print(f'Request message: {sqs.receive_input()}')
    # Output queue
    sqs.send_response('response test')
    print(f'Response message: {sqs.receive_output()}')

    s3 = S3()
    s3.store_image('./images/test_0.JPEG', 'test_0.JPEG')    


if __name__ == '__main__':
    main()