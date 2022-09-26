# CSE-546-IaaS
### Names: Junghwan Park, Sivanarayana Nagulapati, Ritvik Ramdas

##### Junghwan Park Completed Tasks:
- Configuration for AWS access and setup.
- Python class implementations for SQS, EC2, and S3 using boto3.
- App instance user data that instructs each instance to follow a series of tasks:
    1. Setup environment
    2. Get image request from SQS input queue
    3. Download image from S3
    4. Run image classification on image
    5. Send output to SQS output queue and S3 output bucket.
- Project report writeup.

##### Sivanarayana Nagulapati Completed Tasks:
- 
- Project report writeup.

##### Ritvik Ramdas Completed Tasks:
- 
- Project report writeup.

### AWS Elements

##### SQS
- InputQueue
- OutputQueue

##### EC2
- web-instance
- app-instance

##### S3
- image-inputbucket
- resultpair-outputbucket