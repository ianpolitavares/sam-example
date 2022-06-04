import boto3
import json


def hello(event, context):
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('sam-app-srcbucket-16f8dlu093ts5')

    for my_bucket_object in bucket.objects.all():
        if my_bucket_object.key == 'tbrzien.json' or my_bucket_object.key == 'tbrzien2.json':
            print('entrou')

            body = my_bucket_object.get()['Body'].read()
            loaded = body.decode('utf-8')
            lines = loaded.splitlines()
            print(lines)


    return "end"