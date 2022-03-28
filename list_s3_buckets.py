import json
import boto3

s3=boto3.resource('s3')
def lambda_handler(event,context):
    bucket_list=[]
    for bucket in s3.buckets.all(): ##before that roles and policy has been provided to accesss s3 
        print(bucket.name)
        bucket_list.append(bucket.name)
    return {
        'statusCode':200,
        'body':bucket_list
    }