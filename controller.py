from sqs import SQS


def main():
    
    sqs = SQS()
    # Input queue
    sqs.send_request('input test')
    print(f'Request message: {sqs.receive_input()}')
    # Output queue
    sqs.send_response('response test')
    print(f'Response message: {sqs.receive_output()}')
    

if __name__ == '__main__':
    main()